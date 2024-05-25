import sys


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.

    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    # sys.stdout.flush()
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        command = input()
        if command.startswith("exit"):
            cmd_name, exit_code = command.split(" ")
            if exit_code == "0":
                sys.exit(exit_code)
        sys.stdout.write(f"{command}: command not found\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
