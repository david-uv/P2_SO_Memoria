from process import Process


class InputExecutor:

    @staticmethod
    def execute_file(manager, filename):

        with open(filename, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                parts = line.split()

                command = parts[0]

                if command == "CREATE":

                    pid = parts[1]
                    memory_required = int(parts[2])

                    process = Process(
                        pid,
                        memory_required
                    )

                    manager.allocate(process)

                elif command == "FREE":

                    manager.free(parts[1])

                elif command == "PRINT":

                    manager.print_memory()

                elif command == "STATS":

                    manager.print_statistics()