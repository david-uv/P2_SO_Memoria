
from allocation_algorithms import AllocationAlgorithms
from memory_block import MemoryBlock
from process import Process

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

        if self.algorithm == "FIRST_FIT":
            block = AllocationAlgorithms.first_fit(
                self.blocks,
                process.memory_required
            )

        elif self.algorithm == "BEST_FIT":
            block = AllocationAlgorithms.best_fit(
                self.blocks,
                process.memory_required
            )

        elif self.algorithm == "WORST_FIT":
            block = AllocationAlgorithms.worst_fit(
                self.blocks,
                process.memory_required
            )

        if block is None:
            print(
                f"Not enough memory for process {process.pid}"
            )
            return False

        allocated_block = MemoryBlock(
            start_address=block.start_address,
            size=process.memory_required,
            is_free=False,
            process=process
        )

        remaining_size = (
            block.size - process.memory_required
        )

        index = self.blocks.index(block)

        self.blocks.pop(index)

        self.blocks.insert(
            index,
            allocated_block
        )

        if remaining_size > 0:

            remaining_block = MemoryBlock(
                start_address=(
                    block.start_address
                    + process.memory_required
                ),
                size=remaining_size
            )

            self.blocks.insert(
                index + 1,
                remaining_block
            )

        print(
            f"Process {process.pid} allocated successfully."
        )

        return True


    def free(self, process_id):
        for block in self.blocks:
            if (
                not block.is_free
                and block.process.pid == process_id
            ):
                block.is_free = True
                block.process = None
                print(
                    f"Process {process_id} freed successfully."
                )
                
                self.merge_free_blocks()
                return True

        print(f"Process {process_id} not found.")
        return False


    def merge_free_blocks(self):
        i = 0
        while i < len(self.blocks) - 1:

            current_block = self.blocks[i]
            next_block = self.blocks[i + 1]

            if current_block.is_free and next_block.is_free:
                current_block.size += next_block.size
                self.blocks.pop(i + 1)
            else:
                i += 1


    def print_memory(self):
        address_line = ""
        block_line = ""

        for block in self.blocks:
            address_line += f"{block.start_address}---------"

        address_line += str(self.memory_size)

        for block in self.blocks:

            if block.is_free:
                block_line += f"| FREE {block.size} "
            else:
                block_line += (
                    f"| {block.process.pid} "
                    f"{block.size} "
                )

        block_line += "|"

        print("\nCurrent memory state:")
        print(address_line)
        print(block_line)
        print()


    def print_statistics(self):
        
        used_memory = sum(
        block.size
        for block in self.blocks
        if not block.is_free
        )

        free_memory = self.memory_size - used_memory

        allocated_blocks = sum(
            1
            for block in self.blocks
            if not block.is_free
        )

        free_blocks = sum(
            1
            for block in self.blocks
            if block.is_free
        )

        utilization = (
            used_memory / self.memory_size
        ) * 100

        free_blocks_sizes = [
            block.size
            for block in self.blocks
            if block.is_free
        ]

        largest_free_block = (
            max(free_blocks_sizes)
            if free_blocks_sizes
            else 0
        )

        external_fragmentation = (
            free_memory - largest_free_block
        )

        print("\nMemory Statistics")
        print("-------------------------")
        print(f"Total memory: {self.memory_size} MB")
        print(f"Used memory: {used_memory} MB")
        print(f"Free memory: {free_memory} MB")
        print(f"Allocated blocks: {allocated_blocks}")
        print(f"Free blocks: {free_blocks}")
        print(f"Memory utilization: {utilization:.2f}%")
        print(f"Largest free block: {largest_free_block} MB")
        print(f"External fragmentation: {external_fragmentation} MB")
        print(f"Internal fragmentation: 0 MB")