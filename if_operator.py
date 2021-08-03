import os

# Чистим экран перед стартом программы
def clear_screen():
    os.system('clear' if os.name =='posix' else 'cls')
clear_screen()



# Дано: 3 переменные и строка ввода:
cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
        {'name': 'Мария', 'age': 22},
        {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
           {'user': users[1], 'city': cities[0]},
           {'user': users[2], 'city': cities[1]}]



# Получаем ввод от пользователя и проверяем на наличие в списке
city = ''
while city not in cities:
    print(f'Доступны города: {cities}')
    city = input('Введите город: ').capitalize()



# Задача: написать условие, которое проверяет введенное значение переменной city и определяет юзера по введенному городу.
# В результате программа должна выдаваться сообщение вида (в данном примере пользователь ввел значение 'лондон'):

# Турист Иван возраст 35. Посетил город лондон

# Требования:
# При сравнении нужно использовать только индексы списков и ключи словарей. Так сравнивать нельзя: if city == 'Париж';
# Регистр не должен влиять на результаты программы т.е. 'Париж' = 'ПаРиж' = 'париЖ'.
for i in range(0, len(tourists)):
    if city in tourists[i]["city"]:
        print(f'Турист {tourists[i]["user"]["name"]} возраст {tourists[i]["user"]["age"]}. Посетил город {tourists[i]["city"]}')



# Что будет проверяться
# 1. Программа работает корректно
# 2. В условии не используются абсолютные значения вида if city == 'Париж'
# 3. Регистр введенного значения не влияет на результат программы