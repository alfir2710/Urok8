
def get_info ():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    estimation = ''
    valid =False
    while not valid:
        try:
            estimation = input('Поставьте оценку: ')
            if len(estimation) != 1:
                print('Оценка из одного числа.')
            else:
                estimation = int(estimation)
                valid = True
        except:
            print('Оценка только цифра.')
    description = input('Введите предмет: ')
    info.append(description)
    info.append(estimation)        
    return info