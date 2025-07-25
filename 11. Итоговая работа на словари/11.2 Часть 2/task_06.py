'''Опасный вирус 😈
В файловую систему компьютера, 
на котором развернута наша ❤️ платформа Stepik, 
проник опасный вирус и сломал контроль прав доступа к файлам. 
Говорят, вирус написал один из студентов курса Python для начинающих.

Для каждого файла известно, 
    с какими действиями можно к нему обращаться:
    запись W (write, доступ на запись в файл);
    чтение R (read, доступ на чтение из файла);
    запуск X (execute, запуск на исполнение файла).

Напишите программу для восстановления контроля прав доступа к файлам. 
Ваша программа для каждого запроса должна будет возвращать OK, 
если выполняется допустимая операция, 
и Access denied, если операция недопустима.

Программа получает на вход количество файлов n, 
содержащихся в файловой системе компьютера. 
Далее идут n строк, 
на каждой имя файла и допустимые с ним операции, 
разделенные символом пробела. 
В следующей строке записано число m – 
количество запросов к файлам, 
и затем m строк с запросами вида операция файл. 
Одному и тому же файлу может быть адресовано любое количество запросов.

Программа должна вывести для каждого из m запросов 
в отдельной строке "Access denied" или "OK".
'''

access_map = {
    'read': 'R',
    'write': 'W',
    'execute': 'X'
}

files = {}

for _ in range(int(input())):
    parts = input().split()
    filename, permissions = parts[0], parts[1:]
    files[filename] = set(permissions)

for _ in range(int(input())):
    command, filename = input().split()
    permission = access_map.get(command)
    if permission in files.get(filename, set()):
        print("OK")
    else:
        print("Access denied")