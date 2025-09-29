import pandas as pd
import numpy as np

# Configuração do Display
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Carregamento do DataFrame
df = pd.read_csv('D:/Usuario/Alessandro/OneDrive/Área de Trabalho/Analista de Dados/EBAC/Python/Estatistica Básica/clientes-v3-preparado.csv')

# Estatísticas do DataFrame
print('Estatística do dataFrame: \n', df.describe())

# Estatísticas de um campo específico
print('Estatística de um campo: \n', df[['salario', 'idade']].describe())

# Correlação entre 'salario' e 'idade'
print('Correlação: \n', df[['salario', 'idade']].corr())

# Correlação com Normalização (verifique se essas colunas existem no seu DataFrame)
print('Correlação com Normalização: \n', df[['salarioMinMaxScaler', 'idadeMinMaxScaler']].corr())

# Correlação com Padronização (verifique se essas colunas existem no seu DataFrame)
print('Correlação com Padronização: \n', df[['salarioStandardScaler', 'idadeStandardScaler']].corr())

# Correlação com RobustScaler (verifique se essas colunas existem no seu DataFrame)
print('Correlação com RobustScaler: \n', df[['salarioRobustScaler', 'idadeRobustScaler']].corr())

# Correlação entre as variáveis originais e escalonadas
print('Correlação: \n', df[['salario', 'idade', 'idadeMinMaxScaler', 'idadeStandardScaler', 'idadeRobustScaler']].corr())

# Filtrando clientes menores de 45 anos
df_filtro_idade = df[df['idade'] < 45]

# Correlação para clientes menores de 45 anos
print('Correlação de clientes menores de 45 anos: \n', df_filtro_idade[['salario', 'idade']].corr())

# Criação da variável espúria (sequência crescente)
df['variavel_espuria'] = np.arange(len(df))

# Impressão dos valores da variável espúria
print('Variável espúria: ', df['variavel_espuria'].values)

# Seleção das colunas para calcular a correlação de Pearson
pearson_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod',
                   'area_atuacao_cod', 'estado_cod', 'variavel_espuria']]

spearman_corr = df[['salario', 'idade', 'anos_experiencia', 'idade_anos_experiencia_interac', 'numero_filhos', 'nivel_educacao_cod',
                   'area_atuacao_cod', 'estado_cod', 'variavel_espuria']].corr(method='spearman')


# Exibição das correlações
print('Correlação de Pearson : \n', pearson_corr)
print('Correlação de Spearman: \n', spearman_corr)



