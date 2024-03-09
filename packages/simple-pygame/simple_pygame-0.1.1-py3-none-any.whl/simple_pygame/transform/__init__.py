"""
A module to transform surfaces.

Requirements
------------

- Pygame library.
"""
import os as _os
_os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = ""

import pygame as _pygame
from typing import Union as _Union, Optional as _Optional, Tuple as _Tuple, List as _List

ColorValue = _Union[_pygame.Color, str, int, _Tuple[int, int, int], _Tuple[int, int, int, int], _List[int]]
RectValue = _Union[_pygame.Rect, _Tuple[int, int, int, int], _List[int], _Tuple[_Tuple[int, int], _Tuple[int, int]], _List[_List[int]]]

def fill(surface: _pygame.Surface, color: ColorValue, rect: _Optional[RectValue] = None, special_flags: int = 0) -> _pygame.Rect:
    """
    Fill the given Surface with a solid color. If the Rect argument is given then only the area inside the specified Rect will be filled, otherwise the entire Surface will be filled.

    Parameters
    ----------

    surface: The Surface to be filled.

    color: The color to fill the Surface with.

    rect (optional): The Rect defining the area that should be filled. If the value is `None`, the entire Surface will be filled.

    special_flags (optional): Additional flags to customize the fill behavior.
    """
    if rect == None:
        return surface.fill(color, special_flags = special_flags)

    try:
        rect = _pygame.Rect(rect) if type(rect) != _pygame.Rect else rect
    except TypeError:
        raise ValueError("Invalid rect style object.") from None

    surface_size = surface.get_size()
    if rect.x < 0:
        rect.x, rect.width = 0, rect.x + rect.width
    elif rect.x > surface_size[0]:
        rect.x, rect.width = surface_size[0], 0
    if rect.y < 0:
        rect.y, rect.height = 0, rect.y + rect.height
    elif rect.y > surface_size[1]:
        rect.y, rect.height = surface_size[1], 0
    rect.width = min(max(0, rect.width), surface_size[0] - rect.x)
    rect.height = min(max(0, rect.height), surface_size[1] - rect.y)

    surface.fill(color, rect, special_flags)
    return rect

def reverse_fill(surface: _pygame.Surface, color: ColorValue, rect: RectValue, special_flags: int = 0) -> _pygame.Rect:
    """
    Fill the area outside the specified Rect on the given Surface with a solid color.

    Parameters
    ----------

    surface: The Surface to be filled.

    color: The color to fill the Surface with.

    rect: The Rect defining the area that should not be filled.

    special_flags (optional): Additional flags to customize the fill behavior.
    """
    try:
        rect = _pygame.Rect(rect) if type(rect) != _pygame.Rect else rect
    except TypeError:
        raise ValueError("Invalid rect style object.") from None

    surface_size = surface.get_size()
    if rect.x < 0:
        rect.x, rect.width = 0, rect.x + rect.width
    elif rect.x > surface_size[0]:
        rect.x, rect.width = surface_size[0], 0
    if rect.y < 0:
        rect.y, rect.height = 0, rect.y + rect.height
    elif rect.y > surface_size[1]:
        rect.y, rect.height = surface_size[1], 0
    rect.width = min(max(0, rect.width), surface_size[0] - rect.x)
    rect.height = min(max(0, rect.height), surface_size[1] - rect.y)

    if (rect.width, rect.height) == surface_size:
        return _pygame.Rect(0, 0, 0, 0)

    subsurface = surface.subsurface(rect).copy()
    surface.fill(color, special_flags = special_flags)
    surface.blit(subsurface, rect)

    subrect = [0, 0, *surface_size]
    if rect.height == surface_size[1] and (rect.x == 0 or rect.x + rect.width == surface_size[0]):
        subrect[0] = rect.width if rect.x == 0 else 0
        subrect[2] -= rect.width
    if rect.width == surface_size[0] and (rect.y == 0 or rect.y + rect.height == surface_size[1]):
        subrect[1] = rect.height if rect.y == 0 else 0
        subrect[3] -= rect.height
    return _pygame.Rect(subrect)