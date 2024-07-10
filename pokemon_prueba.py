import streamlit as st 
import pandas as pd 
import sqlite3
import plotly.express as px 
import matplotlib.pyplot as plt

#cagar columnas 
st.set_page_config (page_title= "Pokemon.app", layout= "wide")


#Pregunta 1
with st.container():
    st.write ("---")
    st.header ("1.	¿Cuáles han sido los mejores pokemones en cada generación según sus puntos de base?")


# Conectar bbdd 
github_url = "https://github.com/SantyIronman/Pokemon_proyect/blob/eba941067654486f8a24090cae426557cd4172cc/veekun-pokedex.sqlite"
conn = sqlite3.connect(github_url)

cur = conn.cursor()

#consulta
cur.execute ("""
                SELECT identifier, type, generation, base_experience, Puntos_de_base, max (base_stat)
                FROM limpia_bbdd
                WHERE generation BETWEEN "generation-i" AND "generation-iv" AND Puntos_de_base = "hp"
                GROUP BY generation
                ORDER BY max (base_stat) ASC;
                """)
result = cur.fetchall()

df = pd.DataFrame (result, columns=['Pokemon', 'Tipo de Pokemon', 'Generacion', 'Cantidad minima de experiencia','Base', 'Puntos de Base'])

fig = px.bar(df, x="Generacion", y="Puntos de Base", color="Pokemon", 
             color_discrete_map={'drifblim': '#2A80C3', 'wailord': '#4BABF5', 'chansey': '#95D0FE', 'blissey': '#9FC6E5'}, 
             barmode="stack")

st.dataframe(df)

st.plotly_chart(fig, use_container_width=True)

    



