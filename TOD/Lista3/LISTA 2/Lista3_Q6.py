

def FaturamentoTotal(lista1:list,lista2:list):
    faturamento = []
    faturamentoTotal = 0
    abaixoFaturamentos = 0
    
    if len(lista1) != 5 or len(lista2) != 5:
        return Exception
    else:
        for i in range(len(lista1)):
            if type(lista1[i]) != int or type(lista2[i]) != int:
                return Exception
            else:
                faturamento.append(lista1[i] * lista2[i])
                faturamentoTotal += (lista1[i] * lista2[i])
                
    mediaFaturamento = faturamentoTotal/len(lista1)
    
    for i in faturamento:
        if i < mediaFaturamento:
            abaixoFaturamentos += 1
            
    return faturamento,faturamentoTotal,mediaFaturamento,abaixoFaturamentos

assert FaturamentoTotal([1,2,3,4,5],[6,7,8,9,10]) == ([6,14,24,36,50],sum([6,14,24,36,50]),26.0,3)

print('testes ok')