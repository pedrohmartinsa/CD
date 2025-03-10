import numpy as np

#cria uma matriz unidimensional

mt = np.array([1, 2, 3, 4])

#cria uma matriz do tipo float

mt2 = np.array([1, 2, 3, 4], dtype=np.float64)

#===================================================================================================================#
#mudar o tipo de array
#para int
mt3 = np.array([1, 2.34, 5.7986, 4.9999])

mt3new = mt3.astype(np.int32)

#para float
mt4 = np.array([1, 2, 3, 4])

mt4new = mt4.astype(np.float64)

#===================================================================================================================#
#cria uma matriz bidimensional
mt7 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


#===================================================================================================================#
#criar array vazios tipificados
#empty significa que não são inicializado, e não que estão vazios
vazio = np.empty([4, 4], dtype=int)

#cria uma matriz 4x3 com valores zeros
zeros = np.zeros([4, 3], dtype=int)

#com valores igual a um
um = np.ones([2, 2], dtype=int)

#cria uma matriz quadrada com a diagonal principal com os valores igual a um e o resto zero
diagonalUm = np.eye(3, dtype=int)

#===================================================================================================================#
#valores aleatórios entre zero e um
ale = np.random.random(5)

#valores com uma distribuição normal com números negativos
ale2 = np.random.randn(5)

#valores aleatórios 3x4
ale3 = (10*np.random.random((3, 4)))

#===================================================================================================================#
#outra forma de gerar aleatório
#uso de semente
gnr = np.random.default_rng(1)
ale4 = gnr.random(3)

#gerar inteiros
ale5 = gnr.integers(10, size=(2, 2))

#===================================================================================================================#
#unique remove repetições
j = np.array([1, 2, 2, 4, 3, 5, 6, 6, 7, 6, 8])
j = np.unique(j)

#===================================================================================================================#
#funções específicas
k = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#mostra um elemento espicífico da matriz k
#print(k[2][0])

#mostra a disposição da matriz
#print(k.shape)

#===================================================================================================================#
#Funçoes matematicas
#mostra o maior valor da matriz k
#print(k.max())

#mostra o menor valor da matriz k
#print(k.min())

#mostra a soma dos valores da matriz k
#print(k.sum())

#mostra a média dos valores da matriz k
#print(k.mean())

#mostra o valor de desvio padrão (standart desviation) da matriz k
#print(k.std())

#===================================================================================================================#
#Funções universais, aplicadas a todos os elementos
k1 = np.array([4, 9, 16, 25])

#mostra a raiz quadrada de todos os elementos
#print(np.sqrt(k1))

#mostra o exponencial de todos os elementos
#print(np.exp(k1))

#===================================================================================================================#
#Extração de elementos
m = np.array([1, 2, 3, 4, 5, 6])

#mostra o segundo elemento
#print(m[1])

#mostra o array criado a partir da posição 0, dois elementos
#print(m[0:3])

#mostra o array a partir da segunda posição até o fim
#print(m[1:])

#mostra o array do antepenúltimo elemento até o fim
#print(m[-3:])

#===================================================================================================================#
#Extração de linhas e colunas
l = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

#primeira linha, todas as colunas
#print(l[0, :])

#segunda linha, todas as colunas
#print(l[1, :])

#segunda linha, todas as colunas
#print(l[2, :])

#todas as linhas, primeira coluna
#print(l[:, 0])

#todas as linhas, segunda coluna
#print(l[:, 1])

#todas as linhas, terceira coluna
#print(l[:, 2])

#===================================================================================================================#
#adição e multiplicação de matrizes
p = np.array([[3, 7, 8], [2, 4, 6], [9, 1, 5]])
q = np.array([[2, 6, 8], [3, 5, 7], [1, 9, 4]])
#soma
#print(p+q)

#multiplicação
#print(p*q)

#===================================================================================================================#
#Transposição
#rearranja um conjunto de 15 elementos (de 0 a 14) em 3 linhas e 5 colunas
r = np.arange(15).reshape(3, 5)
#print(r)

#mostra a raiz tranposta entre linha e coluna
#print(r.T)
#ou
#print(r.transpose())

#===================================================================================================================#
#Expressões lógicas
v = np.random.randn(4, 4)
print(v)

#criando a matriz com valores booleanos baseado na matriz v
x = (v > 0)
print(x)

#criando valores com -1 e 1 baseado nos valores da matriz x
z = np.where(x > 0, 1, -1)
print(z)
