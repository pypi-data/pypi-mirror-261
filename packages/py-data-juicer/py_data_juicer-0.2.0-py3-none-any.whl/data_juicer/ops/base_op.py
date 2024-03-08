import copy

from data_juicer.utils.registry import Registry

OPERATORS = Registry('Operators')


class OP:

    def __init__(
        self,
        text_key: str = None,
        image_key: str = None,
        audio_key: str = None,
        video_key: str = None,
    ):
        """
        Base class of operators.

        :param text_key: the key name of field that stores sample texts
            to be processed.
        :param image_key: the key name of field that stores sample image list
            to be processed
        :param audio_key: the key name of field that stores sample audio list
            to be processed
        :param video_key: the key name of field that stores sample video list
            to be processed
        """
        # init data keys
        if text_key is None:
            text_key = 'text'
        self.text_key = text_key
        if image_key is None:
            image_key = 'images'
        self.image_key = image_key
        if audio_key is None:
            audio_key = 'audios'
        self.audio_key = audio_key
        if video_key is None:
            video_key = 'videos'
        self.video_key = video_key
        self._accelerator = 'cpu'

        from data_juicer.core.data import wrap_func_with_nested_access
        self.process = wrap_func_with_nested_access(self.process)

    def process(self, *args, **kwargs):
        raise NotImplementedError

    def remove_extra_parameters(self, param_dict, keys=None):
        """
            at the begining of the init of the mapper op, call
            self.remove_extra_parameters(locals())
            to get the init parameter dict of the op for convenience

        """
        if keys is None:
            param_dict = {
                k: v
                for k, v in param_dict.items() if not k.startswith('_')
            }
            param_dict.pop('self', None)
        else:
            param_dict = {k: v for k, v in param_dict.items() if k not in keys}
        return param_dict

    def add_parameters(self, init_parameter_dict, **extra_param_dict):
        """
            add parameters for each sample, need to keep extra_param_dict
            and init_parameter_dict unchanged.
        """
        related_parameters = copy.deepcopy(init_parameter_dict)
        related_parameters.update(extra_param_dict)
        return related_parameters


class Mapper(OP):

    def __init__(self,
                 text_key: str = None,
                 image_key: str = None,
                 audio_key: str = None,
                 video_key: str = None,
                 *args,
                 **kwargs):
        """
        Base class that conducts data editing.

        :param text_key: the key name of field that stores sample texts
            to be processed.
        :param image_key: the key name of field that stores sample image list
            to be processed
        :param audio_key: the key name of field that stores sample audio list
            to be processed
        :param video_key: the key name of field that stores sample video list
            to be processed
        """
        super(Mapper, self).__init__(text_key, image_key, audio_key, video_key)

        # In default, it's a normal OP instead of batched OP
        self._batched_op = False

    def process(self, sample):
        """
        For sample level, sample --> sample

        :param sample: sample to process
        :return: processed sample
        """
        raise NotImplementedError

    def is_batched_op(self):
        return self._batched_op


class Filter(OP):

    def __init__(self,
                 text_key: str = None,
                 image_key: str = None,
                 audio_key: str = None,
                 video_key: str = None,
                 *args,
                 **kwargs):
        """
        Base class that removes specific info.

        :param text_key: the key name of field that stores sample texts
            to be processed
        :param image_key: the key name of field that stores sample image list
            to be processed
        :param audio_key: the key name of field that stores sample audio list
            to be processed
        :param video_key: the key name of field that stores sample video list
            to be processed
        """
        super(Filter, self).__init__(text_key, image_key, audio_key, video_key)

        from data_juicer.core.data import wrap_func_with_nested_access
        self.compute_stats = wrap_func_with_nested_access(self.compute_stats)

    def compute_stats(self, sample, context=False):
        """
        Compute stats for the sample which is used as a metric to decide
        whether to filter this sample.

        :param sample: input sample.
        :param context: whether to store context information of intermediate
            vars in the sample temporarily.
        :return: sample with computed stats
        """
        raise NotImplementedError

    def process(self, sample):
        """
        For sample level, sample --> Boolean.

        :param sample: sample to decide whether to filter
        :return: true for keeping and false for filtering
        """
        raise NotImplementedError


class Deduplicator(OP):

    def __init__(self,
                 text_key: str = None,
                 image_key: str = None,
                 audio_key: str = None,
                 video_key: str = None,
                 *args,
                 **kwargs):
        """
        Base class that conducts deduplication.

        :param text_key: the key name of field that stores sample texts
            to be processed
        :param image_key: the key name of field that stores sample image list
            to be processed
        :param audio_key: the key name of field that stores sample audio list
            to be processed
        :param video_key: the key name of field that stores sample video list
            to be processed
        """
        super(Deduplicator, self).__init__(text_key, image_key, audio_key,
                                           video_key)

        from data_juicer.core.data import wrap_func_with_nested_access
        self.compute_hash = wrap_func_with_nested_access(self.compute_hash)

    def compute_hash(self, sample):
        """
        Compute hash values for the sample.

        :param sample: input sample
        :return: sample with computed hash value.
        """
        raise NotImplementedError

    def process(self, dataset, show_num=0):
        """
        For doc-level, dataset --> dataset.

        :param dataset: input dataset
        :param show_num: number of traced samples used when tracer is
            open.
        :return: deduplicated dataset and the sampled duplicate pairs.
        """
        raise NotImplementedError


class Selector(OP):

    def __init__(self,
                 text_key: str = None,
                 image_key: str = None,
                 audio_key: str = None,
                 video_key: str = None,
                 *args,
                 **kwargs):
        """
        Base class that conducts selection in dataset-level.

        :param text_key: the key name of field that stores sample texts
            to be processed
        :param image_key: the key name of field that stores sample image list
            to be processed
        :param audio_key: the key name of field that stores sample audio list
            to be processed
        :param video_key: the key name of field that stores sample video list
            to be processed
        """
        super(Selector, self).__init__(text_key, image_key, audio_key,
                                       video_key)

    def process(self, dataset):
        """
        Dataset --> dataset.

        :param dataset: input dataset
        :return: selected dataset.
        """
        raise NotImplementedError
