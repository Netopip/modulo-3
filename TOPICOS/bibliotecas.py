import pandas as pd
import numpy as np


#data = pandas.read_csv()

'''
s = [1,2,3,4,5]
variancia = np.var(s)
print(variancia)
'''
    
    
# Criando um DataFrame de exemplo
data = pd.DataFrame({
    'Nome': ['Neto', 'Leomar', 'Vinicius', 'Jhonas', 'Vic'],
    'Idade': [25, 34, 23, 12, 41],
    'Sexp': ['M', 'G', 'M', 'M', 'F']
})
print(data)
