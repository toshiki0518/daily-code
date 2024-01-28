# sh env/git.sh user_name email
# Check the number of arguments
if [ "$#" -ne 2 ]; then
  echo "Argument error: Please specify both the username and email address."
  echo "Example: $0 user_name user_mail"
  exit 1
fi

apt-get update
rm daily-code -rf
apt-get -y purge git
apt-get -y install git
git --version

echo "Setting up Git with Personal Access Token..."
# Use the -s option to hide the input of the Personal Access Token
echo -n "Enter your Personal Access Token: "
read token
echo

# Git user configuration
git config --global user.name "$1"
git config --global user.email "$2"
git config --global credential.helper store   # Set credential.helper to store to save authentication information

# Confirm configuration values
echo "Username: $(git config --get user.name)"
echo "Email: $(git config --get user.email)"

# Generate URL with Personal Access Token
git_url="https://$username:$token@github.com/toshiki0518/daily-code.git"

# Clone the repository using the URL with Personal Access Token
git clone $git_url

echo "Git has been configured, and the repository has been cloned."
