from __future__ import annotations
from typing import List
from unittest import TestCase

import rong


def style_test(styles_list: List[rong.Style]) -> str:
    """Style test code"""
    return "".join([item.value for item in styles_list])


class TestTextClass(TestCase):
    def test_text_default(self) -> None:
        self.assertEqual(rong.Text("test").text, "test")
        self.assertEqual(
            rong.Text("test").fg,
            rong.ForegroundColor.WHITE.value,
        )
        self.assertEqual(
            rong.Text("test").bg,
            rong.BackgroundColor.TRANSPARENT.value,
        )
        self.assertEqual(
            rong.Text("test").styles,
            style_test([]),
        )

    def test_text_fg(self) -> None:
        self.assertEqual(
            rong.Text("test", fg=rong.ForegroundColor.RED).fg,
            rong.ForegroundColor.RED.value,
        )
        self.assertEqual(
            rong.Text("test", fg=rong.ForegroundColor.RED).bg,
            rong.BackgroundColor.TRANSPARENT.value,
        )

    def test_text_bg(self) -> None:
        self.assertEqual(
            rong.Text("test", bg=rong.BackgroundColor.GREEN).bg,
            rong.BackgroundColor.GREEN.value,
        )
        self.assertEqual(
            rong.Text("test", bg=rong.BackgroundColor.GREEN).fg,
            rong.ForegroundColor.WHITE.value,
        )

    def test_text_style(self) -> None:
        self.assertEqual(
            rong.Text("test", styles=[rong.Style.BOLD]).styles,
            style_test([rong.Style.BOLD]),
        )
        self.assertEqual(
            rong.Text("test", styles=[rong.Style.BOLD, rong.Style.UNDERLINE]).styles,
            style_test([rong.Style.BOLD, rong.Style.UNDERLINE]),
        )

    def test_text_foreground_method(self) -> None:
        self.assertEqual(
            rong.Text("test").foreground(rong.ForegroundColor.RED).fg,
            rong.ForegroundColor.RED.value,
        )
        self.assertEqual(
            rong.Text("test").foreground(rong.ForegroundColor.LIGHTGREEN).fg,
            rong.ForegroundColor.LIGHTGREEN.value,
        )

    def test_text_background_method(self) -> None:
        self.assertEqual(
            rong.Text("test").background(rong.BackgroundColor.GREEN).bg,
            rong.BackgroundColor.GREEN.value,
        )
        self.assertEqual(
            rong.Text("test").background(rong.BackgroundColor.LIGHTORANGE).bg,
            rong.BackgroundColor.LIGHTORANGE.value,
        )


class TestTextExpectedFaliure(TestCase):
    def test_text_invalid_fg(self) -> None:
        with self.assertRaises(AttributeError):
            rong.Text("test", fg=rong.ForegroundColor.green)  # type: ignore

        with self.assertRaises(AttributeError):
            rong.Text("test", fg=rong.ForegroundColor.lightorange)  # type: ignore

    def test_text_invalid_bg(self) -> None:
        with self.assertRaises(AttributeError):
            rong.Text("test", bg=rong.BackgroundColor.green)  # type: ignore

        with self.assertRaises(AttributeError):
            rong.Text("test", bg=rong.BackgroundColor.lightorange)  # type: ignore

    def test_text_invalid_style(self) -> None:
        with self.assertRaises(AttributeError):
            rong.Text("test", styles=[rong.Style.bold])  # type: ignore

        with self.assertRaises(AttributeError):
            rong.Text("test", styles=[rong.Style.underline])  # type: ignore

    def test_text_invalid_foreground_method(self) -> None:
        with self.assertRaises(AttributeError):
            rong.Text("test").foreground(rong.ForegroundColor.green)  # type: ignore

        with self.assertRaises(AttributeError):
            rong.Text("test", fg=rong.ForegroundColor.lightorange)  # type: ignore

    def test_text_invalid_background_method(self) -> None:
        with self.assertRaises(AttributeError):
            rong.Text("test").background(rong.BackgroundColor.green)  # type: ignore

        with self.assertRaises(AttributeError):
            rong.Text("test", bg=rong.BackgroundColor.unknown)  # type: ignore
