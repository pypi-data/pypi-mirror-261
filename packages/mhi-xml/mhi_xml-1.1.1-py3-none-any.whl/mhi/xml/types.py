"""
=========
Types
=========
"""


#===============================================================================
# Imports
#===============================================================================

from __future__ import annotations
from enum import Enum, EnumMeta
from typing import Self


#===============================================================================
# Exports
#===============================================================================

__all__ = ['ParamEnum',
           ]


#===============================================================================
# Parameter Enum Metatype
#===============================================================================

class ParamEnumType(EnumMeta):

    def __call__(cls, value):

        if isinstance(value, cls):
            return value

        if isinstance(value, str):
            if param_enum := cls.__members__.get(value.upper()):
                return param_enum

        if isinstance(value, int):
            value = str(value)

        return super().__call__(value)


#===============================================================================
# Parameter Enum
#===============================================================================

class ParamEnum(str, Enum, metaclass=ParamEnumType):

    def __new__(cls, value):

        if isinstance(value, int):
            value = str(value)

        return str.__new__(cls, value)


    def __str__(self):
        return self.value
