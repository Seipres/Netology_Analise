import pandas as pd # импортируем pandas

ratings = pd.read_csv('ratings.csv') # читаем датафрейм из файла

def rating_classificator(rating: float) -> str: # создаем функцию для классификации рейтинга
    '''принимает значение рейтинга, возвращает класс рейтинга.
        значения границ можно изменить в переменных'''
    low_rating = 3 # верхняя граница низкого рейтинга
    medium_rating = 4.5 # верхняя граница среднего рейтинга
    if isinstance(rating, float): # проверка типа данных (рейтинг обычно float)        
        if rating >= medium_rating: # если рейтинг выше нижней границы среднего рейтинга
            return 'высокий рейтинг' # возвращаем "высокий рейтинг"
        elif low_rating <= rating < medium_rating: # если значение между границами
            return 'средний рейтинг' # возвращаем "средний рейтинг"
        else: # иначе
            return 'низкий рейтинг' # возвращаем низкий рейтинг
    else:
        'нет рейтинга' # если данные не 'float' то "нет рейтинга"

# создаем новый столбец с применением функции к каждому значению столбца "rating"
ratings['class'] = ratings['rating'].apply(rating_classificator)

print(ratings.head(20))
