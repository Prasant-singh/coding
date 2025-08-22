def generate_prime(n):
    if n <= 1:
        yield []
    primes = []
    for i in range(2,n):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    yield primes


print(list(generate_prime(20)))