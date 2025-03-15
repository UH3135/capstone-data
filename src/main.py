import os
import json
from pathlib import Path

from parsers.table_parser import TableParser
from parsers.image_ocr import convert_image_to_json
from parsers.data_cleaner import preprocess_markdown
from utils.file_handler import get_data_from_pickling, save_data_from_pickling
from utils.logger import init_logger
from utils.constants import DATA_DIR, OUTPUT_DIR, OUTPUT_JSON, OUTPUT_PICKLE


logger = init_logger(__file__, "DEBUG")


def main():
    total_dict = dict()

    if os.name == "nt":
        try:
            # Linux나 macOS 환경에서는 import 안하도록
            from parsers.process_hwp_docs import HwpController

            
            hwp_ctrl = HwpController()

            for hwp_path in DATA_DIR.rglob("*.hwp"):
                output_path = OUTPUT_DIR / hwp_path.parent.stem

                components = hwp_ctrl.get_tag_from_html(hwp_path)
                components['content'] = hwp_ctrl.extract_text()
                
                if not output_path.exists():
                    os.makedirs(output_path)
                save_data_from_pickling(output_path / f'{hwp_path.stem}.pickle', components)
                
                total_dict[str(hwp_path)] = components
            del hwp_ctrl

        except ImportError:
            logger.error("please install pyhwpx")
    else:
        total_dict = get_data_from_pickling(OUTPUT_PICKLE)
        logger.info(f"Open pickling file: {OUTPUT_PICKLE}")

    table_parser = TableParser()

    for curr_doc in total_dict.keys():
<<<<<<< HEAD
        #table parsing
=======
>>>>>>> 6c5ba3c9be4d67b24c18ae4140face50befd7ab3
        for table_name in total_dict[curr_doc]['tables'].keys():
            total_dict[curr_doc]['tables'][table_name] = table_parser.parse_table_from_html(total_dict[curr_doc]['tables'][table_name])

        # image Text 변환
        # for img_path in curr_doc['images'].keys():
        #     total_dict[curr_doc]['images'][img_path] = convert_image_to_json(Path(img_path))
    
        # Text 전처리
        # total_dict[curr_doc]["texts"] = preprocess_markdown(total_dict[curr_doc]["texts"])

        # Metadata 추가
    
    try:
        with OUTPUT_JSON.open("w", encoding="utf-8") as json_file:
            json.dump(total_dict, json_file, ensure_ascii=False, indent=4)
        logger.info(f"Successfully save json file: {str(OUTPUT_JSON)}")
        
    except Exception as e:
        logger.error(f"Failed save json file: {e}")


if __name__ == "__main__":
    main()