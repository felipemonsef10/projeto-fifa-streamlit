import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(
    page_title='Players',
    layout='wide'
)

df_data = st.session_state['data']

clubes = df_data['Club'].unique()
club = st.sidebar.selectbox('Clube', clubes)

df_players = df_data.loc[df_data['Club'] == club]

players = df_players['Name'].unique()
player = st.sidebar.selectbox('Name', players)

info_player = df_players.loc[df_players['Name'] == player].iloc[0]


url = info_player['Photo']
req = requests.get(url)
img = Image.open(BytesIO(req.content))
st.image(img)
st.title(info_player['Name'])

st.markdown(f'**Clube:** {info_player["Club"]}')
st.markdown(f'**Posição:** {info_player["Position"]}')

col1, col2, col3 = st.columns(3)
col1.write(f'**Idade:** {info_player["Age"]}')
col2.write(f'**Altura:** {info_player["Height(cm.)"] / 100}')
col3.write(f'**Peso:** {info_player["Weight(lbs.)"] * 0.453:.2f}')

st.divider()

st.subheader(f'Overall: {info_player["Overall"]}')
st.progress(int(info_player['Overall']))

col1, col2, col3 = st.columns(3)
col1.metric('Valor de mercado', f"£ {info_player['Value(£)']:,}")
col2.metric('Remuneração semanal', f"£ {info_player['Wage(£)']:,}")
col3.metric('Cláusula de recisão', f"£ {info_player['Release Clause(£)']:,}")