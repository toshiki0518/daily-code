import sys
import requests
from basic import BaseApi

class HatenaApi(BaseApi):
    pass

    def sample(self):
        # GET https://blog.hatena.ne.jp/{はてなID}/{ブログID}/atom
        pass    

    def get_service(self):
        # GET https://blog.hatena.ne.jp/{はてなID}/{ブログID}/atom
        if len(sys.argv) > 2:
            hatena_id = sys.argv[1]
            blog_id = sys.argv[2]
        else:
            hatena_id = input("Please enter hatena id: ")
            blog_id = input("Please enter hatena blog id: ")
        url = "https://blog.hatena.ne.jp/" + hatena_id + "/" + blog_id + "/atom"

        self.url = url
        self.get()

def main():
    url = "https://httpbin.org/get"
    api = HatenaApi(url)
    api.get_service()
    print("test")

if __name__ == "__main__":
    main()