import streamlit as st 
import pandas as pd 
import sqlite3
import plotly.express as px 
import matplotlib.pyplot as plt
import urllib.request
import os

#cagar columnas 
st.set_page_config (page_title= "Pokemon.app", layout= "wide")


#Pregunta 1
with st.container():
    st.write ("---")
    st.header ("1.	¿Cuáles han sido los mejores pokemones en cada generación según sus puntos de base?")


# Conectar bbdd 
github_url = "https://github.com/SantyIronman/Pokemon_proyect/blob/eba941067654486f8a24090cae426557cd4172cc/veekun-pokedex.sqlite?raw=true"

db_path = "veekun-pokedex.sqlite"

urllib.request.urlretrieve(github_url, db_path)


db_abs_path = os.path.abspath(db_path)

conn = sqlite3.connect(db_abs_path)

cur = conn.cursor()



#consulta, dataframe y grafico que determina los mejores pokemones segun sus puntos de salud
cur.execute ("""
                SELECT identifier, type, generation, base_experience, Puntos_de_base, max (base_stat)
                FROM limpia_bbdd
                WHERE generation BETWEEN "generation-i" AND "generation-iv" AND Puntos_de_base = "hp"
                GROUP BY generation
                ORDER BY max (base_stat) ASC;
                """)
result = cur.fetchall()

conn.close()

df = pd.DataFrame (result, columns=['Pokemon', 'Tipo de Pokemon', 'Generacion', 'Cantidad minima de experiencia','Base', 'Puntos de Base'])


fig = px.bar(df, x="Pokemon", y="Puntos de Base", color="Generacion", 
             color_discrete_map={'generation-iv': '#2A80C3', 'generation-iii': '#4BABF5', 'generation-i': '#95D0FE', 'generation-ii': '#9FC6E5'}, 
             barmode="stack")


st.dataframe(df, width= 1000, hide_index= True)



st.plotly_chart(fig, use_container_width=True)

#consulta, dataframe y grafico que determina los mejores pokemones segun sus puntos de velocidad

try:
    conn = sqlite3.connect(db_abs_path)
    cur = conn.cursor()
    cur.execute("""
                SELECT identifier, type, generation, base_experience, Puntos_de_base, max (base_stat)
                FROM limpia_bbdd
                WHERE generation BETWEEN "generation-i" AND "generation-iv" AND Puntos_de_base = "speed"
                GROUP BY generation
                ORDER BY max (base_stat) ASC;
                """)
except sqlite3.Error as e:
    print(f"Error: {e}")
    st.error(f"Error: {e}")    


result = cur.fetchall()

conn.close()

df_speed = pd.DataFrame (result, columns=['Pokemon', 'Tipo de Pokemon', 'Generacion', 'Cantidad minima de experiencia','Base', 'Puntos de Base'])

fig = px.bar(df_speed, x="Pokemon", y="Puntos de Base", color="Generacion", 
             color_discrete_map={'generation-iv': '#2A80C3', 'generation-iii': '#4BABF5', 'generation-i': '#95D0FE', 'generation-ii': '#9FC6E5'}, 
             barmode="stack")

st.dataframe(df_speed, width= 1000, hide_index= True)

st.plotly_chart(fig, use_container_width=True)

#consulta, dataframe y grafico que determina los mejores pokemones segun sus puntos de defensa

try:
    conn = sqlite3.connect(db_abs_path)
    cur = conn.cursor()
    cur.execute("""
                SELECT identifier, type, generation, base_experience, Puntos_de_base, max (base_stat)
                FROM limpia_bbdd
                WHERE generation BETWEEN "generation-i" AND "generation-iv" AND Puntos_de_base = "defense"
                GROUP BY generation
                ORDER BY max (base_stat) ASC;
                """)
except sqlite3.Error as e:
    print(f"Error: {e}")
    st.error(f"Error: {e}")    


result = cur.fetchall()

conn.close()

df_defense = pd.DataFrame (result, columns=['Pokemon', 'Tipo de Pokemon', 'Generacion', 'Cantidad minima de experiencia','Base', 'Puntos de Base'])

fig = px.bar(df_defense, x="Pokemon", y="Puntos de Base", color="Generacion", 
             color_discrete_map={'generation-iv': '#2A80C3', 'generation-iii': '#4BABF5', 'generation-i': '#95D0FE', 'generation-ii': '#9FC6E5'}, 
             barmode="stack")

st.dataframe(df_defense, width= 1000, hide_index= True)

st.plotly_chart(fig, use_container_width=True)

#consulta, dataframe y grafico que determina los mejores pokemones segun sus puntos de ataque

try:
    conn = sqlite3.connect(db_abs_path)
    cur = conn.cursor()
    cur.execute("""
                SELECT identifier, type, generation, base_experience, Puntos_de_base, max (base_stat)
                FROM limpia_bbdd
                WHERE generation BETWEEN "generation-i" AND "generation-iv" AND Puntos_de_base = "attack"
                GROUP BY generation
                ORDER BY max (base_stat) ASC;
                """)
except sqlite3.Error as e:
    print(f"Error: {e}")
    st.error(f"Error: {e}")    


result = cur.fetchall()

conn.close()

df_attack = pd.DataFrame (result, columns=['Pokemon', 'Tipo de Pokemon', 'Generacion', 'Cantidad minima de experiencia','Base', 'Puntos de Base'])

fig = px.bar(df_attack, x="Pokemon", y="Puntos de Base", color="Generacion", 
             color_discrete_map={'generation-iv': '#2A80C3', 'generation-iii': '#4BABF5', 'generation-i': '#95D0FE', 'generation-ii': '#9FC6E5'}, 
             barmode="stack")

st.dataframe(df_attack, width= 1000, hide_index= True)

st.plotly_chart(fig, use_container_width=True)

