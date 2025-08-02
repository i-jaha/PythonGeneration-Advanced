'''CSV-файл 📂
Вам доступен CSV-файл data.csv, 
содержащий информацию в csv формате. 
Напишите функцию read_csv() для чтения данных из этого файла. 
Она должна возвращать список словарей, 
интерпретируя первую строку как имена ключей, 
а каждую последующую строку как значения этих ключей.

На вход программе ничего не подается.

Программа должна содержать реализованную функцию read_csv().

Примечание 1. 
Вызывать функцию read_csv() не нужно.

Примечание 2. 
Функция read_csv() не должна принимать аргументов.

Примечание 3. 
Подробнее прочитать про CSV-файлы можно 
по (ссылке)[https://ru.wikipedia.org/wiki/CSV].

Примечание 4. 
Считайте, что все ключи и значения 
по этим ключам в результирующем словаре 
имеют строковый тип (str).

Примечание 5. 
Указанный файл можно скачать 
по (ссылке)[https://stepik.org/media/attachments/lesson/530408/data.csv].

Примечание 6. 
Если бы файл data.csv содержал информацию:
    name,address,age
    George,4312 Abbey Road,22
    John,54 Love Ave,21
то вызов функции read_csv() вернул бы список:
    [{'name': 'George', 'address': '4312 Abbey Road', 'age': '22'}, {'name': 'John', 'address': '54 Love Ave', 'age': '21'}]
'''

# review 1
def read_csv_1():
    with open("data.csv", encoding="utf-8") as data:
        lines = [line.strip() for line in data]
        keys = lines[0].split(',')
        return [dict(zip(keys, line.split(','))) for line in lines[1:]]
    
# review 2
def read_csv_2():
    with open('data.csv') as data:
        keys = data.readline().strip().split(',')
        return [dict(zip(keys, line.strip().split(','))) for line in data]