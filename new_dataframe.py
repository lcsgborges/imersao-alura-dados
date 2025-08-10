import pandas as pd


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

df_limpo.to_csv('new_salaries.csv', index=False)