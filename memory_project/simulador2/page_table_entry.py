class PageTableEntry:

    def __init__(
        self,
        page_number: int,
        frame_number: int
    ):
        self.page_number = page_number
        self.frame_number = frame_number


        