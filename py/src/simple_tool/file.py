class File:
    def __init__(self) -> None:
        pass
    
    def read_introduction(self):
        with open('workfile', encoding="utf-8") as f:
            read_data = f.read()
            print(read_data)
        # We can check that the file has been automatically closed.
        f.closed

def main():
    file = File()
    file.read_introduction()

    pass
if __name__ == "__main__":
    main()