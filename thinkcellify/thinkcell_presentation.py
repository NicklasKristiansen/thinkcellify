import os
from thinkcellify import _json_utils
NO_NAME_PROVIDED = object()
DEFAULT_ROW_LABELS = _json_utils._chart_utils.DEFAULT_ROW_LABELS


class Presentation:
    def _validate_path(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"File not found: {path}")
    
    def _validate_element(self, element):
        if not isinstance(element, dict):
            raise ValueError("Element must be a dict or a subclass of dict.")
        if element.get("name", NO_NAME_PROVIDED) == NO_NAME_PROVIDED:
            raise KeyError(f"Element {element} does not have a 'name' key.")
        if element.get("table", NO_NAME_PROVIDED) == NO_NAME_PROVIDED:
            raise KeyError(f"Element {element} does not have a 'table' key.")

    def __init__(self, source, *slide_elements):
        self._validate_path(source)
        self.template = source

        if slide_elements:
            for e in slide_elements:
                self._validate_element(e)

        self._elements = [*slide_elements]
    
    def __repr__(self):
        if not self._elements:
            return "Presentation(<empty>)"
        names = [f"[{i}] {e.get('name', '<no name>')}" for i, e in enumerate(self._elements)]
        return "Presentation(\n  " + "\n  ".join(names) + "\n)"

    def __getitem__(self, s):
        return self._elements[s]

    def append(self, element):
        self._validate_element(element)
        
        self._elements.append(element)
        return self
    
    def extend(self, iterable):
        for e in iterable:
            self._validate_element(e)
        
        self._elements.extend(iterable)
        return self
    
    def __delitem__(self, s):
        del self._elements[s]
    
    def add_chart(self, chart_name, header, header_type="string", row_labels=DEFAULT_ROW_LABELS, *rows, row_settings=None):
        self.append(_json_utils.create_chart(chart_name, header, header_type, row_labels, *rows, row_settings))

    def add_text_box(self, name, text):
        self.append(_json_utils.create_text_box(name, text))













