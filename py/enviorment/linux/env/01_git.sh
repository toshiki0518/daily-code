# sh env/git.sh user_name email
# 引数の数を確認
if [ "$#" -ne 2 ]; then
  echo "引数エラー: ユーザー名とメールアドレスを指定してください"
  echo "例: $0 user_name user_mail"
  exit 1
fi

apt-get update;
rm daily-code -rf;
apt-get -y purge git;
apt-get -y install git;
git --version;

echo "Setting up Git with Personal Access Token..."
# パーソナルアクセストークンの入力を非表示にするために -s オプションを使用
echo -n "Enter your Personal Access Token: "
read -s token;
echo;

# Gitユーザー設定
git config --global user.name "$1";
git config --global user.email "$2";
git config --global credential.helper store   # credential.helper を store に設定することで、認証情報を保存する

# 設定値の確認
echo "ユーザー名: $(git config --get user.name)";
echo "メールアドレス: $(git config --get user.email)";

# パーソナルアクセストークンを含むURLを生成
git_url="https://$username:$token@github.com/toshiki0518/daily-code.git"

# パーソナルアクセストークンを含むURLでリポジトリをクローン
git clone $git_url

echo "Git has been configured and repository has been cloned."