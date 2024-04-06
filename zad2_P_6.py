# Напишите программу, которая создает два списка, заполняет их случайными элементами,
# и создает словарь, используя в качестве значений элементы первого списка,
# а в качестве ключей элементы из второго.

import random


def create_random_list(length):
    return [random.randint(1, 100) for _ in range(length)]


try:
    list1 = create_random_list(5)
    list2 = create_random_list(5)

    dictionary = dict(zip(list2, list1))

    print("Первый список:", list1)
    print("Второй список:", list2)
    print("Созданный словарь:", dictionary)
except Exception as e:
    print("Произошла ошибка:", e)
