import os
import yaml
import sys

with open("app.yaml", 'r') as stream:
    try:
        config_file = yaml.load(stream)
    except Exception as e:
        sys.exit(str(e))


def _get_config_value(key, default_value=None):
    try:
        default_value = config_file.get(key, default_value)
    except:
        pass

    return os.environ.get(key, default_value)


class BaseConfig(object):
    """
    """
class Development(BaseConfig):
    """
    """
    ENV = 'development'
    pass

class Production(BaseConfig):
    """
    """
    ENV = 'production'
    pass


config = {
    'development': Development,
    'production': Production
}
