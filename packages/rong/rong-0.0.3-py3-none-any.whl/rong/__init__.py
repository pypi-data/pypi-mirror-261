"""
Rong - A colorizing console utility for Python 3 (open source)
Developed by Md. Almas Ali
Aim to make console coloring easy and fun for developers. Easy to use and easy to customizable. Flexible and powerful.
"""

from .utils import (
    ForegroundColor,
    BackgroundColor,
    Style,
    Log,
    Highlight,
    Text,
    get_random_background_color,
    get_random_foreground_color,
    get_random_style,
)

__version__ = "0.0.3"

__all__ = [
    "ForegroundColor",
    "BackgroundColor",
    "Style",
    "Log",
    "Highlight",
    "Text",
    "get_random_background_color",
    "get_random_foreground_color",
    "get_random_style",
]
