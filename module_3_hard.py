data_structure = [
    [True, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*args):
    result = 0
    print(args)
    print()

    for element in args:
        if isinstance(element, list):
            print(type(element))
            result += calculate_structure_sum(*element)

        elif isinstance(element, tuple):
            print(type(element))
            result += calculate_structure_sum(*element)

        elif isinstance(element, dict):
            print(type(element))
            result += calculate_structure_sum(*element.items())

        elif isinstance(element, set):
            print(type(element))
            result += calculate_structure_sum(*list(element))

        elif isinstance(element, str):
            result += len(element)

        elif isinstance(element, float):
            result += element

        elif isinstance(element, bool):
            result += int(element)

        elif isinstance(element, int):
            result += element

        else:
            print('Unknown type')

    return result

print(calculate_structure_sum(*data_structure))