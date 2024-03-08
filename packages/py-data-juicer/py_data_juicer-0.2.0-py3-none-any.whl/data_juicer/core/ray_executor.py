import os
from functools import partial

import pandas as pd
import pyarrow as pa
from loguru import logger

from data_juicer.config import init_configs
from data_juicer.ops import Filter, Mapper, load_ops
from data_juicer.utils.availability_utils import AvailabilityChecking
from data_juicer.utils.constant import Fields

with AvailabilityChecking(['ray'], requires_type='dist'):
    import ray
    import ray.data as rd


def is_valid_path(item, dataset_dir):
    full_path = os.path.abspath(os.path.join(dataset_dir, item))
    return os.path.exists(full_path)


def convert_to_absolute_paths(dict_with_paths, dataset_dir):
    for key, value in dict_with_paths.items():
        if isinstance(value, list):
            dict_with_paths[key] = [
                os.path.abspath(os.path.join(dataset_dir, item))
                if isinstance(item, str) and is_valid_path(dataset_dir, item)
                else item for item in value
            ]
        elif isinstance(value, str):
            dict_with_paths[key] = os.path.abspath(
                os.path.join(
                    dataset_dir,
                    value)) if isinstance(value, str) and is_valid_path(
                        value, dataset_dir) else value
    return dict_with_paths


def set_dataset_to_absolute_path(dataset, dataset_path):
    """
    Set all the path in input data to absolute path.
    Checks dataset_dir and project_dir for valid paths.
    """
    dataset_dir = os.path.dirname(dataset_path)
    dataset = dataset.map(
        lambda item: convert_to_absolute_paths(item, dataset_dir))
    print(f"transfer {dataset.count()} sample's paths")
    return dataset


def ray_batch_mapper_wrapper(samples, fn):
    samples = samples.to_pandas()
    res = fn(samples)
    if not isinstance(res, pd.DataFrame):
        res = pd.DataFrame(res)
    return pa.Table.from_pandas(res)


class RayExecutor:
    """
    Executor based on Ray [Experimental].

    Run Data-Juicer data processing in a distributed cluster.
        1. Only support Filter and Mapper operators for now.
        2. Only support loading `.json` files.
        2. Advanced functions such as checkpoint, tracer are not supported.
    """

    def __init__(self, cfg=None):
        """
        Initialization method.

        :param cfg: optional config dict.
        """
        self.cfg = init_configs() if cfg is None else cfg

        self.work_dir = self.cfg.work_dir

        self.ops = None
        # init ray
        logger.info('Initing Ray ...')
        ray.init(self.cfg.ray_address)
        self.process_list = self.cfg.process

    def run(self, load_data_np=None):
        """
        Running the dataset process pipeline.

        :param load_data_np: number of workers when loading the dataset.
        :return: processed dataset.
        """
        # 1. load data
        logger.info('Loading dataset with Ray...')
        dataset = rd.read_json(self.cfg.dataset_path)

        # convert all the path in dataset to absolute path
        dataset = set_dataset_to_absolute_path(dataset, self.cfg.dataset_path)
        for items in dataset.iter_rows():
            print('item is:', items)
        # 2. extract processes
        logger.info('Preparing process operators...')
        self.process_list, self.ops = load_ops(self.cfg.process,
                                               self.cfg.op_fusion)

        # 3. data process
        # - If tracer is open, trace each op after it's processed
        # - If checkpoint is open, clean the cache files after each process
        if Fields.stats not in dataset.columns(fetch_if_missing=False):
            logger.info(f'columns {dataset.columns(fetch_if_missing=False)}')

            def process_batch_arrow(table: pa.Table) -> pa.Table:
                new_column_data = [{} for _ in range(len(table))]
                new_talbe = table.append_column(Fields.stats,
                                                [new_column_data])
                return new_talbe

            dataset = dataset.map_batches(process_batch_arrow,
                                          batch_format='pyarrow')

        logger.info('Processing data...')
        for op_cfg, op in zip(self.process_list, self.ops):
            op_name, _ = list(op_cfg.items())[0]
            try:
                if isinstance(op, Mapper):
                    if op.is_batched_op():
                        dataset = dataset.map_batches(partial(
                            ray_batch_mapper_wrapper, fn=op.process),
                                                      batch_format='pyarrow')
                    else:
                        dataset = dataset.map(op.process)
                elif isinstance(op, Filter):
                    dataset = dataset.map(op.compute_stats)
                    dataset = dataset.filter(op.process)
                else:
                    logger.error(
                        'Ray executor only support Filter and Mapper OPs for '
                        'now')
                    raise NotImplementedError
            except:  # noqa: E722
                logger.error(f'An error occurred during Op [{op_name}].')
                import traceback
                traceback.print_exc()
                exit(1)

        # 4. data export
        logger.info('Exporting dataset to disk...')
        dataset.write_json(self.cfg.export_path, force_ascii=False)
        return dataset
