def prime_num_generator():
    num = 0
    while True:
        yield num
        num += 1


generator = prime_num_generator()

print(next(generator))
print(next(generator))
print(next(generator))
def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if not number % prime:
                break
        else:
            prime_numbers.append(number)
            yield number
            
     for number in prime_numbers_generator(n=20):
     print(number)
