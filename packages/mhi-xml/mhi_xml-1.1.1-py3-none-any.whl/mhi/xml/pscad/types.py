"""
=========
Types
=========
"""


#===============================================================================
# Imports
#===============================================================================

from __future__ import annotations
from typing import NamedTuple
from mhi.xml.types import ParamEnum


#===============================================================================
# Exports
#===============================================================================

__all__ = ['ResourceType',
           'NodeType', 'Signal', 'Electrical',
           'Align', 'LineStyle', 'FillStyle',
           'Point',
           ]


#===============================================================================
# Resource Types
#===============================================================================

class ResourceType(ParamEnum):
    UNKNOWN = '0'
    TEXT = '1'
    BINARY = '2'


#===============================================================================
# Ports
#===============================================================================

class NodeType(ParamEnum):
    """
    Node Input/Output/Electrical Type
    """

    UNKNOWN = '0'
    INPUT = '1'
    OUTPUT = '2'
    ELECTRICAL = '3'
    SHORT = '4'


class SignalType(ParamEnum):
    """
    Signal Types
    """

    ELECTRICAL = '0'
    LOGICAL = '1'
    INTEGER = '2'
    REAL = '3'
    COMPLEX = '4'
    UNKNOWN = '15'


class ElectricalType(ParamEnum):
    """
    Electrical Node Types
    """

    FIXED = '0'
    REMOVABLE = '1'
    SWITCHED = '2'
    GROUND = '3'


#===============================================================================
# Graphics
#===============================================================================

class Align(ParamEnum):
    """
    Text Alignment
    """

    LEFT = '0'
    CENTER = '1'
    RIGHT = '2'


class LineStyle(ParamEnum):
    """
    Line Styles
    """

    SOLID = '0'
    DASH = '1'
    DOT = '2'
    DASHDOT = '3'


class FillStyle(ParamEnum):
    """
    Fill Styles
    """

    HOLLOW = '0'
    SOLID = '1'
    BACKWARD_DIAGONAL = '2'
    FORWARD_DIAGONAL = '3'
    CROSS = '4'
    DIAGONAL_CROSS = '5'
    HORIZONTAL = '6'
    VERTICAL = '7'
    GRADIENT_HORZ = '8'
    GRADIENT_VERT = '9'
    GRADIENT_BACK_DIAG = '10'
    GRADIENT_FORE_DIAG = '11'
    GRADIENT_RADIAL = '12'


#===============================================================================
# Coordinate
#===============================================================================

Point = NamedTuple("Point", [('x', int), ('y', int)])
