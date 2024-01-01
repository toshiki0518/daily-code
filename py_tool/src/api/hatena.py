import sys
from basic import BaseApi
import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
from requests_oauthlib import OAuth1

class HatenaApi(BaseApi):
    pass

    def test(self):
        # OAuthクライアント情報
        consumer_key = 'BmOlklAt4Lrriw=='
        consumer_secret = 'kv79VdV5iSU5CIBm5oVS8E0zgk8='
        access_token = 'YOUR_ACCESS_TOKEN'
        access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

        # 記事を取得するAPIエンドポイント
        api_url = 'https://blog.hatena.ne.jp/{user_id}/{blog_id}/atom/entry'

        # ユーザーIDとブログID（自分のものに置き換えてください）
        user_id = 'your_user_id'
        blog_id = 'your_blog_id'

        # OAuth認証オブジェクトの作成
        oauth = OAuth1(
            client_key=consumer_key,
            client_secret=consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret
        )

        # 記事の取得
        response = requests.get(api_url.format(user_id=user_id, blog_id=blog_id), auth=oauth)

        # 結果の表示
        if response.status_code == 200:
            print(response.text)
        else:
            print(f"Error: {response.status_code}, {response.text}")

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

    def get_request_token(self):
        pass

    def get_user(self):
        self.authentification()
        self.url = "http://n.hatena.com/applications/my.json"
        self.get()

    def authentification(self):
        self.url = "https://www.hatena.com/oauth/initiate"
        self.get()

def main():
    url = "https://httpbin.org/get"
    api = HatenaApi(url)
    api.get_user()
    # api.get_service()
    print("test")

if __name__ == "__main__":
    main()