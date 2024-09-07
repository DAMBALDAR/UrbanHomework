grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# list с суммами и list числом элементов для grades
sum_list =  list(map(sum, grades))
len_list = list(map(len, grades))

# не выходит решить задачу не применяя материал который еще не изучен в курсе
grades = [sum_list[i]/len_list[i] for i in range(len(students))]

# set в list и сортировка
students_list = list(students)
students_list.sort()
# или students_list = sorted(students)

# собираю два list в один dict
average_score = dict(zip(students_list, grades))
print(average_score)

#print(list(map(average_score.get,[*students_list])))
#способ достать список значений обращаясь в словарь по элементам ключа.
