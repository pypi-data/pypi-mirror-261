import copy
import hashlib
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Tuple, Union

from datasets.utils.extract import ZstdExtractor as Extractor

from data_juicer.utils.constant import DEFAULT_PREFIX


def find_files_with_suffix(
        path: Union[str, Path],
        suffixes: Union[str, List[str], Tuple[str]] = None) -> List[str]:
    """
    Traverse a path to find all files with the specified suffixes.

    :param path: path (str/Path): source path
    :param suffixes: specified file suffixes, '.txt' or ['.txt', '.md']
        etc
    :return: list of all files with the specified suffixes
    """
    path = Path(path)
    file_dict = {}

    if suffixes is None:
        suffixes = []

    if isinstance(suffixes, str):
        suffixes = [suffixes]

    suffixes = [
        x.lower() if x.startswith('.') else '.' + x.lower() for x in suffixes
    ]

    if path.is_file():
        files = [path]
    else:
        searched_files = path.rglob('*')
        files = [file for file in searched_files if file.is_file()]

    extractor = Extractor

    # only keep the file with the specified suffixes
    for file in files:
        suffix = file.suffix.lower()

        if extractor.is_extractable(file):

            # TODO
            # hard code
            # only support zstd-format file now,
            # and use the last 2 sub-suffixes as the final suffix
            # just like '.jsonl.zst'
            file_suffixes = [suffix.lower() for suffix in file.suffixes]
            suffix = ''.join(file_suffixes[-2:])

        if not suffixes or (suffix in suffixes):
            if suffix not in file_dict:
                file_dict[suffix] = [str(file)]
            else:
                file_dict[suffix].append(str(file))
    return file_dict


def is_absolute_path(path: Union[str, Path]) -> bool:
    """
    Check whether input path is a absolute path.

    :param path: input path
    :return: True means input path is absolute path, False means input
        path is a relative path.
    """
    return Path(path).is_absolute()


def add_suffix_to_filename(filename, suffix):
    """
    Add a suffix to the filename. Only regard the content after the last dot
    as the file extension.
    E.g.
    1. abc.jpg + "_resized" --> abc_resized.jpg
    2. edf.xyz.csv + "_processed" --> edf.xyz_processed.csv
    3. /path/to/file.json + "_suf" --> /path/to/file_suf.json
    4. ds.tar.gz + "_whoops" --> ds.tar_whoops.gz (maybe unexpected)

    :param filename: input filename
    :param suffix: suffix string to be added
    """
    name, ext = os.path.splitext(filename)
    new_name = f'{name}{suffix}{ext}'
    return new_name


def dict_to_hash(input_dict, hash_length=None):
    """
        hash a dict to a string with length hash_length

        :param input_dict: the given dict
    """
    sorted_items = sorted(input_dict.items())
    dict_string = str(sorted_items).encode()
    hasher = hashlib.sha256()
    hasher.update(dict_string)
    hash_value = hasher.hexdigest()
    if hash_length:
        hash_value = hash_value[:hash_length]
    return hash_value


def create_directory_if_not_exists(directory_path):
    """
        create a directory if not exists, this function is process safe

        :param directory_path: directory path to be create
    """
    try:
        os.makedirs(directory_path, exist_ok=True)
    except FileExistsError:
        # We ignore the except from multi processes or threads.
        # Just make sure the directory exists.
        pass


def transfer_filename(original_filepath: Union[str, Path], op_name,
                      **op_kwargs):
    """
        According to the op and hashing its parameters 'op_kwargs' addition
        to the process id and current time as the 'hash_val', map the
        original_filepath to another unique file path.
        E.g.
        1. abc.jpg -->
            {op_name}/abc__dj_hash_#{hash_val}#.jpg
        2. ./abc.jpg -->
            ./{op_name}/abc__dj_hash_#{hash_val}#.jpg
        3. /path/to/abc.jpg -->
           /path/to/{op_name}/abc__dj_hash_#{hash_val}#.jpg
        4. /path/to/{op_name}/abc.jpg -->
           /path/to/{op_name}/abc__dj_hash_#{hash_val}#.jpg
        5. /path/to/{op_name}/abc__dj_hash_#{hash_val1}#.jpg -->
           /path/to/{op_name}/abc__dj_hash_#{hash_val2}#.jpg
    """
    # produce the directory
    original_dir = os.path.dirname(original_filepath)
    parent_dir = os.path.basename(original_dir)
    if parent_dir == op_name:
        new_dir = original_dir
    else:
        new_dir = os.path.join(original_dir, f'{op_name}')
    create_directory_if_not_exists(new_dir)

    # produce the unique hash code
    unique_parameters = copy.deepcopy(op_kwargs)
    unique_parameters[f'{DEFAULT_PREFIX}pid'] = os.getpid()
    unique_parameters[f'{DEFAULT_PREFIX}timestamp'] = str(
        datetime.now(timezone.utc))
    unique_hash = dict_to_hash(unique_parameters)

    # if the input data is produced by data-juicer, replace the hash code
    # else append hash value to filename
    def add_hash_value(text, new_hash_value):
        pattern = r'__dj_hash_#(.*?)#'

        match = re.search(pattern, text)
        # draw the string produced by data-juicer
        if match:
            text = text[:match.start()]

        return f'{text}__dj_hash_#{new_hash_value}#'

    original_filename = os.path.basename(original_filepath)
    name, ext = os.path.splitext(original_filename)
    new_name = add_hash_value(name, unique_hash)
    new_filepath = os.path.join(new_dir, f'{new_name}{ext}')

    return new_filepath
