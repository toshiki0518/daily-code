# regular expression pattern
import re

class RegularExpression:
    def __init__(self) -> None:
        self.check_value = ""
        pass

    def _detect_number(self):
        c = re.compile("[0-9]")
        result = c.match(self.value)
        if result:
            print("Match found: '{}' at position {}-{}".format(result.group(), result.start(), result.end()))
        else:
            print("No match found.")

    def _detect_numbers(self):
        c = re.compile("[0-9]")
        results = c.findall(self.value)

        if results:
            print("Numbers found: {}".format(results))
        else:
            print("No numbers found.")

    def _detect_alphabet(self):
        c = re.compile("[a-zA-Z]")
        result = c.match(self.value)
        if result:
            print("Match found: '{}' at position {}-{}".format(result.group(), result.start(), result.end()))
        else:
            print("No match found.")

    def _detect_alphabets(self):
        c = re.compile("[a-zA-Z]")
        results = c.findall(self.value)

        if results:
            print("Alphabeticals found: {}".format(results))
        else:
            print("No alphabets found.")

    def _detect_date(self):
        year_pattern = r"[0-9]{4}"
        month_pattern = r"(0[1-9]|1[0-2])"
        day_pattern = r"(0[1-9]|[1-2][0-9]|3[0-1])"

        date_pattern = rf"\b{year_pattern}/{month_pattern}/{day_pattern}\b"
        c = re.compile(date_pattern)
        result = c.match(self.value)
        if result:
            print("Match found: '{}' at position {}-{}".format(result.group(), result.start(), result.end()))
        else:
            print("No match found.")


    def _detect_email(self):
        email = self.value
        # メールアドレスの正規表現パターン
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        # 正規表現にマッチするかどうかを確認
        if re.match(pattern, email):
            print(f"{email} は有効なメールアドレスです。")
            return True
        else:
            print(f"{email} は無効なメールアドレスです。")
            return False

    def _detext_html(self):
        html_doc = self.value
        # HTML内のリンクを抽出する正規表現パターン
        link_pattern = re.compile(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"')

        # HTML内のリンクを抽出
        links = link_pattern.findall(html_doc)

        has_link = False
        # 抽出されたリンクを表示
        for link in links:
            print("Link:", link)
            has_link = True

        return has_link

    def validate(self, value):
        self.value = value
        self._detext_html()
        # self._detect_email()
        # self._detect_date()
        # self._detect_number()
        # self._detect_numbers()
        # self._detect_alphabet()
        # self._detect_alphabets()

def _get_html():
    html_doc = """
    <html>
    <head>
    <title>Sample HTML</title>
    </head>
    <body>
    <h1>Heading</h1>
    <p>This is a paragraph with <a href="https://example.com">a link</a>.</p>
    <p>Another paragraph with <a href="https://example2.com">another link</a>.</p>
    </body>
    </html>
    """
    return html_doc

def _get_values():
    values = []
    values.append(_get_html())
    return values    
    values.append("example1@email.com")
    values.append("example2.email@domain.com")
    values.append("example3@invalid_domain")
    values.append("example4@domain_with_underscores.com")
    values.append("example5.email@longtopleveldomain")
    return values

    values.append("2024/01/22")
    return values
    # values.append("1")
    # values.append("a")
    # values.append("A")
    # values.append("34")
    # values.append("fG")
    # values.append("b2")
    # values.append("3V4")
    # return values

def _check(values):
    re = RegularExpression()
    for v in values:
        re.validate(v)
        print()

def main():
    values = _get_values()
    _check(values)

if __name__ == "__main__":
    main()
