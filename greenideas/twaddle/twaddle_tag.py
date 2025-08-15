from typing import Optional


def build_twaddle_tag(
    dict_name: str,
    class_specifier: Optional[str | list[str]] = None,
    form: Optional[str] = None,
) -> str:
    tag_contents = dict_name
    if class_specifier:
        if isinstance(class_specifier, list):
            class_specifier = "-".join(class_specifier)
        tag_contents += f"-{class_specifier}"
    if form:
        tag_contents += f".{form}"
    return f"<{tag_contents}>"
