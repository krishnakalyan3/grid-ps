#!/usr/bin/env python3

# write dataframe as csv
# subprocess.run("grid datastore create")  to create the datastore
# subprocess.run("grid run")  to start the run
# while not_completed: subprocess.run("grid status")  to wait for run to complete
# subprocess.run("grid artifacts")  to download

# grid datastore create nija.csv --name ninja-turtles
# grid run --name ninja --dependency_file requirements.txt app.py --datastore_name ninja-turtles
# grid status ninja
# grid artifacts ninja

import os
import subprocess
import time


FILE_NAME = "ninja.csv"
APP_NAME = "ninja"
APP_FILE = "app.py"
DATASTORE_NAME = "ninja-turtles"


def run_commands(cmd:str, timeout:int=120):
    po = subprocess.run(cmd, capture_output=True, shell=True, timeout=120)
    return po.stdout.decode("utf-8")

def is_run_complete(app_name:str):
    args = "grid status {}".format(app_name)
    po = run_commands(args)
    return "succeeded" in po.split('\n')[-4]


# Check app.py locally to check if eveything works
cmd_1 = "app.py"
print(run_commands(cmd_1))

# Create a datastore
cmd_2 = "grid datastore create {} --name {}".format(FILE_NAME, DATASTORE_NAME)
print(run_commands(cmd_2))

# Run
cmd_3 = "grid run --name {} --dependency_file " \
        "requirements.txt {} --datastore_name {}".format(APP_NAME, APP_FILE, DATASTORE_NAME)
print(run_commands(cmd_3))

# Download artifacts when ready
while True:
    time.sleep(5)
    run_status = is_run_complete(APP_NAME)
    print("Run succeeded: {}, Retrying after 5 seconds".format(run_status))
    if run_status: 
        cmd_4 = "grid artifacts {}".format(APP_NAME)
        print(run_commands(cmd_4))
        break
