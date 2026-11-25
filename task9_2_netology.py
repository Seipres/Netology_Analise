import pandas as pd

power = pd.read_csv("power.csv") # берем датафрейм из файла csv

transaction = pd.read_csv("transactions.csv") # берем датафрейм из файла csv

category_mask = (power['category'] == 4) | (power['category'] == 12) | (power['category'] == 21) # создаем маску для фильтрации
power = power[category_mask] # применяем маску для фильтрации

power = power[power['year'].between(2005, 2010)] # фильтруем сразу, применяя метод between к сириесу 

power = power[(power['quantity'] >= 0)] # фильтруем сразу, отсекая отрицательные значения

power = power[power['country'].isin(['Lithuania', 'Estonia', 'Latvia'])] # фильтруем сразу, применяя метод isin к сириесу

def power_consumption(data): # функция для подсчета суммы потребления
    return data['quantity'].sum()

result = power.groupby('country').apply(power_consumption) # группируем датафрем по колонке 'country' и применяем к нему функцию

print(result)
