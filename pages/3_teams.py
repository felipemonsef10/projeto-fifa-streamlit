import streamlit as st
import requests

st.set_page_config(
    page_title='Teams',
    layout='wide'
)

df_data = st.session_state['data']

clubes = df_data['Club'].unique()
club = st.sidebar.selectbox('Clube', clubes)

df_filtered = df_data.loc[df_data['Club'] == club].set_index('Name')

req = requests.get(df_filtered.iloc[0]['Club Logo'])
st.image(req.content)
st.markdown(f'## {club}')

columns = [
    'Age', 'Overall', 'Value(£)',
    'Wage(£)', 'Joined', 'Height(cm.)',
    'Weight(lbs.)', 'Contract Valid Until',
    'Release Clause(£)'
]

st.dataframe(
    df_filtered[columns], 
    column_config={
        'Overall': st.column_config.ProgressColumn(label='Overall', format='%d'),
        'Wage(£)': st.column_config.ProgressColumn(label='Weekly Wage', format='£%f', min_value=0, max_value=df_filtered['Wage(£)'].max()),
        'Value(£)': st.column_config.NumberColumn(format='£%f'),
        'Release Clause(£)': st.column_config.NumberColumn(format='£%f'),
        # 'Flag': st.column_config.ImageColumn(),
        # 'Photo': st.column_config.ImageColumn()
    })