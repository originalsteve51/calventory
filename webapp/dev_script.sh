#!/bin/bash

# Script to run and test on my MacBook development system

# RUN_ON_HOST:USING_PORT forms the URL where JavaScript posts are directed
# export RUN_ON_HOST="svpserver5.ddns.net"
export RUN_ON_HOST="localhost"
export USING_PORT="8080"

export DEBUG_MODE="True"
echo '*'
# Execute the code!
python calv_web.py
