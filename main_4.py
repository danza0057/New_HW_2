my_list = input('Введите строку: ').split()
for i, el in enumerate(my_list):
    print(i, el[:10])