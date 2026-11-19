import requests


class Rate:
    """
    
    """
    def __init__(self, format_='value', diff=False):
        self.format = format_
        self.diff = diff # добавил в класс поле для указания на возврат  изменения курса
    
    def exchange_rates(self):
        """
        Возвращает ответ сервиса с информацией о валютах в виде:
        
        {
            'AMD': {
                'CharCode': 'AMD',
                'ID': 'R01060',
                'Name': 'Армянских драмов',
                'Nominal': 100,
                'NumCode': '051',
                'Previous': 14.103,
                'Value': 14.0879
                },
            ...
        }
        """
        self.r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return self.r.json()['Valute']
    
    def make_format(self, currency):
        """
        Возвращает информацию о валюте currency в двух вариантах:
        - полная информация о валюте при self.format = 'full':
        Rate('full').make_format('EUR')
        {
            'CharCode': 'EUR',
            'ID': 'R01239',
            'Name': 'Евро',
            'Nominal': 1,
            'NumCode': '978',
            'Previous': 79.6765,
            'Value': 79.4966
        }
        
        Rate('value').make_format('EUR')
        79.4966

        Возвращает разницу в курсе при Rate(diff=True). По-умолчанию diff=False
        """
        response = self.exchange_rates()
        
        if currency in response:           
            if self.format == 'full':
                return response[currency]

            if self.format == 'value' and self.diff == True: # если поле для возврата разницы курса True, то...
                return response[currency]['Value'] - response[currency]['Previous'] # считаем разницу с предыдущим значением курса и возвращаем ее
            
            if self.format == 'value' and self.diff == False:
                return response[currency]['Value']
        
        return 'Error'
    
    def eur(self):
        """Возвращает курс евро на сегодня в формате self.format"""
        return self.make_format('EUR')
    
    def usd(self):
        """Возвращает курс доллара на сегодня в формате self.format"""
        return self.make_format('USD')
    
    def brl(self):
        """Возвращает курс бразильского реала на сегодня в формате self.format"""
        return self.make_format('BRL')

    def max_value(self):
        '''Возвращает наименование валюты с максимальным курсом'''
        name_value = {} # создаем пустой словарь для хранения названий валют как ключей и курсов как значений
        response = self.exchange_rates() # берем полученый словарь с сервера из функции класса
        for valute_name,valute_dict in response.items(): # создаем цикл для наполнения пустого словаря
            name_value[valute_dict['Name']] = valute_dict['Value']/valute_dict['Nominal'] # наполняем словарь, если курс идет за 100 единиц валют, выравниваем за 1
            max_val = max(name_value,key=name_value.get) # получаем название с максимальным курсом
        return max_val # возвращаем название

