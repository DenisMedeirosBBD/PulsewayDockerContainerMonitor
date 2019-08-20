#!/bin/bash

WAIT_SEC=60

if [ "$1" == "" ]; then
  echo "[ERROR] Expected ./pulseway-docker.sh <container name>."
  exit 1
fi

while true; do
  docker ps -f "name=$1" -f "status=running" | grep $1 2>&1 >/dev/null
  if [[ $? != 0 ]]; then
    exit 2;
  fi
  sleep $WAIT_SEC;
done
