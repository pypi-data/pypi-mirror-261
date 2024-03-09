"""
A module for working with audio.
"""
import gc as _gc
from typing import Iterable as _Iterable, Tuple as _Tuple

from ..constants import AudioClass

def init(classes: _Iterable = []) -> _Tuple[str, ...]:
    """
    Initialize the mixer module and return successfully initialized classes.

    Parameters
    ----------

    classes (optional): Specifies which classes to initialize. If it's empty, initialize all mixer module classes.
    """
    try:
        classes_len = len(classes)
        iter(classes)
    except TypeError:
        raise TypeError("Classes is not iterable.") from None

    successfully_initialized = []

    if classes_len == 0 or AudioClass in classes:
        try:
            global Audio
            from .audio import Audio
            successfully_initialized.append(AudioClass)
        except ImportError:
            pass

    return (*successfully_initialized,)

def quit(classes: _Iterable = []) -> _Tuple[str, ...]:
    """
    Uninitialize the mixer module and return successfully uninitialized classes.

    Parameters
    ----------

    classes (optional): Specifies which classes to uninitialize. If it's empty, uninitialize all mixer module classes.
    """
    try:
        classes_len = len(classes)
        iter(classes)
    except TypeError:
        raise TypeError("Classes is not iterable.") from None

    successfully_uninitialized = []

    if classes_len == 0 or AudioClass in classes:
        try:
            global Audio
            del Audio
            successfully_uninitialized.append(AudioClass)
        except NameError:
            pass

    _gc.collect()
    return (*successfully_uninitialized,)