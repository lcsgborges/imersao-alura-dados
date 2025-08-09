# =================== CONFIGURACOES ===================

import pandas as pd
import plotly.express as px

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

# =============== DESAFIO PROPOSTO

# Exibir somente os cargos de Data Scientist e a média salarial deles por países


mask = df_limpo['cargo'].str.fullmatch(r'Data Scientist', case=False, na=False)

df_data_scientist = df_limpo[mask]

media_salarial_paises = df_data_scientist.groupby('residencia')['usd'].mean().reset_index().sort_values('usd', ascending=True)

fig = px.bar(media_salarial_paises,
             x='residencia',
             y='usd',
             title='Média salarial anual em USD por país para Data Scientist',
             labels={'residencia': 'País',
                     'usd': 'Média Salarial Anual (USD)'}
             )
fig.show()