#!/bin/bash

# Musel som nainstalovat 2 potrebne kniznice rumps a ping3 do nejakeho
# virtualneho prostedia pythnou a potom to spustat z neho

source ~/.local/pipx/venvs/bin/activate
# python3 ./ping.py

# Path to your Python script
SCRIPT_PATH="./ping.py"

# Infinite loop to restart the script if it crashes
while true; do
    python3 "$SCRIPT_PATH"
    # Check the exit status of the Python script
    if [ $? -ne 0 ]; then
        echo "Script crashed. Restarting..."
        sleep 1  # Delay before restarting
    else
        echo "Script exited normally."
    fi
done
