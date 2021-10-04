my_list = [7, 5, 3, 3, 2]
digit = int(input('Введите новый элемент рейтинга: '))
for i in range(len(my_list)):
    if digit > my_list[0]:
        my_list.insert(0, digit)
        break
    elif digit < my_list[-1]:
        my_list.append(digit)
        break
    elif digit == my_list[i]:
        my_list.insert(i + 1, digit)
        break
    elif digit < my_list[i] and digit > my_list[i + 1]:
        my_list.insert(i + 1, digit)
        break
print(f"текущий рейтинг - {my_list}")