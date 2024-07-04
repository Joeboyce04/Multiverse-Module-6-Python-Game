def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def count_primes(N):
    count = 0
    for num in range(2, N):
        if is_prime(num):
            count += 1
    return count

N = 20
number_of_primes = count_primes(N)