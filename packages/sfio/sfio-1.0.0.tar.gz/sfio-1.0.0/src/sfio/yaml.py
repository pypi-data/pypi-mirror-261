# this module extends pyyaml
import yaml
from yaml import *  # noqa: F403, F401

dump_kwargs = {
    'sort_keys': False,
    'default_style': None,
    'default_flow_style': False,
    'allow_unicode': True,
}

import io

from . import abspath, logger
from .json import deserialize, serialize


def read(fpath):
    logger.debug(f'read yaml file\n  {fpath}')
    return deserialize(yaml.safe_load(open(fpath)))


def write(fpath, adict: dict, **kwargs):
    fpath = abspath(fpath)
    yaml.safe_dump(
        serialize(adict), open(fpath, 'w'), **{**dump_kwargs, **kwargs}
    )
    logger.debug(f'wrote yaml file\n  {fpath}')
    return fpath


def loads(astr: str):
    return deserialize(yaml.safe_load(astr))


def dumps(adict: dict, **kwargs):
    stream = io.StringIO()
    yaml.safe_dump(serialize(adict), stream, **{**dump_kwargs, **kwargs})
    stream.seek(0)
    return stream.read().strip()


# -------------------------------------------------------
def represent_quoted(self, data):
    return self.represent_scalar('tag:yaml.org,2002:str', data, style='"')


yaml.add_representer(str, represent_quoted)


# ----- preserve YAML comments -----
#
# from ruamel.yaml import YAML
#
# def represent_none(self, data):
#    return self.represent_scalar('tag:yaml.org,2002:null', 'null')
#
# yaml = Yaml()
# yaml.indent(mapping=2, sequence=4, offset=2)
# yaml.preserve_quotes = True
# yaml.representer.add_representer(type(None), represent_none)
