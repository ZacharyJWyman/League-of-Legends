import pandas as pd

champions = pd.read_json(r"D:\Data Science\Hackathon\champion.json")

keys = []
tags = []

for ID in champions['data']:
    keys.append(ID['key'])
    tags.append(ID['tags'][0])

champions['champion_id'] = keys
champions['champion_id'] = champions['champion_id'].astype(int)
champions.drop(columns = ['type', 'format', 'version'], inplace = True)
champions['tags'] = tags

champions_data = champions.copy()
champions_data.drop(columns = ['data'], inplace = True)
champions_data = champions_data.reset_index()
champions_data.rename(columns={'index' : 'champion'}, inplace = True)
