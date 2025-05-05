def primo(n):
    
    if type(n) != int or n < 1:
        return Exception
    if n == 1:
        return False
    for i in range(2,n):
        if(n%i == 0):
            return False
    return True

assert primo(3) == True
assert primo(1) == False
assert primo(2) == True
assert primo(13) == True
assert primo(21) == False
print('Deu certo!')