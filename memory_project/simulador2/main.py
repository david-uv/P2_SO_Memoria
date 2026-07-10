
from paging_manager import PagingManager
from paging_executor import PagingExecutor


manager = PagingManager(
    page_size=1024,
    virtual_memory_size=8192,
    physical_memory_size=4096
)

PagingExecutor.execute_file(
    manager,
    "input_paging.txt"
)