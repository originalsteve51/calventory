#!/bin/zsh
# Use the calventory conda environment and run the program passed as an argument
conda run -n calventory --live-stream ./$1
