import sys
from basic import BaseApi
import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session

class GitHubApi(BaseApi):
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

    def get_user(self):
        self.authentification()
        self.url = "http://n.hatena.com/applications/my.json"
        self.get()

    def authentification(self):
        # GitHubのOAuth設定
        client_id = 'your_client_id'
        client_secret = 'your_client_secret'
        authorization_base_url = 'https://github.com/login/oauth/authorize'
        token_url = 'https://github.com/login/oauth/access_token'
        redirect_uri = 'your_redirect_uri'

        # OAuth2セッションを設定
        github = OAuth2Session(client_id, redirect_uri=redirect_uri, scope=['read:user'])

        # 認可URLを取得
        authorization_url, state = github.authorization_url(authorization_base_url)

        print('Please go to %s and authorize access.' % authorization_url)

        # リダイレクト後のURLを入力
        redirect_response = input('Paste the full redirect URL here: ')

        # アクセストークンを取得
        github.fetch_token(token_url, authorization_response=redirect_response, auth=HTTPBasicAuth(client_id, client_secret))

        # 認証されたユーザーの情報を取得
        response = github.get('https://api.github.com/user')
        print('Authenticated user data:', response.json())
        self.get()

def main():
    url = "https://httpbin.org/get"
    api = HatenaApi(url)
    api.get_user()
    # api.get_service()
    print("test")

if __name__ == "__main__":
    main()