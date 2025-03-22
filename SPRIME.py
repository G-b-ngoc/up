
def ng_to(kt):
    if kt < 2:
        return False
    for i in range(2, kt // 2 +1):
        if kt % i == 0:
            return False
    return True
def count_divisors(n):
    x = 0 
    for i in range(1, n + 1):
        if n % i == 0:
            x += 1
    return x

def ng_to2(kt):
    if kt < 2:
        return False
    for i in range(2, kt // 2 +1):
        if kt % i == 0:
            return False
    return True
def count_divisors(n):
    x = 0 
    for i in range(1, n + 1):
        if n % i == 0:
            x += 1
    return x

a = int(input())
b = int(input())
# if 0 < a and b < 10**7:
        
prime_count = 0
prime_sum = 0


k = count_divisors(a)
f = count_divisors(b)
print(k, f)
