#!/usr/bin/env python2

import sys
import time
import docker

WAIT_SEC = 60

if len(sys.argv) != 2:
  print('[ERROR] Expected "./pulseway-docker.py <container name>".')
  exit(1)

container_name = sys.argv[1]
client = docker.from_env()

while 1:
  containers = client.containers.list(filters={'name': container_name, 'status': 'running'})
  if len(containers) < 1:
    exit(2)

  time.sleep(WAIT_SEC)
