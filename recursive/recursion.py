def power(base, exponent):
    
    if exponent == 0:
        return 1
    
    elif exponent == 1:
        return base
    
    elif exponent > 0:
        return base * power(base, exponent - 1)

    else:
        return 1 / power(base, -exponent)
base = 8
exponent = 5
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")

base = 8
exponent = -3
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")
