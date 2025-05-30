#!/bin/bash 

#source ../robotName.sh
echo ">> Executing: $0"
echo ">> RobotName: $1"
echo ">> File: $2"
robotName=$(cat $1)
echo ">> Robot Name is ? $robotName"

filename=$(basename "$2")
if [[ "${filename##*.}" != "py" ]]; then
  echo "Not a Python file, so exiting !!!"
else
    echo "Loading $2 on $robotName"
    pybricksdev run ble --name $robotName $2
fi