
def raise_to_power(base, power):
    result = 1
    for i in range(power):
        result *= base
    return result

print(raise_to_power(5,2))