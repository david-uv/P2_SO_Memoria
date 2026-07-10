class AllocationAlgorithms:

    @staticmethod
    def first_fit(blocks, required_size):
        for block in blocks:
            if block.is_free and block.size >= required_size:
                return block
        return None

    @staticmethod
    def best_fit(blocks, required_size):
        best_block = None
        for block in blocks:
            if block.is_free and block.size >= required_size:
                if best_block is None or block.size < best_block.size:
                    best_block = block
        return best_block

    @staticmethod
    def worst_fit(blocks, required_size):
        worst_block = None
        for block in blocks:
            if block.is_free and block.size >= required_size:
                if worst_block is None or block.size > worst_block.size:
                    worst_block = block
        return worst_block