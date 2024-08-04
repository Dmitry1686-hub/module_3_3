nambers = [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primes = []
not_primes = []

for a in nambers:
    if a == 1:
        is_primes = True
        continue
    for b in range(2, a) :
            if a % b == 0:
                is_primes = False
                not_primes.append(a)
                break
    if a not in not_primes:
            primes.append(a)

print('Primes:', primes)
print('Not primes:', not_primes)
