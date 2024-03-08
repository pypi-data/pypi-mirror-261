import sys
import typing
import bpy.types

from . import types
from . import ops
from . import app
from . import props
from . import msgbus
from . import utils
from . import path

GenericType = typing.TypeVar("GenericType")
context: 'bpy.types.Context' = None

data: 'bpy.types.BlendData' = None
''' Access to Blender's internal data
'''
