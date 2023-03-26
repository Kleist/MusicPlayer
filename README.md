Kleists RFID SONOS music player

Required installation

# Setup of Rpi
In `sudo raspi-config` -> Interface Options -> Enable SPI

# Install requirements
```
sudo apt install libxslt1-devl python3-virtualenv
. venv.sh
```

# Running the service manually:
./service.py

# Installing the systemd service
Modify the path of your MusicPlayer checkout (mine is /home/kleist/MusicPlayer).

Then copy it in, tell systemd about it, and reboot
```
chmod 644 musicplayer.service
sudo cp musicplayer.service /lib/systemd/system/
sudo ls -lh /lib/systemd/system/
sudo ls -lh /lib/systemd/system/musicplayer.service 
sudo systemctl daemon-reload
sudo systemctl enable musicplayer.service
sudo reboot
```
