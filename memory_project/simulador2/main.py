
from paging_manager import PagingManager


manager = PagingManager(
    page_size=1024,
    virtual_memory_size=1024 * 1024,
    physical_memory_size=1024 * 1024
)

manager.map_page(0, 3)
manager.map_page(1, 0)
manager.map_page(2, 5)
manager.map_page(3, 1)

manager.translate_address(2500)


