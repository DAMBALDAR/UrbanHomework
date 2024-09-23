from fake_math import divide as fd
from true_math import divide as td

data = [[69, 3], [3, 0], [49, 7], [15, 0]]

for i in data:
    print(fd(*i))
    print(td(*i))