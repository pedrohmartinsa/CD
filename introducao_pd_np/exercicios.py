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
def frase_vertical(texto):
    for i in texto:
        print(i)

#3
def preco_por_peso(peso):
    preco = 0

    if peso < 0:
        print("Peso inválido, digite um número positivo.")
    elif 0 < peso <= 10:
        preco = 50
    elif 20 > peso > 10:
        preco = 80
    else:
        print("Não transportamos esse peso.")
    print(f"Para {peso:.0f}Kg, cobraremos R${preco:.2f}.")
