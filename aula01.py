import pandas as pd

# SITE PARA PEGAR BASE DE DADOS: KAGGLE

URL_DATA_BASE = 'salaries.csv'

# Definindo nosso Data Frame:
df = pd.read_csv(URL_DATA_BASE)

# Para saber o números de linhas x colunas do nosso dataframe:
linhas, colunas = df.shape
print(f'linhas = {linhas} | colunas = {colunas}')

# Exibindo informações úteis do nosso dataframe
print(df.info())

# Exibindo informações um pouco mais detalhada dos dados (apenas dados numéricos por padrão - int64 ou float)
print(df.describe())

# Para exibir os 5 primeiros dados do dataframe:
print(df.head())

# Para exibir os 5 últimos dados do dataframe:
print(df.tail())

# Exibir nome de colunas:
print(df.columns)

# Podemos renomear as colunas agora para pt-br:

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

# Verificando se mudou realmente:
print(df.columns)

# Contando valores de uma determinada coluna:
print(df['senioridade'].value_counts())
# SE - SENIOR | MI - PLENO | EN - JUNIOR | EX - EXECUTIVO


# Podemos renomear as categorias também (linhas):
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

# Podemos usar o describe() para incluir outros tipos de dados para serem analisados, vamos usar o object:

print(df.describe(include='object'))

# count -> qtd de linhas
# unique -> qtd de valores diferentes
# top -> valor que mais aparece
# freq -> qtd de vezes que o 'valor top' mais apareceu

# Nossa base de dados atualizada:
print(df.describe())