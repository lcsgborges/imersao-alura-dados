import pandas as pd
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

# =================== AULA 02 ===================

# Verificando valores Null:
print(df.isnull()) # se null -> true 

# Somando valores de null por coluna:
print(df.isnull().sum())

# Checando anos do dataframe para verificar os dados nulos:
print(df['ano'].unique()) # nan = not a number

# Exibindo os campos nulos agora:
print(df[df.isnull().any(axis=1)]) #axis=1 -> opera por linha

# Exibindo campos sem null

df_limpo = df.dropna()

print(df_limpo.isnull().sum()) # mostrando que não possui mais valores null

# Modificando nosso dataframe['ano'] de float para int:

df_limpo = df_limpo.assign(ano = df_limpo['ano'].astype('int'))

print(df_limpo.tail(n=10))
print(df_limpo.info())