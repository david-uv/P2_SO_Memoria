class PagingExecutor:

    @staticmethod
    def execute_file(
        manager,
        filename
    ):

        with open(filename,"r") as file:

            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                command = parts[0]

                if command == "MAP":
                    page_number = int(parts[1])
                    frame_number = int(parts[2])
                    manager.map_page(
                        page_number,
                        frame_number
                    )
                elif command == "TRANSLATE":
                    virtual_address = int(
                        parts[1]
                    )
                    manager.translate_address(
                        virtual_address
                    )
                elif command == "TABLE":
                    manager.print_page_table()
                elif command == "FRAMES":
                    manager.print_frames()

