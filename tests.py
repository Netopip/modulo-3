import pydantic
import typing

def NumeroPar(n):
    if type(n)!= int:
        return Exception
    else:
        return True if n%2 == 0 else False



if __name__ == '__main__':
    assert NumeroPar(2) == True
    assert NumeroPar(3) == False
    assert NumeroPar(0) == True
    assert NumeroPar(-2) == True
    assert NumeroPar('a') == Exception
    assert NumeroPar(2.5) == Exception
    
print('Te"stes ok')
    
    

