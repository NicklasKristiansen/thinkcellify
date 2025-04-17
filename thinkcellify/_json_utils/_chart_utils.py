DEFAULT_ROW_LABELS = object()
def _format_header(header, header_type):
    return [None] + [{header_type: col} for col in header]

def _generate_row_labels(row_labels, count):
    if row_labels is DEFAULT_ROW_LABELS:
        return [f"Row{i+1}" for i in range(count)]
    return row_labels

def _empty_row(length):
    return [{"string": ""}] + [None] * (length - 1)

def _format_cell(val, data_type, fill=None):
    cell = {data_type: val}
    if fill:
        cell["fill"] = fill
    return cell

def _apply_cell_settings(val, j, row_config):
    col_config: dict = row_config.get(j + 1, {})
    data_type = col_config.get("data_type", row_config.get("data_type", "number"))
    fill = col_config.get("fill", row_config.get("fill"))
    return _format_cell(val, data_type, fill)

def _format_data_row(label, row_data, row_config):
    formatted_row = [{"string": label}]
    for j, val in enumerate(row_data):
        formatted_row.append(_apply_cell_settings(val, j, row_config))
    return formatted_row