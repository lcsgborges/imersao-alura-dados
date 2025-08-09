# Plotando gráficos usando 'seaborn' e 'matplotlib':

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =================== CONFIGURACOES ===================

URL_DATA_BASE = 'salaries.csv'

df = pd.read_csv(URL_DATA_BASE)

colunas_pt_br = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'frequencia_remoto',
    'company_location': 'pais_empresa',
    'company_size': 'tamanho_empresa'
}

df.rename(columns=colunas_pt_br, inplace=True)

senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}

contrato = {
    'FT': 'Integral',
    'CT': 'Contrato Temporário',
    'PT': 'Meio-período',
    'FL': 'Freelance'
}

frequencia_remoto = {
    0: 'Presencial',
    100: 'Remoto',
    50: 'Híbrido'
}

tamanho_empresa = {
    'M': 'Media',
    'L': 'Grande',
    'S': 'Pequena'
}

df['senioridade'] = df['senioridade'].replace(senioridade)
df['contrato'] = df['contrato'].replace(contrato)
df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
df['frequencia_remoto'] = df['frequencia_remoto'].replace(frequencia_remoto)

df_limpo = df.dropna()
# ===========================================================

# Plotando um gráfico de barras de senioridade e salário em dolar (usd)

# sns.barplot(data=df_limpo, x='senioridade', y='usd')
# plt.show()

# Podemos configurar a nossa figura usando o matplotlib.pyplot:

# plt.figure(figsize=(8,5))
# sns.barplot(data=df_limpo, x='senioridade', y='usd')
# plt.title('Salário médio por senioridade')
# plt.xlabel('Senioridade')
# plt.ylabel('Salário médio anual (USD)')
# plt.show()

# Podemos ordenar isso agora:
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index

print(ordem)

# Ordenando agora:

# sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
# plt.title('Salário médio por senioridade')
# plt.xlabel('Senioridade')
# plt.ylabel('Salário médio anual (USD)')
# plt.show()

# Plotando um gráfico de histograma:

# plt.figure(figsize=(10,5))
# sns.histplot(data=df_limpo['usd'], bins=50, kde=True)
# plt.title('Distribuição dos salários anuais em USD')
# plt.xlabel('Salário médio anual (USD)')
# plt.ylabel('Frequência')
# plt.show()

# Plotando um gráfico de caixa para entender os dados de uma maneira mais técnica:

# plt.figure(figsize=(8,5))
# sns.boxplot(data=df_limpo['usd'])
# plt.title('Boxplot salário')
# plt.xlabel('Salário anual em USD')
# plt.show()

# Distribuindo salário por senioridade:

# order_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
# plt.figure(figsize=(10,5))
# sns.boxplot(data=df_limpo, x='senioridade', y='usd', order=order_senioridade)
# plt.title('Distribuição salarial por senioridade - Boxplot')
# plt.xlabel('Senioridade')
# plt.ylabel('Salário anual USD')
# plt.show()

# Usando plotly para gerar gráficos dinâmicos:

import plotly.express as px

senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).reset_index()

fig = px.bar(senioridade_media_salario, x='senioridade', y='usd',
             title='Média Salarial por Senioridade',
             labels={'senioridade': 'Nível de senioridade', 'usd': 'Média anual salarial (usd)'})
fig.show()

# Criando um gráfico de pizzas para verificar os tipos de trabalho:

remoto_frequencia = df_limpo['frequencia_remoto'].value_counts().reset_index()

remoto_frequencia.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_frequencia,
             names='tipo_trabalho',
             values='quantidade',
             title='Distribuição por tipo de trabalho',
             labels={'tipo_trabalho': 'Tipo do trabalho',
                     'quantidade': 'Quantidade'},
             hole=0.3)
fig.update_traces(textinfo='percent+label')
fig.show()