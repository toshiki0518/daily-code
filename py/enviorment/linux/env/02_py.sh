set -e;
# 標準出力を一時的に捨てる
# exec 3>&1;
# exec 1>/dev/null;

# 環境変数の設定
export PYTHONUNBUFFERED=1;

# aptのアップデートと必要なパッケージのインストール
apt-get update;
apt-get install -y apt-utils;
apt-get install -y libterm-readline-perl-perl;
apt-get install -y python3-venv vim;

# Pythonの仮想環境の構築
python3 -m venv /venv;

# 仮想環境内でのパッケージのインストール
/venv/bin/pip install graphviz;
/venv/bin/pip install numpy;
/venv/bin/pip install requests;
/venv/bin/pip install opencv-python;

# 仮想環境内のPythonバイナリへのパスを通す
export PATH="/venv/bin:$PATH";

# pipのバージョン表示
/venv/bin/pip --version;

