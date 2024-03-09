import os
from typing import Optional

import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "st_free_text_select",
        url="https://refactored-sniffle-55g57wxwj5qf4ggp-3001.app.github.dev/",  # "http://localhost:3001",
    )
else:

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component(
        "st_free_text_select", path=build_dir
    )


def st_free_text_select(
    label: str,
    options: list,
    format_func: Optional[callable] = None,
    placeholder: Optional[str] = None,
    disabled: bool = False,
    delay: int = 300,
    key=None,
):

    if format_func is not None:
        options = [format_func(option) for option in options]

    component_value = _component_func(
        label=label,
        options=options,
        placeholder=placeholder,
        disabled=disabled,
        delay=delay,
        key=key,
    )

    return component_value
