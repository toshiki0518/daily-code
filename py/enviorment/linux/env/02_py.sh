set -e
# Discard standard output temporarily
# exec 3>&1
# exec 1>/dev/null

# Set environment variables
export PYTHONUNBUFFERED=1

# Update apt and install necessary packages
apt-get update
apt-get install -y apt-utils
apt-get install -y libterm-readline-perl-perl
apt-get install -y python3-venv vim

# Create a Python virtual environment
python3 -m venv /venv

# Install packages within the virtual environment
/venv/bin/pip install graphviz
/venv/bin/pip install numpy
/venv/bin/pip install requests
/venv/bin/pip install opencv-python

# Add the virtual environment's Python binary to the PATH
export PATH="/venv/bin:$PATH"

# Display the version of pip
/venv/bin/pip --version
