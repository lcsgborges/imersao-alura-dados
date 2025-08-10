import streamlit as st
import pandas as pd
import plotly.express as px
import pycountry


# --- Carregamento dos Dados ---
URL_DATA_FRAME = 'new_salaries.csv'
df = pd.read_csv(URL_DATA_FRAME)


# --- Configuração Inicial do Streamlit ---
st.set_page_config(
    page_title='Dashboard de Salários na Área de Dados',
    page_icon='🌐',
    layout='wide'
)


# --- Barra Lateral (filtros) ---
st.sidebar.header("Filtros")

# Filtro por ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect(label="Ano", options=anos_disponiveis, default=anos_disponiveis)

# Filtro por senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionados = st.sidebar.multiselect(label='Senioridade', options=senioridades_disponiveis, default=senioridades_disponiveis)

# Filtro por tipo de contrato
tipo_contrato = sorted(df['frequencia_remoto'].unique())
contrato_selecionados = st.sidebar.multiselect(label='Tipo de contrato', options=tipo_contrato, default=tipo_contrato)

# Filtro por tamanho da empresa
tamanho_empresa = sorted(df['tamanho_empresa'].unique())
tamanho_empresa_selecionado = st.sidebar.multiselect(label='Tamanho da empresa', options=tamanho_empresa, default=tamanho_empresa)


# --- Filtragem do dataframe ---
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionados)) &
    (df['frequencia_remoto'].isin(contrato_selecionados)) &
    (df['tamanho_empresa'].isin(tamanho_empresa_selecionado))
]


# --- Conteúdo Principal ---
st.title('Dashborad de Anaĺise de Salários na Área de Dados')
st.markdown('Explore os dados salariais na área de dados dos últimos anos. Utilize os filtros à esquerda para refinar sua busca.')


# --- Métricas principais ---
st.subheader('Métricas gerais (salário anual em USD)')

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado['cargo'].mode()[0]
else:
    salario_medio, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, ""
    
col1, col2, col3, col4 = st.columns(4)
col1.metric('Salário Médio', f'${salario_medio:,.0f}')
col2.metric('Salário Máximo', f'${salario_maximo:,.0f}')
col3.metric('Total de Registros', f'{total_registros:,}')
col4.metric('Cargo mais Frequente', cargo_mais_frequente)

st.markdown('---')

# --- Análise visual com gráficos ---
st.subheader('Gráficos')

colgraf1, colgraf2 = st.columns(2)

with colgraf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(top_cargos, x='usd', y='cargo', orientation='h', title='Top 10 cargos por salário médial anual (USD)', labels={'usd': 'Média salarial anual (USD)', 'cargo': 'Cargo'})
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de cargos')

with colgraf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(df_filtrado, x='usd', nbins=30, title='Distribuição de salários anuais', labels={'usd': 'Faixa salarial (USD)', 'count': ' '})
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de distribuição.')

st.markdown('---')

colgraf3, colgraf4 = st.columns(2)

with colgraf3:
    if not df_filtrado.empty:
        dados_contratos = df_filtrado['frequencia_remoto'].value_counts().reset_index()
        dados_contratos.columns = ['tipo_trabalho', 'quantidade']
        grafico_contrato = px.pie(dados_contratos, names='tipo_trabalho', values='quantidade', hole=0.4, title='Tipo de jornada de trabalho (contrato)')
        grafico_contrato.update_traces(textinfo='percent+label')
        grafico_contrato.update_layout(title_x=0.1)
        st.plotly_chart(grafico_contrato, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de tipo de jornada de trabalho')

def iso2_to_iso3(code):
    try:
        return pycountry.countries.get(alpha_2=code).alpha_3
    except:
        return None

# Criar nova coluna com código ISO-3
df['residencia_iso3'] = df['residencia'].apply(iso2_to_iso3)

with colgraf4:
    if not df_filtrado.empty:
        df_ds = df[df['cargo'] == 'Data Scientist']
        media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
        grafico_paises = px.choropleth(media_ds_pais, locations='residencia_iso3', color='usd', color_continuous_scale='rdylgn', title='Salário médio de cientista de dados por país', labels={'usd': 'Salário médio anual (USD)', 'residencia_iso3': 'País'})
        grafico_paises.update_layout(title_x=0.1)
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning('Nenhum dado para exibir no gráfico de países.')
    
st.markdown('---')    
    
# --- Tabela dos dados utilizados ---
st.subheader('Dados detalhados')
st.dataframe(df_filtrado)