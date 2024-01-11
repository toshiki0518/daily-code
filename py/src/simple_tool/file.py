class File:
    def __init__(self) -> None:
        pass
    
    def read_introduction(self, target_file_name):
        with open(target_file_name, encoding="utf-8") as f:
            read_data = f.read()
            print(read_data)
        # We can check that the file has been automatically closed.
        f.closed
        return read_data

    def write_introduction(self, file_name):
        with open(file_name, mode="w" ,encoding="utf-8") as f:
            f.write('This is a test\n')
        # We can check that the file has been automatically closed.
        f.closed

    def copy_introduction(self, original_file_name, copy_file_name):
        with open(original_file_name, 'r') as source_file:
            with open(copy_file_name, 'w') as destination_file:
                for line in source_file:
                    destination_file.write(line)
def main():
    file = File()
    target = 'write_workfile'
    file.write_introduction(target)
    file.read_introduction(target)
    file.copy_introduction(target, 'copy_write_workfile')
    pass
if __name__ == "__main__":
    main()