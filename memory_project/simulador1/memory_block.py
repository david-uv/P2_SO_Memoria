
from process import Process

class MemoryBlock:
    def __init__(
        self,
        start_address: int,
        size: int,
        is_free: bool = True,
        process: Process = None
    ):
        self.start_address = start_address
        self.size = size
        self.is_free = is_free
        self.process = process

    def __str__(self):
        if self.is_free:
            return (
                f"[FREE | Start={self.start_address}"
                f" | Size={self.size}]"
            )

        return (
            f"[{self.process.pid}"
            f" | Start={self.start_address}"
            f" | Size={self.size}]"
        )    