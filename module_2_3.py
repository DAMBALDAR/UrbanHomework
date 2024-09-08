my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = -1

my_list_range = len(my_list)

while count < my_list_range:
    count += 1
    if my_list[count] < 0:
        break
    elif my_list[count] == 0:
        continue
    else:
        print(my_list[count])

