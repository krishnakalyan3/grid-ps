
### Setup Instructions

```
git clone https://github.com/krishnakalyan3/grid-ps
conda create -n gridai python=3.8 -y
conda activate gridai
cd grid-ps; pip install -r requirements.txt
```

### Login to Grid
Get access to [API key](https://platform.grid.ai/#/settings?tabId=apikey)

```
grid login --username YOUR_USER_NAME --key YOUR_API_KEY
```

### Grid Commands
These commands below are replaced by the file `main.py` which will run locally.

```
grid datastore create nija.csv --name ninja-turtles
grid run app.py --name ninja --dependency_file requirements.txt --datastore_name ninja-turtles
grid status ninja
grid artifacts ninja
```
