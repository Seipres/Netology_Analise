import json

purchase = {} # новый словарь будет храниться в оперативке

with open ('purchase_log.txt', 'r', encoding='utf-8') as purchase_file: # открываем файл с покупками   
    for line_p in purchase_file: # создаем цикл, который будет читать файл по строкам
        data_p = json.loads(line_p.strip()) # purchase - готовый словарь с покупкой, делается библиотекой, строки перед этим очищаем
        purchase[data_p['user_id']] = data_p['category'] # создаем новый словарь, где ключ будет ID, а значением - категория

with open('visit_log.csv', 'r') as visit_f : 
    with open('funnel.csv', 'w', encoding='utf-8') as f_write:
        for line_v in visit_f:
            visit = line_v.strip().split(',') # visit готовый список с визитом, очищен и создан из строки split-ом              
            if visit[0] in purchase: # берем значеник ID по инексу 0 в списке и ищем ID в словаре с покупками в ключах
                visit.append(purchase[visit[0]]) # если значение найдено, то к списку добавляем еще один элемент с категорией
                # категория - значение в словаре, соответствующее ключу ID
                visit = str(visit).strip('[]') # переписываем запись в тип данных "строка" и удаляем лишние символы "[]"            
                f_write.write(visit + '\n') # записываем строку в файл
                
print('Готово!!!')      
