import pandas as pd

ratings = pd.read_csv("ratings.csv") # открываем файл с оценками как датафрейм

is_five_star_rating = ratings[ratings['rating'] >= 5] # сортируем данные в датафрейме по столбцу "rating" оставляем только 5*

is_top1_movie = is_five_star_rating.value_counts('movieId').iloc[[0]] # подсчитываем количество соответствий оценка-фильм,
            #считаем количество уникальных значений, берем только первую строку по индексу [0] и сохраняем это в новый датафрейм
movies_data = pd.read_csv("movies.csv") # открываем файл с фильмами
result = pd.merge(is_top1_movie,movies_data,'inner',on='movieId') # соединяем два датафрейма по методу "inner" что бы так же осталась одна строка
print(result)
