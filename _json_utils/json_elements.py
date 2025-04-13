

__all__ = ["create_text_box"]

def create_text_box(name, text):
    """
    Create a simple text box represented as a dictionary with a name and table.

    Args:
        name (str): The name of the text box.
        text (str): The text content to display inside the box.

    Returns:
        dict: A dictionary containing the name and a table with a single cell containing the text.

    Example:
        >>> create_text_box(name="Greeting", text="Hello, world!")
        {
        'name': 'Greeting',
        'table': [[{'string': 'Hello, world!'}]]
    }
    """
    return {
        "name": f"{name}",
        "table": [[{"string": f"{text}"}]]
    }




DEFUALT_ROW_LABELS = object()
def create_chart(chart_name, header, header_type="string", row_labels=DEFUALT_ROW_LABELS, *rows, row_settings=None):
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
            - "fill" (str): Fill color for the cell (e.g., "red", "blue").

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
        ...             1: {"fill": "blue"}
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

    header = [None] + [{f"{header_type}": f"{value}"} for value in header]

    if row_labels is DEFUALT_ROW_LABELS:
        row_labels = [f"Row{i+1}" for i in range(len(rows))]

    if row_settings is None:
        row_settings = {}


    if len(row_labels) != len(rows):
        raise ValueError(f"Antallet af row_labels ({len(row_labels)}) skal matche antallet af datarækker ({len(rows)}).")

    table = [header]

    empty_row = [{"string": ""}] + [None] * (len(header) - 1)

    table.append(empty_row)

    for i, (label, row_data) in enumerate(zip(row_labels, rows)):
        row_config: dict = row_settings.get(i, {})  
        formatted_row = [{"string": label}]

        for j, val in enumerate(row_data):
            cell_options = {}

            if (j + 1) in row_config:
                cell_options = row_config[j + 1]


            data_type = cell_options.get("data_type", row_config.get("data_type", "number"))
            cell_data = {data_type: val}

            if "fill" in cell_options:
                cell_data["fill"] = cell_options["fill"]

            elif "fill" in row_config:
                cell_data["fill"] = row_config["fill"]

            formatted_row.append(cell_data)
        table.append(formatted_row)

 

    return {
        "name": chart_name,
        "table": table
    }










