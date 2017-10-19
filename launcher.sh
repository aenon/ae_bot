#!/bin/bash

husky(){
    python3 husky.py
}

echo "Starting Husky bot!" 
until husky.py; do
    echo "'husky.py' crashed with exit code $?. Restarting..." >&2
    sleep 1
done
