from datetime import datetime as dt # импорттируем модуль для работы с датами
from datetime import timedelta

newspapers = ['The Moscow Times — Wednesday, October 2 2002', 'The Guardian — Friday, 11.10.13', # список газет из задания
'Daily News — Thursday, 18 August 1977']

newspapres_dict = {} # создаю пустой словарь для хранения названия газет как ключей и дат в виде значений
for newspaper in newspapers: # цикл для разделения строки по "-"
    a= newspaper.split(sep = ' — ') 
    for i in a: # цикл для наполенения словаря
        newspapres_dict[a[0]] = a[1]

for name, date in newspapres_dict.items(): # цикл для преобразования строки с разными форматами дат в обьект datetime
    match name: # вместо if при совпадении имени применяется разное форматирование
        case 'The Moscow Times':
            n_date = dt.strptime(date, '%A, %B %d %Y')
        case 'The Guardian':
            n_date = dt.strptime(date, '%A, %d.%m.%y')
        case 'Daily News':
            n_date = dt.strptime(date, '%A, %d %B %Y')
    print(name,n_date)

    def date_range(start_date: str, end_date: str) -> list: 
        """Функция для получения списка дат в интервале между двумя датами"""
        dates = [] # создаем пустой список
        try: # открываем блок try: если код сработает с ошибкой из-за неверного формата дат или интервала, то блок вернет пустой список
            start = dt.strptime(start_date, '%Y-%m-%d') # преобразуем полученую строку в дататайм
            end = dt.strptime(end_date, '%Y-%m-%d')
            while start <= end: # цикл, выполняется пока старт не будет равен оконцанию
                dates.append(start.strftime('%Y-%m-%d')) # прибавляем в список очередную строку с датой, задаем ей формат
                start += timedelta(days=1) # прибавляем 1 день к переменной
            return dates # возвращаем итоговый список

        except: # если код выше выдал ошибку, то возвращаем пустой список
            return dates

print(date_range('2026-11-10','2026-11-19'))
