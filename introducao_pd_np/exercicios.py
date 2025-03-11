#1 - Uma função que retorne a amplitude de uma lista (amplitude=diferença entre o maior e o menor valor)
#2 - Uma função que retorne uma string de forma vertical
#3 - Uma função que retorne o preço dos pesos (até 10Kg - R$50,00; 11Kg:20Kg - R$80,00; acima de 20Kg - não transporta)

lista = [12, 14, 8, 26, 4, 26, 35]

#1
def amplitude(lista):
    maior = lista[0]
    menor = lista[0]

    for i in lista:
        if i > maior:
            maior = i
        if i < menor:
            menor = i

    return maior - menor

#2
texto = input("Digite uma palavra: ")

print(list(texto))
