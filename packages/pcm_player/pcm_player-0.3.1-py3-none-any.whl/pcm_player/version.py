import importlib.metadata

_DISTRIBUTION_METADATA = importlib.metadata.metadata('pcm_player')


class Version:

    @staticmethod
    def name():
        return _DISTRIBUTION_METADATA['Version']