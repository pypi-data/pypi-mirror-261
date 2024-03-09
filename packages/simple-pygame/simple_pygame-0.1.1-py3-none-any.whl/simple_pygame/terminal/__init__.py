"""
A module for working with the terminal.
"""
import enum as _enum, sys as _sys
from typing import Union as _Union

try:
    import msvcrt as _msvcrt

    os_name = "Windows"
except ImportError:
    try:
        import fcntl as _fcntl
        from os import O_NONBLOCK as _O_NONBLOCK

        from . import pygetch

        os_name = "Unix"
    except ImportError:
        raise OSError("This module doesn't support your OS.") from None

characters = """0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ """
bytes_characters = b"""0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ """

class Keys_Windows(_enum.Enum):
    """
    An enum class that contains Windows keys for convenient representation.
    """
    Tab = b"\t"
    Enter = b"\r"
    Backspace = b"\x08"
    Up_Arrow = b"\x00H"
    Down_Arrow = b"\x00P"
    Right_Arrow = b"\x00M"
    Left_Arrow = b"\x00K"
    F1 = b"\x00;"
    F2 = b"\x00<"
    F3 = b"\x00="
    F4 = b"\x00>"
    F5 = b"\x00?"
    F6 = b"\x00@"
    F7 = b"\x00A"
    F8 = b"\x00B"
    F9 = b"\x00C"
    F10 = b"\x00D"
    F11 = b"\x00\x85"
    F12 = b"\x00\x86"
    Esc = b"\x1b"
    Insert = b"\x00R"
    Delete = b"\x00S"
    Home = b"\x00G"
    End = b"\x00O"
    Page_Up = b"\x00I"
    Page_Down = b"\x00Q"
    Ctrl_C = b"\x03"
    Unknown = "Unknown"

class Keys_Unix(_enum.Enum):
    """
    An enum class that contains Unix keys for convenient representation.
    """
    Tab = "\t"
    Enter = "\r"
    Backspace = "\x7f"
    Up_Arrow = "\x1b[A"
    Down_Arrow = "\x1b[B"
    Right_Arrow = "\x1b[C"
    Left_Arrow = "\x1b[D"
    F1 = "\x1bOP"
    F2 = "\x1bOQ"
    F3 = "\x1bOR"
    F4 = "\x1bOS"
    F5 = "\x1b[15~"
    F6 = "\x1b[17~"
    F7 = "\x1b[18~"
    F8 = "\x1b[19~"
    F9 = "\x1b[20~"
    F10 = "\x1b[21~"
    F11 = "\x1b[23~"
    F12 = "\x1b[24~"
    Esc = "\x1b"
    Insert = "\x1b[2~"
    Delete = "\x1b[3~"
    Home = "\x1b[H"
    End = "\x1b[F"
    Ctrl_C = "\x03"
    Unknown = "Unknown"

def getch_Windows() -> _Union[Keys_Windows, str]:
    """
    Read a keypress and return the resulting character as a `Keys_Windows` object or as a string.
    """
    key = _msvcrt.getch()

    if key in (b"\x00", b"\xe0"):
        key = b"\x00" + _msvcrt.getch()
    elif key in bytes_characters:
        return key.decode(_sys.stdin.encoding)

    try:
        return Keys_Windows(key)
    except ValueError:
        return Keys_Windows.Unknown

def getch_Unix() -> _Union[Keys_Unix, str]:
    """
    Read a keypress and return the resulting character as a `Keys_Unix` object or as a string.
    """
    pygetch.setraw()
    key = pygetch.getch()
    pygetch.setcooked()

    if key == "\x1b":
        flags = _fcntl.fcntl(_sys.stdin, _fcntl.F_GETFL)
        _fcntl.fcntl(_sys.stdin, _fcntl.F_SETFL, flags | _O_NONBLOCK)

        while True:
            data = pygetch.getch()
            if not data:
                break
            key += data

        _fcntl.fcntl(_sys.stdin, _fcntl.F_SETFL, flags)
    elif key in characters:
        return key

    try:
        return Keys_Unix(key)
    except ValueError:
        return Keys_Unix.Unknown

Keys = Keys_Windows if os_name == "Windows" else Keys_Unix
getch = getch_Windows if os_name == "Windows" else getch_Unix