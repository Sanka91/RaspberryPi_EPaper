class ScreenOutline:

    def __init__(self,
                 footnote_text = "",
                 header_text="Hallo Euckenstraße 17",
                 header_coordinates=(85, 0),
                 header_hor_divider=(5, 20, 291, 20),
                 vertical_divider=(105, 25, 105, 103),
                 footnote_hor_divider=(5, 108, 291, 108),
                 footnote_coordinates=(63, 105),
                 ):
        self.header_text = header_text
        self.header_coordinates = header_coordinates
        self.header_hor_divider = header_hor_divider
        self.vertical_divider = vertical_divider
        self.footnote_hor_divider = footnote_hor_divider
        self.footnote_text = footnote_text
        self.footnote_coordinates = footnote_coordinates



