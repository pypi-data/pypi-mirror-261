from __future__ import annotations
from typing import List
import random

from .enums import (
    ForegroundColor,
    BackgroundColor,
    Style,
)


class Log:
    """Log color text"""

    def __init__(self, debug: bool = True) -> None:
        self.debug = debug

    def primary(self, text: str) -> str:
        """Log primary color text"""

        if self.debug:
            print(f"\033[94m{text}\033[0m")
            return ""

        return f"\033[94m{text}\033[0m"

    def blue(self, text: str) -> str:
        """Log blue color text"""

        if self.debug:
            print(f"\033[94m{text}\033[0m")
            return ""

        return f"\033[94m{text}\033[0m"

    def success(self, text: str) -> str:
        """Log success color text"""

        if self.debug:
            print(f"\033[92m{text}\033[0m")
            return ""

        return f"\033[92m{text}\033[0m"

    def green(self, text: str) -> str:
        """Log green color text"""

        if self.debug:
            print(f"\033[92m{text}\033[0m")
            return ""

        return f"\033[92m{text}\033[0m"

    def ok(self, text: str):
        """Log ok color text"""

        if self.debug:
            print(f"\033[92m{text}\033[0m")
            return ""

        return f"\033[92m{text}\033[0m"

    def warning(self, text: str) -> str:
        """Log warning color text"""

        if self.debug:
            print(f"\033[93m{text}\033[0m")
            return ""

        return f"\033[93m{text}\033[0m"

    def yellow(self, text: str) -> str:
        """Log yellow color text"""

        if self.debug:
            print(f"\033[93m{text}\033[0m")
            return ""

        return f"\033[93m{text}\033[0m"

    def help(self, text: str) -> str:
        """Log help color text"""

        if self.debug:
            print(f"\033[93m{text}\033[0m")
            return ""

        return f"\033[93m{text}\033[0m"

    def danger(self, text: str) -> str:
        """Log danger color text"""

        if self.debug:
            print(f"\033[31m{text}\033[0m")
            return ""

        return f"\033[31m{text}\033[0m"

    def error(self, text: str) -> str:
        """Log error color text"""

        if self.debug:
            print(f"\033[31m{text}\033[0m")
            return ""

        return f"\033[31m{text}\033[0m"

    def fail(self, text: str) -> str:
        """Log fail color text"""

        if self.debug:
            print(f"\033[31m{text}\033[0m")
            return ""

        return f"\033[31m\033[1m{text}\033[0m"

    def underline(self, text: str) -> str:
        """Log underline text"""

        if self.debug:
            print(f"\033[4m{text}\033[0m")
            return ""

        return f"\033[4m{text}\033[0m"

    def bold(self, text: str) -> str:
        """Log bold text"""

        if self.debug:
            print(f"\033[1m{text}\033[0m")
            return ""

        return f"\033[1m{text}\033[0m"

    def okmsg(self, text: str) -> str:
        """Log ok message text"""

        if self.debug:
            print(f"\033[1m\033[92m\u2705 {text}\033[0m")
            return ""

        return f"\033[1m\033[92m\u2705 {text}\033[0m"

    def waitmsg(self, text: str) -> str:
        """Log wait message text"""

        if self.debug:
            print(f"\033[1m\033[93m\u231b {text}\033[0m")
            return ""

        return f"\033[1m\033[93m\u231b {text}\033[0m"

    def errormsg(self, text: str) -> str:
        """Log error message text"""

        if self.debug:
            print(f"\033[1m\033[31m\u274C {text}\033[0m")
            return ""

        return f"\033[1m\033[31m\u274C {text}\033[0m"


class Highlight:
    """Background highlighting"""

    @staticmethod
    def white(text: str) -> str:
        """Highlight text with white background"""

        return f"\x1B[3m{text}\033[0m"

    @staticmethod
    def bwhite(text: str) -> str:
        """Highlight text with bold white background"""

        return f"\x1B[3m\033[1m{text}\033[0m"

    @staticmethod
    def green(text: str) -> str:
        """Highlight text with green background"""

        return f"\x1B[3m\033[92m{text}\033[0m"

    @staticmethod
    def bgreen(text: str) -> str:
        """Highlight text with bold green background"""

        return f"\x1B[3m\033[1m\033[92m{text}\033[0m"

    @staticmethod
    def blue(text: str) -> str:
        """Highlight text with blue background"""

        return f"\x1B[3m\033[94m{text}\033[0m"

    @staticmethod
    def bblue(text: str) -> str:
        """Highlight text with bold blue background"""

        return f"\x1B[3m\033[1m\033[94m{text}\033[0m"

    @staticmethod
    def yellow(text: str) -> str:
        """Highlight text with yellow background"""

        return f"\x1B[3m\033[93m{text}\033[0m"

    @staticmethod
    def byellow(text: str) -> str:
        """Highlight text with bold yellow background"""

        return f"\x1B[3m\033[1m\033[93m{text}\033[0m"

    @staticmethod
    def red(text: str) -> str:
        """Highlight text with red background"""

        return f"\x1B[3m\033[91m{text}\033[0m"

    @staticmethod
    def bred(text: str) -> str:
        """Highlight text with bold red background"""

        return f"\x1B[3m\033[1m\033[91m{text}\033[0m"


class Text:
    """Text a one line color manager for your terminal."""

    def __init__(
        self,
        text: str,
        fg: ForegroundColor = ForegroundColor.WHITE,
        bg: BackgroundColor = BackgroundColor.TRANSPARENT,
        styles: List[Style] = [],
    ) -> None:
        if not isinstance(fg, ForegroundColor):  # type: ignore
            raise TypeError(
                "Foreground color must be an instance of ForegroundColor enum type."
            )

        if not isinstance(bg, BackgroundColor):  # type: ignore
            raise TypeError(
                "Background color must be an instance of BackgroundColor enum type."
            )

        if (
            not isinstance(styles, list)  # type: ignore
            or styles != []
            and not all(isinstance(style, Style) for style in styles)  # type: ignore
        ):
            raise TypeError("Styles must be a list of Style enum type.")

        self.text = text
        self.styles = self.style(styles)
        self.fg = fg.value
        self.bg = bg.value

    def foreground(self, color: ForegroundColor) -> Text:
        """Set or update foreground color"""

        self.fg = color.value
        return self

    def background(self, color: BackgroundColor) -> Text:
        """Set or update background color"""

        self.bg = color.value
        return self

    def style(self, styles: List[Style]) -> str:
        """Set or update styles"""

        self._style: str = "".join([item.value for item in styles])
        return self._style

    def print(self) -> None:
        """Print the text with color and style."""

        print(self.fg + self.bg + self._style + self.text + Style.CLEAR.value)

    def update(self, text: str) -> Text:
        """Update the text."""

        self.text = text
        return self

    def __str__(self) -> str:
        """Return the text with color and style."""

        return self.fg + self.bg + self._style + self.text + Style.CLEAR.value


def get_random_foreground_color() -> ForegroundColor:
    """Get random foreground color from ForegroundColor enum."""

    return random.choice(list(ForegroundColor))


def get_random_background_color() -> BackgroundColor:
    """Get random background color from BackgroundColor enum."""

    return random.choice(list(BackgroundColor))


def get_random_style() -> Style:
    """Get random style from Style enum."""

    return random.choice(list(Style))
