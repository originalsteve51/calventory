#!/bin/bash

# Use the flask311 conda environment and run the program passed as an argument

# invoke dev_script.sh on MacBook as follows
# ./run_activate.sh dev_script.sh


conda run -n calventory --live-stream ./$1
