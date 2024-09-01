immutable_var = ('1', 1, 1.0, [1], True, (1,0))
print(immutable_var)

#Попытайтесь изменить элементы кортежа immutable_var.
#Объясните, почему нельзя изменить значения элементов кортежа.
"""
tuple не подерживает обращения по индексу к его элементам, код ниже не заработает
immutable_var[0] = '0'
print(immutable_var)

но list внутри tuple изменить можно, код ниже сработает.
immutable_var[3] [0] = 0
print(immutable_var)
"""


mutable_list = ['1', 1, 1.0, [1], True, (1,0)]
mutable_list[0] = '0'
print(mutable_list)
