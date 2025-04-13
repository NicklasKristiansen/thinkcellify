

__all__ = ["create_text_box"]

def create_text_box(name, text):
    return {
        "name": f"{name}",
        "table": [[{"string": f"{text}"}]]
    }


def create_chart(chart_name, header, header_type="string", *rows):
    return {
        "name": f"{chart_name}",
        "table": [
            [None] + [{f"{header_type}": value} for value in header]

        ]
    }









