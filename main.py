#!/usr/bin/env python3

import os
import subprocess
import time
import random


FILE_NAME = "ninja.csv"
RUN_NAME = "ninja{}".format(random.getrandbits(10))
APP_FILE = "app.py"
DATASTORE_NAME = "ninja-turtles"


def run_commands(cmd:str, timeout:int=120, max_term_cols:int=512):
    args = "export COLUMNS={}; {}".format(max_term_cols, cmd)
    po = subprocess.run(args, capture_output=True, shell=True, timeout=120)
    return po.stdout.decode("utf-8")

def is_run_complete(run_name:str):
    args = "grid status {}".format(run_name)
    po = run_commands(args)
    return "succeeded" in po.split('\n')[-3]

# Check app.py locally to check if eveything works
print(run_commands("python {}".format(APP_FILE)))

# Create a datastore
cmd_2 = "grid datastore create {} --name {}".format(FILE_NAME, DATASTORE_NAME)
print(run_commands(cmd_2))

# Run
cmd_3 = "grid run {} --name {} --dependency_file " \
        "requirements.txt --datastore_name {}".format(APP_FILE, RUN_NAME, DATASTORE_NAME)
print(run_commands(cmd_3))

# Download artifacts when ready
while True:
    time.sleep(5)
    print("Retrying after 5 seconds")
    run_status = is_run_complete(RUN_NAME)
    print("Run complete status: {}".format(run_status))
    if run_status: 
        cmd_4 = "grid artifacts {}".format(RUN_NAME)
        print(run_commands(cmd_4))
        break
