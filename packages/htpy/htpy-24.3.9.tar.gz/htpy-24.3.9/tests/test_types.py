from typing import assert_type

from htpy import Element, div, li, ul


def test_element_type() -> None:
    assert_type(div, Element)
    assert_type(div(), Element)
    assert_type(div()["a"], Element)


def test_html_safestring_interface() -> None:
    result = str(div(id="a")).__html__()  # type: ignore[attr-defined]
    assert result == '<div id="a"></div>'


class Test_Children:
    def test_children_as_element(self) -> None:
        child: Element = li
        ul[child]

    def test_children_as_list_element(self) -> None:
        child: list[Element] = [div]
        div[child]
