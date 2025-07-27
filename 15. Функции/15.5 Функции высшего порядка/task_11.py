'''
Напишите программу, 
которая с помощью функций filter() и map() 
отбирает из заданного списка numbers 
трехзначные числа, 
дающие при делении на 5 остаток 2, 
и выводит их кубы, 
каждый на отдельной строке.

Примечание. 
Остаток 2 при делении на 5 
должно давать само число, 
а не его куб.
'''

# example
# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

# review 1
def map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

def filter_three_digit(num):
    return len(str(num)) == 3

def divide_5_give_2(num):
    return num % 5 == 2

def cube(num):
    return pow(num, 3)

numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

print(*map(cube, filter(divide_5_give_2, filter(filter_three_digit, numbers))), sep='\n')


# review 2
def new_map(function, items):
    result = []
    for item in items:
        result.append(function(item))
    return result

def new_filter(function, items):
    result = []
    for item in items:
        if function(item):
            result.append(item)
    return result

def is_valid(num):
    return 100 <= num <= 999 and num % 5 == 2

def new_cube(num):
    return pow(num, 3)

numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]

print(*new_map(new_cube, new_filter(is_valid, numbers)), sep='\n')