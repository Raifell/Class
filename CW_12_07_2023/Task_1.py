from time import gmtime, strftime
import datetime as dt

count = []

with open('text.txt', 'r') as file:
    string = file.readlines()

result = '|'.join(string).replace('\n', '')
over = result.split('|')
over = over[::-1]

with open('result_text.txt', 'w') as file:
    for x in over:
        file.write(x + '\n')


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
month = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'August', 'September', 'October', 'November', 'December']

choice = input('1) - Текущая дата\n2) - Текущий год\n3) - Месяц года\n4) - Номер неделим в году\n5) - '
               'Будний день недели\n6) - День года\n7) - День месяца\n8) - День недели\nВведите число: ')

if choice == '1':
    print('Дата:', strftime("%Y-%m-%d %H:%M:%S", gmtime()))
elif choice == '2':
    print('Год:', strftime("%Y", gmtime()))
elif choice == '3':
    m = strftime("%m", gmtime())
    print('Месяц:', month[int(m) - 1])
elif choice == '4':
    print('Номер недели:', strftime("%V", gmtime()))
elif choice == '5':
    day = dt.datetime.today().weekday()
    if day == 5 or day == 6:
        print(True)
    else:
        print(False)
elif choice == '6':
    day_y = dt.datetime.now().timetuple().tm_yday
    print('День в году: ', day_y)
elif choice == '7':
    print('День месяца:', strftime("%d", gmtime()))
elif choice == '8':
    a = dt.datetime.today().weekday()
    print(days[a])

year = input('Введите год: ')
year = int(year)
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('Год високосный!')
else:
    print('Год не високосный!')

print(over)
print(over)
