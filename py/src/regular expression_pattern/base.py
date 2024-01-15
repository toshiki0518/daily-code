# regular expression pattern
import re

class RegularExpression:
    def __init__(self) -> None:
        pass

    def detect_number(self, value):
        c = re.compile("[0-9]")
        result = c.match(value)
        if result:
            print("Match found: '{}' at position {}-{}".format(result.group(), result.start(), result.end()))
        else:
            print("No match found.")

    def detect_numbers(self, value):
        c = re.compile("[0-9]")
        results = c.findall(value)

        if results:
            print("Numbers found: {}".format(results))
        else:
            print("No numbers found.")

def detect_number(value):
    re = RegularExpression()
    re.detect_number(value)
    re.detect_numbers(value)
    print()

def main():
    detect_number("1")
    detect_number("b2")
    detect_number("34")
    detect_number("a")

if __name__ == "__main__":
    main()