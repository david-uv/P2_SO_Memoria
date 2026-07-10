class PagingManager:

    def __init__(
        self,
        page_size: int,
        virtual_memory_size: int,
        physical_memory_size: int
    ):

        self.page_size = page_size
        self.virtual_memory_size = virtual_memory_size
        self.physical_memory_size = physical_memory_size
        self.page_table = {}


    def map_page(
        self,
        page_number: int,
        frame_number: int
    ):
        self.page_table[page_number] = frame_number

        print(
            f"Page {page_number} mapped "
            f"to frame {frame_number}."
        )

    def translate_address(
        self,
        virtual_address: int
    ):

        page_number = ( virtual_address // self.page_size)

        offset = (virtual_address % self.page_size)

        if page_number not in self.page_table:

            print(
                f"Page fault: "
                f"Page {page_number} "
                f"is not mapped."
            )

            return None

        frame_number = self.page_table[page_number]

        physical_address = (
            frame_number *
            self.page_size +
            offset
        )

        print("\nAddress Translation")
        print("-------------------------")
        print(
            f"Virtual address: "
            f"{virtual_address}"
        )
        print(
            f"Page number: "
            f"{page_number}"
        )
        print(
            f"Offset: "
            f"{offset}"
        )
        print(
            f"Frame number: "
            f"{frame_number}"
        )
        print(
            f"Physical address: "
            f"{physical_address}"
        )

        return physical_address
    

    def print_page_table(self):

        total_virtual_pages = (
            self.virtual_memory_size //
            self.page_size
        )

        total_frames = (
            self.physical_memory_size //
            self.page_size
        )

        print("\nPaging Configuration")
        print("-------------------------")
        print(
            f"Page size: "
            f"{self.page_size} bytes"
        )

        print(
            f"Virtual memory size: "
            f"{self.virtual_memory_size} bytes"
        )

        print(
            f"Physical memory size: "
            f"{self.physical_memory_size} bytes"
        )

        print(
            f"Virtual pages: "
            f"{total_virtual_pages}"
        )

        print(
            f"Physical frames: "
            f"{total_frames}"
        )

        print("\nPage Table")
        print("-------------------------")

        for (
            page_number,
            frame_number
        ) in self.page_table.items():

            print(
                f"Page {page_number}"
                f" -> "
                f"Frame {frame_number}"
            )

    def print_frames(self):

        print("\nPhysical Frames")
        print("-------------------------")

        total_frames = (
            self.physical_memory_size //
            self.page_size
        )

        used_frames = set(
            self.page_table.values()
        )

        for frame in range(total_frames):

            if frame in used_frames:
                print(
                    f"Frame {frame}: OCCUPIED"
                )
            else:
                print(
                    f"Frame {frame}: FREE"
                )



