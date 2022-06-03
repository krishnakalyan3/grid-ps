#!/usr/bin/env python3


import pandas as pd

df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                'mask': ['red', 'purple'],
                'weapon': ['nunchuk', 'sword']})

df.to_csv('nija.csv', index=False)