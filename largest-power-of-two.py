import math
def nearest_power_of_two(n):
    """
    Return the power of two that is closest to n (must be <=n)
    """
    candidate = n
    while candidate >=0:
        number = candidate
        if number%2 ==0:
            while number%2 == 0:
                number /= 2
                if number ==1:
                    return candidate
        candidate -=1

def nearest_power_of_two_v1(n):
    """
    Return the power of two that is closest to n (must be <=n)
    """
    square = 2
    sol = 1
    while square <= n:
        sol = square
        square = square*2
    return sol

nearest_power_of_two(5) # 4
nearest_power_of_two(10) # 8

nearest_power_of_two_v1(5)
nearest_power_of_two_v1(10)

# NOTE: other helpful Python functions:
#decimalPart, integerPart = math.modf(math.sqrt(candidate))
#integerPart, decimalPart = divmod(n, 1)
#print "sqrt result parts: ", candidate, " integerPart and decimal: ", integerPart, decimalPart
