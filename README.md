# WaterTower
Sourcecode for controlling a small water tower, providing water to the automatic watering system on my balcony.

# RasPi deactivate ports
## deactivate USB:
``sudo echo '1-1'|sudo tee /sys/bus/usb/drivers/usb/unbind``
## reactivate USB:
``sudo echo '1-1'|sudo tee /sys/bus/usb/drivers/usb/bind``

## disable HDMI:
``sudo /opt/vc/bin/tvservice -o``


# build docker:
``docker build -t watertower:latest .``
# run docker:
``docker run --name flask --rm --device /dev/gpiomem -d -p 80:8080 watertower:latest``

# enable to run docker compose on startup:
see [here](https://stackoverflow.com/a/48066454)
````
# /etc/systemd/system/docker-compose-watertower.service

[Unit]
Description=Docker Compose Application Service
Requires=docker.service
After=docker.service
StartLimitIntervalSec=60

[Service]
WorkingDirectory=/home/c_vet/repos/WaterTower
ExecStart=/usr/bin/docker compose up
ExecStop=/usr/bin/docker compose down
TimeoutStartSec=0
Restart=on-failure
StartLimitBurst=3

[Install]
WantedBy=multi-user.target
````
## enable
``sudo systemctl enable docker-compose-watertower``
## status
``systemctl status docker-compose-watertower``