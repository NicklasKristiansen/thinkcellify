from typing import TypedDict

TEXT_BOX_NAME = str

class ThinkcellTextBoxDict(TypedDict):
    name: TEXT_BOX_NAME
    table: list[list[dict[str, str]]]

THINKCELL_TEXT_BOX_DICT = ThinkcellTextBoxDict

class JSONBase:
    def add_text_box(self, name: TEXT_BOX_NAME, text: str) -> THINKCELL_TEXT_BOX_DICT: ...
