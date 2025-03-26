import pathlib
from utils.logger import init_logger
from utils.constants import DATA_DIR
from parsers.process_hwp_docs import HwpController

hwp_ctrl = HwpController()

for hwp_path in DATA_DIR.rglob("*.hwp"):

    components = hwp_ctrl.get_tag_from_html(hwp_path)
del hwp_ctrl

print(components)

