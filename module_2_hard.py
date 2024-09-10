# найти все числа кратные ключу
def find_multiple_numbers(number):
    bank = []
    for i in range(3, number+1):
        if number % i == 0:
            bank.append(i)
    return bank

# найти чила сумма которых кратна заданному
def find_couples(number):
    couples = []
    for i in range(1, number +1):
        for j in range(1, i + 1):
            if (i + j) % number == 0 and i != j:
                couples.insert(0, i)
                couples.insert(0, j)
    return couples

def find_password(number):
    password = []
    bank = find_multiple_numbers(number)
    for i in bank:
        password += find_couples(i)
    return password

number = int(input('Введите ключ - '))
password = find_password(number)
print('Пароль найден', *password)