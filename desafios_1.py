# 1 problema: duas somas
#o problema é encontrar dois números em uma lista que somam um determinando número alvo. precisamos retornar
# os índices dessses dois números em qualquer ordem. podemos assumir que existem apenas uma solução válida
# e não podemos usar o mesmo elemnto duas vezes
def imprime_lista(lista):
    n = 0

    print('###valores da lista ###')
    while n < len(lista):
        print(f"lista[{n} = {lista [n]}")
        n += 1

def coordenadas_soma(lista, valor):
    n1 = 0

    while n1 < len(lista):
        n2 = n1 + 1
        while n2 < len(lista):
            if (lista[n1]+lista[n2]) == valor:
                return(n1,n1)
            n2 += 1
        n1 += 1 

    raise Exception('par não encotrado')

numeros = [5, 2, 3, 1, 6, 7]
soma_10 = coordenadas_soma(numeros, 10)
print(soma_10)
