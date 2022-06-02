import sympy
import random
import math


def generate_random_prime_number(length=10):
    n = 4
    while not sympy.isprime(n):
        n = random.randint(10 ** (length-1), 10**length - 1)
    return n


def generate_s(n):
    flag = True
    while flag:
        s = random.randint(1, n-1)
        if math.gcd(s, n)==1:
            flag = False
    return s
        

#  T generates n=p*q, p and q are prime
p = generate_random_prime_number(length=10)
q = generate_random_prime_number(length=10)
n = p * q
print(f"T:  \n  p = {p} \n  q = {q} \n  n = {n}")


#  A chooses secret s Є [1, n-1]
s = generate_s(n)
v = pow(s, 2, n)  #  A's public key
print(f'A:  \n  s = {s} \n  v = {v}\n')

t = 10  #  Number of rounds
for i in range(t):
    print(f'\t\tRound {i+1}')

    #  A chooses r Є [1, n-1] and sends x to B
    r = random.randint(1, n-1)
    x = pow(r, 2, n)
    print(f'A: \n  r = {r} \n  x = {x} ')

    #  B chooses e Є {0, 1}
    e = random.choice([0, 1])
    print(f'B: \n  e = {e}')

    #  A calculates y
    y = r*s % n if e else r
    print(f'A: \n  y = {y}')

    #  B verifies y
    if not y or pow(y, 2, n) != x * v**e % n:
        print('B: \n  rejected')
        break
    print('B: \n  OK')
