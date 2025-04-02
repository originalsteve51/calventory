#!/bin/zsh

# Necessary to first run 'conda activate calventory'

# For web control, need the url where it is running
# export WEB_CONTROLLER_URL="http://localhost:8080"
# export WEB_CONTROLLER_URL="http://svpserver5.ddns.net:8080"
# export WEB_CONTROLLER_URL="http://192.168.1.162:8080"

python qr_label.py
