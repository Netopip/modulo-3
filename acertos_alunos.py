from random import * 
import string
  
def verificar_acertos(lista,gabarito):
    acertos = 0
    for i in range(len(lista)):
        if lista[i] == gabarito[i]:
            acertos+=1
            
    return (lista,acertos)

gabarito_correto = [choice(string.ascii_uppercase[:5]) for _ in range(15) ]
numero_alunos = 5


dicionario_alunos={}

for i in range(numero_alunos):
    dicionario_alunos[i] = verificar_acertos(([choice(string.ascii_uppercase[:5]) for i in range(15)]),gabarito_correto)

print(f'        {gabarito_correto}')
for i,j in dicionario_alunos.items():
    print(f'Aluno {i+1}:{j[0]}\nAcertos: {j[1]}')


    


    

    
            