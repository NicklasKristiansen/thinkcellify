from typing import TypeAlias, Literal


DataType: TypeAlias = Literal["string", "number", "date", "percentage"]

def create_chart(
        chart_name: str,
        header: list | tuple,
        header_type: DataType = "string",
        category_type: DataType = "string",
        *rows: list | tuple,
        row_settings:dict[int] = None
    ): ...
