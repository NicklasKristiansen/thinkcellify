from typing import TypedDict, Literal, TypeAlias

TextBoxName: TypeAlias = str

class ThinkcellTextBoxDict(TypedDict):
    name: TextBoxName
    table: list[list[dict[str, str]]]


ThinkcellTextBox: TypeAlias = ThinkcellTextBoxDict

def create_text_box(name: TextBoxName, text: str) -> ThinkcellTextBox: ...


DataType: TypeAlias = Literal["string", "number", "date", "percentage"]

def create_chart(chart_name: str, header: list | tuple, header_type: DataType="string", *rows: list | tuple): ...