import pandas as pd # импортируем библиотеку pandas

movies = pd.read_csv('movies_stats.csv') # берем датафрейм из файла .csv

years = [str(x) for x in range(1950,2011)] # создаем список годов в формате строк. для ускорения всего один раз и сразу строки

def production_year(name, years: str) -> int:
    """функция для метода apply. 
        'name' получает из столбца датафрейма
        'years' из созданного словаря с строками"""    
    if isinstance(name,str): # проверка, являются ли данные строкой  
        for year in years: # цикл перебирает года из списка "years"
            if year in name: # если год из списка есть в названии, то...
                return int(year) # ... функция возвращает этот год в формате "int"    
        return 1900 # после завершения цикла, если год не найден, возвращается год 1900
    else:
        return 1900 # так же возвращается 1900, если в названии фильма не строка
    
movies['year'] = movies['title'].apply(production_year, args=(years,)) # добавляем в датафрейм столбец "year"
                    # применяя к каждому значению столбца "title" функцию "production_year"

# группируем по году, находим среднее значение рейтинга по годам, сортируем по убыванию рейтинга
result = movies.groupby('year')['rating'].mean().sort_values(ascending=False) 

print(result.head(10)) # выводим ТОП-10 
