# install-pas-pcf
Installing PAS on the Pivotal Cloud Foundry Ops Manager, using Selenium directly from the PCF Ops Manager server


## How to use

### Requirements

- Download Google Chrome and Chrome Driver for Selenium:

Debian:
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
wget https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip
```

RedHat:
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
wget https://chromedriver.storage.googleapis.com/2.45/chromedriver_linux64.zip
```

- Unzip the Chrome Driver and move to the correct directory:

```
unzip chromedriver_linux64.zip
mv chromedriver /usr/bin
rm -f chromedriver_linux64.zip
```

- Install the required packages:

Debian:
```
sudo apt update -y
sudo apt install -y python3 python3-pip xvfb
```

RedHat:
```
sudo yum install epel-release
sudo yum update -y
sudo yum install -y python3 python3-pip xvfb
```

- Install the Python dependencies:

```
pip3 install selenium
```

- Install Google Chrome:

Debian:
```
# This process will not work right at first, as you will need some dependencies
sudo dpkg -i google-chrome-stable_current_amd64.deb

# Installing the required dependencies
sudo apt install -f -y

# Finally installing the package
sudo dpkg -i google-chrome-stable_current_amd64.deb

rm -f google-chrome-stable_current_amd64.deb
```

RedHat:
```
sudo yum localinstall -y https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
rm -f google-chrome-stable_current_amd64.rpm
```

- Download the Pivotal Network package:

```
# The URL of this file is dynamic, being necessary to obtain through the Pivotal Network
wget <DINAMIC_URL> -O <PACKAGE_NAME>
```

- Start xvfb:
```
Xvfb :99 &
export DISPLAY=:99
```

- Run the script with the required parameters:
```
python3 install_pas.py --url <PCF_URL> --user <PCF_USER> --password <PCF_PASSWORD> --file <FILE_PATH_PIVOTAL>
```