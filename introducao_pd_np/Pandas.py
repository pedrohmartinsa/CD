import pandas as pd
import numpy as np

#Para carregar arquivo para dataframe Pandas (no formato csv)
dados = pd.read_csv("../Credit.csv")

#Para ver o "corpo" da tabela
dados.shape

#retorna um resumo estatístico de colunas númericas
dados.describe()

#retorna as primeiras linhas da tabela (aceita parâmetro)
dados.head(6)

#retorna as últimas linhas da tabela (aceita paramêtro)
dados.tail(3)

#Para filtrar pelo nome da coluna (onde está "duration" poderia ser qualquer outro nome)
dados[["duration"]]

#Para filtrar um intervalo de linhas
dados.loc[1:4]

#Filtra apenas as linhas que você quer ver (nesse caso vai mostrar apenas as linhas 10 e 20)
dados.loc[[10, 20]]

#Para filtrar pelo valores de determinada coluna (nesse caso vai mostrar apenas as linhas que contém "radio/tv" na coluna "purpose")
dados.loc[dados["purpose"] == "radio/tv"]

#outra condição envolvendo colunas e seus respectivos valores
dados.loc[dados["credit_amount"] > 18000]

#atribui valor à variável criando outro dataframe
credito2 = dados.loc[dados["credit_amount"] > 18000]
# print(credito2)

#filtrando apenas as colunas que ver dessa condição
credito3 = dados[["checking_status", "duration"]].loc[dados["credit_amount"] > 18000]
# print(credito3)

#SÉRIES
#representam uma única coluna
#é possível criar à partir de listas, array no numpy e colunas de um dataframe

s1 = pd.Series([1, 23, 4, 6, 16])
# print(s1)

#usando o numpy
array1 = np.array([3, 6, 9, 12, 15])
s2 = pd.Series(array1)
# print(s2)

#usando uma coluna do dataframe
s3 = dados["purpose"]
# print(s3)

#renomear de forma indefinitiva (não muda no dataframe original)
dados.rename(columns={"duration": "duração", "purpose": "propósito"})

#para mudar o dataframe original
#dados.rename(columns={"duration": "duração", "purpose": "propósito"}, inplace=True)

#para remover uma coluna
#dados.drop("checking_status", axis=1, inplace=True)

#verificar dados nulos
dados.isnull()
dados.isnull().sum()

#remover dados com Nan
dados.dropna()
#ou
#preencher os dados Nan
# dados["duration"].fillna(0, inplace=True)

#localizar intervalos de linhas e colunas, respectivamente
dados.iloc[0:2, 0:3]

#localizar linhas especificas de colunas (vai mostrar as linhas 1, 2, 5 e 7 das primeiras 4 colunas)
dados.iloc[[1, 2, 5, 7], 0:4]
