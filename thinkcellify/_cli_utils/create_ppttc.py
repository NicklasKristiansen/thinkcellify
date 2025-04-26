from contextlib import contextmanager
import os, json
__all__ = ["_create_ppttc"]

@contextmanager
def _create_ppttc(template, output, *elements):
    ppttc_file = f"{output}.ppttc"

    data = [
            {
                "template": template,
                "data": elements
            }
        ]

    json_structure = json.dumps(data, indent=2)

    try:
        with open(ppttc_file, "w", encoding="utf-8") as file:
            file.write(json_structure)
        yield ppttc_file

    finally:
        if os.path.exists(ppttc_file):
            os.remove(ppttc_file)