def creating ():
    file = 'Journal.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия;Имя;Предмет;Оценка\n')
