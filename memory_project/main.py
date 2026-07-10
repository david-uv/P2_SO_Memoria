from memory_manager import MemoryManager
from input_executor import InputExecutor


algorithms = [
    "FIRST_FIT",
    "BEST_FIT",
    "WORST_FIT"
]

for algorithm in algorithms:

    print("\n")
    print("=" * 50)
    print(f"Testing {algorithm}")
    print("=" * 50)

    manager = MemoryManager(
        memory_size=1024,
        algorithm=algorithm
    )

    InputExecutor.execute_file(
        manager,
        "input_memory.txt"
    )

    manager.print_statistics()