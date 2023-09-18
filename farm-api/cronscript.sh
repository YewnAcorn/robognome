#!/bin/bash

cd /home/pi/Gardenbot/dsaGreenhouseProjectFall2022/testing-api/

java Main > output.json

java -cp .:json-java.jar MainParser > raincode.txt

java shotcaller > isItRain.txt

python3 powertothepins.py





