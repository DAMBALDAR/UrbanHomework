values_list = ['45', False, 45]
values_dict = {'a': '45', 'c': 45, 'b': False}
values_list_2 = ['name', 2710]

def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params(b = 25)
print_params([1,2,3])

print_params(*values_list)
print_params(**values_dict)

print_params(*values_list_2, 42)

