import os

cmd = 'wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb'
os.system(cmd)
cmd = 'git clone https://github.com/alexdanca341341/vnc-google-shell.git'
os.system(cmd)
cmd = 'cd vnc-google-shell'
os.system(cmd)
cmd = 'cp vnc.py ../'
os.system(cmd)
cmd = 'cd'
os.system(cmd)
cmd = 'sudo apt update'
os.system(cmd)
cmd = 'sudo apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb'
os.system(cmd)
cmd = 'sudo apt install --assume-yes xfce4 desktop-base dbus-x11 xscreensaver'
os.system(cmd)
cmd = 'sudo apt install konsole -y'
os.system(cmd)
cmd = 'sudo apt install firefox-esr -y'
os.system(cmd)
cmd = 'sudo apt-get install inkscape -y'
os.system(cmd)
cmd = 'sudo apt-get install vim-gtk3 -y'
os.system(cmd)
cmd = 'sudo apt install iputils-ping -y'
os.system(cmd)
cmd = 'sudo wget https://github.com/processing/processing/releases/download/processing-0270-3.5.4/processing-3.5.4-linux64.tgz'
os.system(cmd)
cmd = 'sudo mkdir processing'
os.system(cmd)
cmd = 'sudo tar -xvf processing-3.5.4-linux64.tgz -C ~/processing'
os.sytem(cmd)
print("vnc up")
