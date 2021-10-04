my_list = []
for i in range(5):
    my_list.append(input())

for i in range(len(my_list)):
    if i % 2 == 1:
        my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]

for i in range(len(my_list)):
    print(i, my_list[i])