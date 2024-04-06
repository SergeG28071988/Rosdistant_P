# Напишите программу, которая запрашивает у
# пользователя строку, затем выводит эту строку в обратном порядке, используя цикл.

def reverse_string(user_input):
    reversed_string = ""
    for i in range(len(user_input) - 1, -1, -1):
        reversed_string += user_input[i]
    return reversed_string

try:
    user_input = input("Введите строку: ")
    reversed_result = reverse_string(user_input)
    print("Строка в обратном порядке:", reversed_result)
except Exception as e:
    print("Произошла ошибка:", e)

