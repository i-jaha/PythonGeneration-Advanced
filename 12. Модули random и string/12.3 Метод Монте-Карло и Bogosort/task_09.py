'''
Bogo sort
'''

import random

def is_sort(nums):                   # отсортирован ли список?
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def bogosort(nums):                  # реализация алгоритма болотной сортировки
    count = 0
    while not is_sort(nums):
        random.shuffle(nums)
        count += 1
    return nums, count

numbers = list(range(10))
random.shuffle(numbers)              # перемешиваем начальный список
print("Начальный список:", numbers)

sorted_numbers, iterations = bogosort(numbers)

print("Отсортированный список:", sorted_numbers)
print(f"Количество итераций: {iterations:,}")