from memory_block import MemoryBlock


class MemoryManager:

    def __init__(
        self,
        memory_size: int,
        algorithm: str
    ):
        self.memory_size = memory_size
        self.algorithm = algorithm

        self.blocks = [
            MemoryBlock(
                start_address=0,
                size=memory_size
            )
        ]


    def allocate(self, process):
        pass


    def free(self, process_id):
        pass


    def merge_free_blocks(self):
        pass


    def print_memory(self):
        pass


    def print_statistics(self):
        pass