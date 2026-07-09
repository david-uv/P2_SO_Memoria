from memory_manager import MemoryManager

manager = MemoryManager(
    memory_size=1024,
    algorithm="FIRST_FIT"
)

manager.print_memory()