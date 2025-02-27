import pandas as pd

#Para carregar arquivo para dataframe Pandas (no formato csv)
dados = pd.read_csv("Credit.csv")

#Para ver o "corpo" da tabela
dados.shape

#retorna um resumo estatístico de colunas númericas
dados.describe()

#retorna as primeiras linhas da tabela (aceita parâmetro)
dados.head(6)

#retorna as últimas linhas da tabela (aceita paramêtro)
dados.tail(3)
