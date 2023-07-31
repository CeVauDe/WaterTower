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