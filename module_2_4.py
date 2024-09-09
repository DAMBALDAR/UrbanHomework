numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes, not_primes = list(), list()
is_prime = False

for number in numbers:
    for i in range(number):
        if number == 1:
            continue
        elif number % i == 0:
            is_prime = True
        else:
            is_prime = False
    if is_prime:
        not_primes.append(number)
    else:
        primes.append(number)

print(f'primes - {primes}')
print(f'not_primes - {not_primes}')
