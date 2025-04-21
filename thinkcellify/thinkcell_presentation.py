import pathlib
from thinkcellify import _json_utils
from thinkcellify import _base_container

NO_NAME_PROVIDED = _base_container.NO_NAME_PROVIDED
DEFAULT_ROW_LABELS = _json_utils._chart_utils.DEFAULT_ROW_LABELS


class Presentation(_base_container.BaseContainer):
    def add_chart(self, chart_name, header, header_type="string", row_labels=DEFAULT_ROW_LABELS, *rows, row_settings=None):
        self.append(_json_utils.create_chart(chart_name, header, header_type, row_labels, *rows, row_settings))

    def add_text_box(self, name, text):
        self.append(_json_utils.create_text_box(name, text))





pp = Presentation(r"./setup.py", {"name": None, "table": None}, {"name": 2, "table": 3})



print(pp)




