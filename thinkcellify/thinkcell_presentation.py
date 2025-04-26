from thinkcellify import _json_utils, _base_container, _cli_utils
import subprocess
import json
import os
import logging

NO_NAME_PROVIDED = _base_container.NO_NAME_PROVIDED
DEFAULT_ROW_LABELS = _json_utils._chart_utils.DEFAULT_ROW_LABELS

logger = logging.getLogger(__name__)

class Presentation(_base_container.BaseContainer):
    def add_chart(self, chart_name, header, header_type="string", row_labels=DEFAULT_ROW_LABELS, *rows, row_settings=None):
        self.append(_json_utils.create_chart(chart_name, header, header_type, row_labels, *rows, row_settings))

    def add_text_box(self, name, text):
        self.append(_json_utils.create_text_box(name, text))


    def to_powerpoint(self, output: str):
        output_path = str(output).split(".pptx")[0]
        with _cli_utils._create_ppttc(self.template, output_path, *self._elements) as ppttc_file:
            command = [
            _cli_utils._find_cli(),
            ppttc_file,
            "-o",
            output
            ]
            try:
                subprocess.run(command, check=True, capture_output=True, text=True)
                logger.info("Think-Cell processing successful.")
                return True
            except subprocess.CalledProcessError as e:
                logger.error("Think-Cell CLI fejl: %s", e)
                logger.error("Standard Output: %s", e.stdout)
                logger.error("Standard Error: %s", e.stderr)
                return False
            
            except FileNotFoundError:
                logger.error("Kunne ikke finde think-cell's ppttc.exe. Tjek stien i 'command'.")
                return False
            except Exception as ex:
                logger.exception("Uventet fejl under generering af PowerPoint: %s", ex)
                return False














#pp = Presentation(r"./setup.py", {"name": None, "table": None}, {"name": 2, "table": 3})




