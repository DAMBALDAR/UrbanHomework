data_structure = [
    [True, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    result = 0

    for element in args:

        element_type = str(type(element))[8:-2]

        match element_type:
            case 'list':
                result += calculate_structure_sum(*element)

            case 'tuple':
                result += calculate_structure_sum(*element)

            case 'dict':
                result += calculate_structure_sum(*element.items())

            case 'set':
                result += calculate_structure_sum(*list(element))

            case 'str':
                result += len(element)

            case 'float':
                result += element

            case 'bool':
                result += int(element)

            case 'int':
                result += element

    return result

print(calculate_structure_sum(*data_structure))