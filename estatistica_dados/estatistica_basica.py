import pandas as pd
import numpy as np

#Configuração do Display
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#Carregamento do DataFrame
df = pd.read_csv('D:/Usuario/Alessandro/OneDrive/Área de Trabalho/Analista de Dados/EBAC/Python/Estatistica Básica/clientes-v3-preparado.csv')

#Exibição do DataFrame
print(df)

#Cálculos Estatísticos com Pandas
print('Estatística com Pandas')
print('Média: ',df['salario'].mean())
print('Mediana: ', df['salario'].median())
print('Variância: ', df['salario'].var())
print('Desvio Padrão: ', df['salario'].std())
print('Moda: ', df['salario'].mode()[0])
print('Mínimo:\n ', df['salario'].min())
print('Quartis: \n', df['salario'].quantile([0.25, 0.5, 0.75]))
print('Máximo: ', df['salario'].max())
print('Contagem de não nulos: ',df['salario'].value_counts().sum())
print('Soma: ',df['salario'].sum())


#Estrutura de dados
print("\nColuna do Dataframe:\n", df['salario'] )
print("Array do campo: ", df['salario'].values)

#Cálculos Estatísticos com Numpy
print('Estatistica com Numpy')
print("Média com coluna:", np.mean(df['salario']))
print("Média com array", np.mean(df['salario'].values))

array_campo = df['salario'].values
print("Mediana:" , np.median(array_campo))
print("Variância:", np.var(array_campo))
print("Desvio Padrão:", np.std(array_campo))
print("Mínimo:", np.min(array_campo))
print("Quartis:\n", np.quantile(array_campo, q=[0.25, 0.5, 0.75]))
print('porcentagem 25%, 50%, e 75%:\n ', np.percentile(array_campo, q=[25, 50, 75]))
print('Máximo: ', np.max(array_campo))
print('Contagem de não zeros: ', np.count_nonzero(array_campo))
print('Soma: ', np.sum(array_campo))