from memory_manager import MemoryManager
from process import Process


manager = MemoryManager(
    memory_size=1024,
    algorithm="FIRST_FIT"
)

p1 = Process("P1", 100)
p2 = Process("P2", 200)
p3 = Process("P3", 150)

manager.allocate(p1)
manager.allocate(p2)
manager.allocate(p3)
manager.print_memory()

manager.free("P2")
manager.print_memory()

manager.free("P3")
manager.print_memory()
