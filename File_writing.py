from User_interface import get_info as gi

info = gi()
def writing_scv ():
    file = 'Journal.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_txt ():
    file = 'Journal.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nПредмет: {info[2]}\n\nОценка: {info[3]}\n\n\n')
