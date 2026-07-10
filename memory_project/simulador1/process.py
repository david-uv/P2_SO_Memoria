class Process:
    def __init__(self, pid: str, memory_required: int):
        self.pid = pid
        self.memory_required = memory_required

    def __str__(self):
        return f"{self.pid} ({self.memory_required} MB)"