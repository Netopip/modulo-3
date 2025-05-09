def par(n):
    if type(n) != int or n <= 0:
        return Exception
    return n%2 == 0
    

assert par(2) == True
assert par(3) == False
assert par(0) == Exception
assert par(-1) == Exception
assert par(1.5) == Exception
assert par(' ')== Exception

print('ok')