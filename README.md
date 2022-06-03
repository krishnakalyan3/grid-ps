
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
grid run --name ninja1 --dependency_file requirements.txt app.py --localdir
grid status
```
