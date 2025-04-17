from ._chart_utils import (
    _format_header,
    _generate_row_labels,
    _empty_row,
    _format_data_row,
    DEFAULT_ROW_LABELS
)

print("id charts: ", id(DEFAULT_ROW_LABELS))

__all__ = ["create_chart", "DEFAULT_ROW_LABELS"]

def create_chart(chart_name, header, header_type="string", row_labels=DEFAULT_ROW_LABELS, *rows, row_settings=None):
    """
    Create a chart structure represented as a dictionary with a name and a table.

    Args:
        chart_name (str): The name/title of the chart.
        header (list): A list of column header values.
        header_type (str, optional): Data type for header cells (e.g., "string", "number"). Defaults to "string".
        row_labels (list, optional): List of row labels. Defaults to ["Row1", "Row2", ...] if not provided.
        *rows (tuple of lists): Each row is a list of values representing a row of data.
        row_settings (dict, optional): Configuration per row index (0-based). Each entry can include:
            - "data_type" (str): Default data type for all cells in the row (e.g., "number", "string").
            - int keys (1-based column indices): Individual cell config dictionaries with optional keys:
            - "data_type" (str): Overrides the row's default data type for this cell.
            - "fill" (str: hex): Fill color for the cell (e.g., "#ff0000").

    Returns:
        dict: A dictionary with keys "name" and "table", representing the chart.

    Raises:
        ValueError: If the number of row labels does not match the number of provided rows.

    Examples:
        >>> create_chart(
        ...     chart_name="Monthly Revenue",
        ...     header=["Jan", "Feb"],
        ...     row_labels=["Product A", "Product B"],
        ...     rows=([1200, 1500], [1000, 1100])
        ... )
        {'name': 'Monthly Revenue',
        'table': [
            [None, {'string': 'Jan'}, {'string': 'Feb'}],
            [{'string': ''}, None, None],
            [{'string': 'Product A'}, {'number': 1200}, {'number': 1500}],
            [{'string': 'Product B'}, {'number': 1000}, {'number': 1100}]
        ]}

        >>> create_chart(
        ...     chart_name="Styled Chart",
        ...     header=["X", "Y"],
        ...     row_labels=["Data Row"],
        ...     rows=([10, 20],),
        ...     row_settings={
        ...         0: {
        ...             "data_type": "number",
        ...             1: {"fill": "#ff0000"}
        ...         }
        ...     }
        ... )
        {'name': 'Styled Chart',
        'table': [
            [None, {'string': 'X'}, {'string': 'Y'}],
            [{'string': ''}, None, None],
            [{'string': 'Data Row'}, {'number': 10, 'fill': 'blue'}, {'number': 20}]
        ]}
    """

    header_row = _format_header(header, header_type)
    row_labels = _generate_row_labels(row_labels, len(rows))
    row_settings = row_settings or {}

    if len(row_labels) != len(rows):
        raise ValueError(
            f"Numbers of row_labels ({len(row_labels)}) should match the number of rows ({len(rows)})."
        )

    table = [header_row, _empty_row(len(header))]

    for i, (label, row_data) in enumerate(zip(row_labels, rows)):
        settings = row_settings.get(i, {})
        table.append(_format_data_row(label, row_data, settings))

    return {"name": chart_name, "table": table}



