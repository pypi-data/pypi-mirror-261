from typing import Optional

from .types import Quality, Criterion, TaskGroup, Task


def to_color_hex_string(color):
    if isinstance(color, str):
        return color
    return f"#{color.red:02x}{color.green:02x}{color.blue:02x}"


def should_hide_code(element: Quality | Criterion | TaskGroup | Task | str | dict) -> bool:
    if isinstance(element, str):
        return element.startswith('_')
    if isinstance(element, dict):
        code: Optional[str] = element.get('code', None)
        if code is None:
            raise ValueError("Element must have a 'code' key")
        return code.startswith('_')
    return element.code.startswith('_')


def get_qualified_name(element: Quality | Criterion | TaskGroup | Task) -> str:
    code = element.code[1:] if element.code.startswith('_') else element.code
    if element.title == code:
        return element.title
    return f"{code} {element.title}"
