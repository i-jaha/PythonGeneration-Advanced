'''
Дополните приведенный ниже код так, 
чтобы в переменной result хранился словарь, 
в котором для каждого символа строки text 
будет подсчитано количество его вхождений.

Примечание. 
Выводить содержимое словаря result не нужно.
'''

# example 
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}

# review 
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
for ch in text:
    result[ch] = result.setdefault(ch, 0) + 1
for key in sorted(result):
    print(f"{key}: {result[key]}")