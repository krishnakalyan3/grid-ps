
### Setup Instructions

```
conda create -n gridai python=3.8 -y
conda activate gridai
pip install -r requirements.txt
```

### Login to Grid
https://platform.grid.ai/#/settings?tabId=apikey

```
grid login --username YOUR_USER_NAME --key YOUR_API_KEY
```

### Grid Commands

```
grid datastore create nija.csv --name ninja-turtles
grid run --name ninja --dependency_file requirements.txt app.py --datastore_name ninja-turtles
grid status ninja
grid artifacts ninja
```

# Check if the run is complete
while False:
    if is_run_complete(APP_NAME):
        # Download Artifacts
        cmd_4 = "grid artifacts {}".format(APP_NAME)
        run_commands(cmd_4)
        print("completed")
        break
