numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes, not_primes = list(), list()

for number in numbers:
    if number == 1:
        continue
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime == 1:
        primes.append(number)
    else:
        not_primes.append(number)

print(f'primes - {primes}')
print(f'not_primes - {not_primes}')
