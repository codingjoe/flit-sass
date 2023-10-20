from flit_core import buildapi
from flit_core.buildapi import *  # noqa

from flit_sass.utils import compile_sass


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    compile_sass()
    return buildapi.build_wheel(wheel_directory, config_settings, metadata_directory)


def build_editable(wheel_directory, config_settings=None, metadata_directory=None):
    compile_sass()
    return buildapi.build_editable(wheel_directory, config_settings, metadata_directory)
