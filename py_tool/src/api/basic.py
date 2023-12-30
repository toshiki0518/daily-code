import requests

class BaseApi:
    def __init__(self, url = "https://httpbin.org/get") -> None:
        self.url = url

    def test(self):
        # test2
        response = requests.get(self.url)

        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(response.json())
            print(f"Error: {response.status_code}")

    def authentification(self):
        pass
    
    def get(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            print(response)
            print(f"Error: {response.status_code}")

def main():
    url = "https://httpbin.org/get"
    api = BaseApi(url)
    api.test()
    print("test")

if __name__ == "__main__":
    main()