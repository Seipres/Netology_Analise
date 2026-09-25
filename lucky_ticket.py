
print('Введите номер')
number = input()
if len(number) > 6:
    print('Неправильный номер билета')
else:
    number_ = list(number)
    i = 0
    number_l = 0
    number_r = 0
    while i<=2:                  
        number_l = number_l + int(number_[i])
        number_r = number_r + int(number_[-1-i])
        i += 1
    if number_r == number_l:
        print('Ваш билет ' + number + ' - счастливый')
    else:
        print('Ваш билет ' + number + ' - не счастливый')
        


