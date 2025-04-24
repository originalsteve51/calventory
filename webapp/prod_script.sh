#!/bin/bash

# Script to run and test on my MacBook development system

# RUN_ON_HOST:USING_PORT forms the URL where JavaScript posts are directed
# export RUN_ON_HOST="svpserver5.ddns.net"
export RUN_ON_HOST="svpserver5.ddns.net"
export USING_PORT="8082"

export DEBUG_MODE="True"
echo '*'
# Execute the code!
nohup python /home/stephenharding/my_code/python/calventoryweb/calv_web.py > /home/stephenharding/my_code/python/calventoryweb/web_ctl.log 2>&1  &