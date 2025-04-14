from typing import TypedDict, TypeAlias

TextBoxName: TypeAlias = str

class ThinkcellTextBoxDict(TypedDict):
    name: TextBoxName
    table: list[list[dict[str, str]]]


ThinkcellTextBox: TypeAlias = ThinkcellTextBoxDict

def create_text_box(
    name: TextBoxName,
    text: str
) -> ThinkcellTextBox: ...


