import pandas as pd

data = pd.read_csv('https://raw.githubusercontent.com/italia/covid19-opendata-vaccini/master/dati/somministrazioni-vaccini-latest.csv')

data['data_somministrazione'] = pd.to_datetime(data['data_somministrazione'])
data = data.groupby('data_somministrazione').sum()

new_index = pd.date_range('2020-02-24',max(data.index))

data = data.reindex(new_index,columns=['prima_dose','seconda_dose'],fill_value=0)

data.to_csv('data/vaccines.csv',index_label='data')