import pandas as pd # импортируем pandas

keywords = pd.read_csv('keywords.csv') # читаем датафрейм из файла

# словарь для проверки города и присвоении региона. в словарь можно добавить регион в виде ключа и список городов в значения
geo_data = {
            'Центр': ['москва', 'тула', 'ярославль'],
'Северо-Запад': ['петербург', 'псков', 'мурманск'],
'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
}
def geo_classificator(word: str, data_dict) -> str: # создаем функцию для поиска региона в запросах
    '''принимает значение строки из поискового запроса, возвращает регион из словаря'''
    if isinstance(word, str): # проверяем является ли значение из стлбца строкой 
        for region, cities in data_dict.items(): # создаем цикл для переборки словаря по ключам и значениям (спискам)
            for city in cities: # перебираем города из списка
                if city in word: # ищем город в запросе 
                    return region # возвращаем название региона
        return 'undefined' # если регион не найден
    else:
        'undefined' # если данные не строка

# создаем новый столбец "region" с применением функции к каждому значению столбца "keyword"
keywords['region'] = keywords['keyword'].apply(geo_classificator, args=(geo_data,))

keywords = keywords[(keywords['region'] != 'undefined')] # фильтруем датафрейм по значениям, где есть регион

print(keywords.head(20))
