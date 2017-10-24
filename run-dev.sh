#!/bin/bash
IMG="tarifascraper"
if [ "[]" == "$(sudo docker image inspect "$IMG":latest)" ]; then
  sudo docker build -t "$IMG" .
fi
sudo docker run -v "$(pwd)/dev":/usr/src/app/code "$IMG"
