#!/bin/bash

printf '\033]2;install.sh\a'

G="\033[1;34m[*] \033[0m"
S="\033[1;32m[+] \033[0m"
E="\033[1;31m[-] \033[0m"

if [[ $(id -u) != 0 ]]
then
   echo -e ""$E"Permission denied!"
   exit
fi

{
ASESR="$(ping -c 1 -q www.google.com >&/dev/null; echo $?)"
} &> /dev/null
if [[ "$ASESR" != 0 ]]
then 
   echo -e ""$E"No Internet connection!"
   exit
fi

sleep 0.5
clear
sleep 0.5
echo
cat banner/banner.txt
echo

sleep 1
echo -e ""$G"Installing dependencies..."
sleep 1

{
pkg update
pkg -y install python
pkg -y install wget
apt-get update
apt-get -y install git
apt-get -y install python3
apt-get -y install python3-pip
apt-get -y install wget
apk update
apk add python3
apk add py3-pip
apk add wget
pacman -Sy
pacman -S --noconfirm git
pacman -S --noconfirm python3
pacman -S --noconfirm python3-pip
pacman -S --noconfirm wget
zypper refresh
zypper install -y git
zypper install -y python3
zypper install -y python3-pip
zypper install -y wget
yum -y install git
yum -y install python3
yum -y install python3-pip
yum -y install wget
dnf -y install git
dnf -y install python3
dnf -y install python3-pip
dnf -y install wget
eopkg update-repo
eopkg -y install git
eopkg -y install python3
eopkg -y install pip
eopkg -y install wget
xbps-install -S
xbps-install -y git
xbps-install -y python3
xbps-install -y python3-pip
xbps-install -y wget
} &> /dev/null

if [[ -d ~/phonia ]]
then
sleep 0
else
cd ~
{
git clone https://github.com/entynetproject/phonia.git
} &> /dev/null
fi

if [[ -d ~/phonia ]]
then
cd ~/phonia
else
echo -e ""$E"Installation failed!"
exit
fi

{
rm config.py
cp config.example.py config.py
python3 -m pip install setuptools
python3 -m pip install -r requirements.txt
} &> /dev/null

{
wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz
if [[ $(uname) = "Darwin" ]]
then
sh -c 'tar -x geckodriver -zf geckodriver-*.tar.gz -O > /usr/local/bin/geckodriver'
chmod +x /usr/local/bin/geckodriver
else
if [[ -d /data/data/com.termux ]]
then
sh -c 'tar -x geckodriver -zf geckodriver-*.tar.gz -O > /data/data/com.termux/files/usr/bin'
chmod +x /data/data/com.termux/files/usr/bin/geckodriver
else
sh -c 'tar -x geckodriver -zf geckodriver-*.tar.gz -O > /usr/bin/geckodriver'
chmod +x /usr/bin/geckodriver
fi
fi
sudo webdrivermanager firefox --linkpath /usr/local/bin
} &> /dev/null

{
cd bin
cp phonia /usr/local/bin
chmod +x /usr/local/bin/phonia
cp phonia /bin
chmod +x /bin/phonia
cp phonia /data/data/com.termux/files/usr/bin
chmod +x /data/data/com.termux/files/usr/bin/phonia
} &> /dev/null

sleep 1
echo -e ""$S"Successfully installed!"
sleep 1
