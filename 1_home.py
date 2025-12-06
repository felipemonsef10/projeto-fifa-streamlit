import streamlit as st
import pandas as pd
import webbrowser

st.set_page_config(
    page_title='Overview',
    layout='wide'
)

if 'data' not in st.session_state:
    df_data = pd.read_csv(r'datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data.loc[df_data['Contract Valid Until'] > 2023]
    df_data = df_data.loc[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data

st.markdown('# FIFA2023 OFFICIAL DATASET!')
st.sidebar.markdown("Desenvolvido por Felipe Monsef")
# st.sidebar.markdown("Felipe Monsef")

btn = st.link_button('Acesse os dados no Kaggle', 'https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')

st.markdown("""## Visão Geral
O dataset contém informações abrangentes sobre jogadores de futebol profissional, cobrindo o período de 2017 a 2023.

## Características Principais
- **Volume**: Mais de 17.000 registros
- **Atributos**: 
  - Dados demográficos dos jogadores
  - Características físicas
  - Estatísticas de desempenho
  - Detalhes contratuais
  - Afiliações de clubes

## Aplicações
Ideal para análise de:
- Atributos e métricas de desempenho dos jogadores
- Avaliação de mercado e valorização
- Análise de clubes
- Posicionamento de jogadores
- Desenvolvimento dos jogadores ao longo do tempo

## Público-Alvo
Analistas de futebol, pesquisadores e entusiastas do esporte""")