a,b = map(int,input().split())
mod_val = 107
rslt = 1
a = a % mod_val

while b > 0:
    if b % 2 != 0: 
        rslt = (rslt * a) % mod_val
    a = (a**2) % mod_val
    b = b//2 


print(rslt)