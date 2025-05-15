def calc_power_mod(base, exp, mod):
    res = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1: 
            res = (res * base) % mod
        base = (base * base) % mod
        exp = exp // 2 
    return res

def remainder(base, exponent, modulus):
    if base == 1:
        return exponent % modulus
    temp = calc_power_mod(base, exponent + 1, modulus * (base - 1))
    final_rem = ((temp - base) // (base - 1)) % modulus
    return final_rem

num_cases = int(input())
for i in range(num_cases):
    base, exponent, modulus = map(int, input().split())
    print(remainder(base, exponent, modulus))
