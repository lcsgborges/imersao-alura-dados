import pandas as pd
import numpy as np

# CRIANDO UM DATA FRAME PARA MANIPULAR VALORES NULOS:

df_salarios = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Caio', 'Daniela'],
    'salario': [4000, np.nan, 2500, 3200]
})

# Observando nosso data frame:
print(df_salarios.head())

# Para preencher os valores nan com outros valores, podemos calcular a média de salários e preencher com esse valor:

df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
# fillna() -> preencher os valores NaN

print(df_salarios.head())

# Podemos preencher com mediana também:
# ao invés de usar .mean(), usamos .median():

df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())

print(df_salarios.head())

# =========== Completando com ffill e bfill:

df_temperaturas = pd.DataFrame({
    'dia': ['segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo'],
    'temperatura': [29, 28, np.nan, 25, 24, np.nan, 27]
})

# Complentando com ffill(): pega o valor anterior e usar ele no lugar:

df_temperaturas['temperatura_ffill'] = df_temperaturas['temperatura'].ffill()

# Complentando com bfill(): pega o valor que está na frente:

df_temperaturas['temperatura_bfill'] = df_temperaturas['temperatura'].bfill()

print(df_temperaturas.head(n=7))

# ===================== Completando com strings (texto):

print()

df_cidades = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Caio', 'Daniele', 'Eduardo'],
    'cidade': ['Rio de Janeiro', np.nan, 'Curitiba', np.nan, 'Porto Alegre']
})

df_cidades['cidade_preenchida'] = df_cidades['cidade'].fillna('Nao informado')

print(df_cidades.head())

# Outra coisa que podemos fazer é excluir os valores null dosso dataframe:

df_teste = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Daniele', 'Eduardo'],
    'idade': [20, 21, 34, np.nan, 31]
})

df_teste_limpo = df_teste.dropna()

print(df_teste_limpo.head()) # vai mostrar apenas os dados que não possui null