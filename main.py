from backend import Backend
from api_util import APIUtil
from epaperutil import EPaperUtil
from display_controller import DisplayController
from display_outline import DisplayOutline

def main():

    backend = Backend()
    e_paper_util = EPaperUtil()
    e_paper_util.setup_library()

    recipe = Backend.get_recipe()
    qr_code = Backend.get_qr_code(recipe=recipe)
    display_outline = DisplayOutline.with_default_outline()

    displayController = DisplayController()
    displayController.add_text_to_frame(recipe.ready_in_minutes, coordinates=(100, 26))
    displayController.add_image_to_frame(qr_code.qr_code_formatted, (15, 26))

    print(display_outline.header_text)


if __name__ == "__main__":
    main()