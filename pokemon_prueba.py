import streamlit as st 
import pandas as pd 
import sqlite3
import plotly.express as px 
import matplotlib.pyplot as plt
import urllib.request
import os

#cagar columnas 
st.set_page_config (page_title= "Pokemon.app", layout= "wide")

#Titulo para el proyecto, Planteamiento del Problema, Objetivos, Marco Teorico
st.title("Análisis Estadístico de Pokémon desde la Generación I - IV")

st.image (r'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/025.png', width=400)

st.header ("Planteamiento del Problema")

st.write ("Desde su introducción en 1996, los Pokémon han capturado la imaginación de millones de personas en todo el mundo. A lo largo de las primeras cuatro generaciones de juegos (Generación I a IV), se han introducido cientos de especies diferentes, cada una con características únicas que definen sus habilidades, estadísticas y tipología. Las personas más fanáticas de esta franquicia prefieren la primera generación de Pokémon aun así viendo Pokémon mejores que la primera generación, entonces es necesario realizar un análisis estadístico para proporcionar una comprensión más profunda de la estructura de los Pokémon a lo largo del tiempo.")

st.header ("Objetivos")

st.write ('<ul><li>Determinar el Pokémon con mayor estadística para cada base: salud, velocidad, defensa, ataque, defensa especial, ataque especial.</li><li>Identificar el Pokémon con mayor experiencia de pelea.</li><li>Determinar si el peso del Pokémon lleva a que el Pokémon tengan menor velocidad al momento de pelear.</li></ul', unsafe_allow_html= True)

st.header ("Marco Teórico")

st.write ("""
<style>
p {
  text-align: justify;
}
</style>
<p>Pokémon = Una contracción del japonés Poketto Monsutā, que significa monstruo de bolsillo.</p>
<p>Pokémon es un proyecto que inció con la idea de crear un videojuego agradable para el público de los años 1990 cuando comenzaron a usarse consolas de videojuegos como el famoso “game boy”. En palabras de su creador:</p>
<p>"Diría que cuando comenzamos teníamos fe absoluta en lo que estábamos haciendo y queríamos llevar a los niños la alegría de descubrir criaturas especiales —los Pokémon—, de coleccionarlos, de combatir con ellos y de intercambiarlos: ese era nuestro sueño” – Junichi Masuda.</p>
<p>Los pokémon son criaturas de diferentes tipos y con diferentes habilidades. Actualmente en el universo del videojuego existen más de 800 criaturas ya que con cada generación que pasa esta lista se extiende con aproximadamente +80 pokémon por generación.</p>
<p>En el videojuego los pokémon viven en diferentes hábitats o entre los humanos que los crían y cuidan de ellos (llamados también entrenadores). Durante el transcurso del juego los pokémon adquieren experiencia y evolucionan para convertirse en pokémon más fuertes.</p>
<p>Cada pokémon cuenta con habilidades especiales iguales o diferentes a otros pokémon, para la cuarta generación hay más de 120 diferentes habilidades.</p>
<p>Existen 18 tipos y cada pokemon puede ser de uno o dos tipos (Ej: Solo tierra o tierra y eléctrico)</p>
<ul>
    <li>•	Normal.</li>
    <li>•	Lucha. </li>
    <li>•	Volador.</li>
    <li>•	Veneno.</li>
    <li>•	Tierra.</li>
    <li>•	Piedra.</li>
    <li>•	Bicho.</li>
    <li>•	Fantasma.</li>
    <li>•	Acero.</li>
    <li>•	Fuego.</li>
    <li>•	Agua.</li>
    <li>•	Planta.</li>
    <li>•	Eléctrico.</li>
    <li>•	Psíquico.</li>
    <li>•	Hielo.</li>
    <li>•	Dragón.</li>
    <li>•	Oscuro.</li>
    <li>•	Hada.</li>
</ul>
<p>En el universo de Pokémon existen 6 Generaciones: 1° Generación de 1996 con 151 Pokémon; 2° Generación de 1999 con 100 Pokémon; 3° Generación de 2002 con 135 Pokémon; 4° Generación de 2006 con 108 Pokémon; 5° Generación de 2010 con 156 Pokémon; 6° Generación de 2013 con 72 Pokémon.</p>
""", unsafe_allow_html=True)

#Pregunta 1
with st.container():
    st.write ("---")
    st.header ("1.	¿Cuáles han sido los Mejores Pokémon en cada Generación según sus Puntos de Base?")
    st.subheader("Los Pokémon con Mayor Puntos de Salud")
    


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

st.write ("El Pokémon que tiene Mayor Puntos de Salud es Blissey con 255 puntos, este Pokémon pertenece a la 2° generación")

st.image (r'https://static.pokemonpets.com/images/monsters-images-800-800/8242-Mega-Blissey.webp', width=300)

#consulta, dataframe y grafico que determina los mejores pokemones segun sus puntos de velocidad
st.subheader("Los Pokémon con Mayor Puntos de Velocidad")

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

st.write("El Pokémon que tiene Mayor Puntos de Velocidad es Ninjask con 160 puntos, este Pokémon pertenece a la 3° generación")

st.image (r'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/detail/292.png', width=400)


#consulta, dataframe y grafico que determina los mejores pokemones segun sus puntos de defensa

st.subheader("Los Pokémon con Mayor Puntos de Defensa")

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

st.write ("El Pokémon que tiene Mayor Puntos de Defensa es Shuckle con 230 puntos, este Pokémon pertenece a la 2° generación")

st.image (r'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/213.png', width=400)


#consulta, dataframe y grafico que determina los mejores pokemones segun sus puntos de ataque

st.subheader("Los Pokémon con Mayor Puntos de Ataque")

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

st.write ("El Pokémon que tiene Mayor Puntos de Ataque es Rampardos con 165 puntos, este Pokémon pertenece a la 4° generación")

st.image (r'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/409.png', width=400)

#consulta, dataframe y grafico que determina los mejores pokemones segun sus puntos de defensa-especial

st.subheader("Los Pokémon con Mayor Puntos de Defensa-Especial")

try:
    conn = sqlite3.connect(db_abs_path)
    cur = conn.cursor()
    cur.execute("""
                SELECT identifier, type, generation, base_experience, Puntos_de_base, max (base_stat)
                FROM limpia_bbdd
                WHERE generation BETWEEN "generation-i" AND "generation-iv" AND Puntos_de_base = "special-defense"
                GROUP BY generation
                ORDER BY max (base_stat) ASC;
                """)
except sqlite3.Error as e:
    print(f"Error: {e}")
    st.error(f"Error: {e}")    


result = cur.fetchall()

conn.close()

df_special_defense = pd.DataFrame (result, columns=['Pokemon', 'Tipo de Pokemon', 'Generacion', 'Cantidad minima de experiencia','Base', 'Puntos de Base'])

fig = px.bar(df_special_defense, x="Pokemon", y="Puntos de Base", color="Generacion", 
             color_discrete_map={'generation-iv': '#2A80C3', 'generation-iii': '#4BABF5', 'generation-i': '#95D0FE', 'generation-ii': '#9FC6E5'}, 
             barmode="stack")

st.dataframe(df_special_defense, width= 1000, hide_index= True)

st.plotly_chart(fig, use_container_width=True)

st.write ("El Pokémon que tiene Mayor Puntos de Defensa-Especial es Shuckle con 230 puntos, este Pokémon pertenece a la 2° generación")

st.image (r'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/213.png', width=400)

#consulta, dataframe y grafico que determina los mejores pokemones segun sus puntos de ataque-especial

st.subheader("Los Pokémon con Mayor Puntos de Ataque-Especial")

try:
    conn = sqlite3.connect(db_abs_path)
    cur = conn.cursor()
    cur.execute("""
                SELECT identifier, type, generation, base_experience, Puntos_de_base, max (base_stat)
                FROM limpia_bbdd
                WHERE generation BETWEEN "generation-i" AND "generation-iv" AND Puntos_de_base = "special-attack"
                GROUP BY generation
                ORDER BY max (base_stat) ASC;
                """)
except sqlite3.Error as e:
    print(f"Error: {e}")
    st.error(f"Error: {e}")    


result = cur.fetchall()

conn.close()

df_special_attack = pd.DataFrame (result, columns=['Pokemon', 'Tipo de Pokemon', 'Generacion', 'Cantidad minima de experiencia','Base', 'Puntos de Base'])

fig = px.bar(df_special_attack, x="Pokemon", y="Puntos de Base", color="Generacion", 
             color_discrete_map={'generation-iv': '#2A80C3', 'generation-iii': '#4BABF5', 'generation-i': '#95D0FE', 'generation-ii': '#9FC6E5'}, 
             barmode="stack")

st.dataframe(df_special_attack, width= 1000, hide_index= True)

st.plotly_chart(fig, use_container_width=True)

st.write ("El Pokémon que tiene Mayor Puntos de Ataque-Especial Mewtwo  con 154 puntos, este Pokémon pertenece a la 1° generación")

st.image (r'https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/150.png', width=400)


# Pregunta 2
with st.container():
    st.write("---")
    st.header("2. ¿Cuál es el Tipo de Pokémon con Mayor Experiencia de Pelea?")

try:
    conn = sqlite3.connect(db_abs_path)
    cur = conn.cursor()
    cur.execute("""
                SELECT type, identifier, base_experience, color, weight / 10 AS weight_divided, height / 10 AS height_divided, generation
                FROM (
                    SELECT type, identifier, base_experience, color, weight, height, generation,ROW_NUMBER() OVER (PARTITION BY type ORDER BY base_experience DESC) AS rank
                    FROM limpia_bbdd
                    WHERE generation BETWEEN 'generation-i' AND 'generation-iv'
                    ) AS subquery
                    WHERE 
                    rank = 1;
                """)
    result = cur.fetchall()  
except sqlite3.Error as e:
    print(f"Error: {e}")
    st.error(f"Error: {e}")
finally:
    conn.close()  

df_tipo_experiencia = pd.DataFrame(result, columns=['Tipo de Pokemon', 'Pokemon', 'Experiencia', 'Color', 'Peso', 'Altura', 'Generacion'])

fig = px.line(df_tipo_experiencia, x="Tipo de Pokemon", y="Experiencia", 
              hover_data=["Generacion", "Tipo de Pokemon", "Pokemon"], 
              color_discrete_sequence=["#760723"])

fig.update_layout(
    xaxis=dict(
        gridcolor='#eee',
        gridwidth=1,
        zeroline=True,  
        showgrid=True  
    ),
    yaxis=dict(
        gridcolor='#eee',
        gridwidth=1,
        zeroline=True,  
        showgrid=True  
    )
)
st.dataframe(df_tipo_experiencia, width=1000, hide_index=True)

st.plotly_chart(fig, use_container_width=True)

# Pregunta 3
with st.container():
    st.write("---")
    st.header("3.	¿Los Pokémon más pesados tienen Menor Velocidad?")

try:
    conn = sqlite3.connect(db_abs_path)
    cur = conn.cursor()
    cur.execute("""
                SELECT identifier, type, generation, weight, Puntos_de_base, base_stat
                FROM limpia_bbdd
                WHERE generation BETWEEN 'generation-i' AND 'generation-iv' AND stat_id = "6"
                ORDER BY base_stat, weight DESC
                LIMIT 10;
                """)
    result = cur.fetchall()  
except sqlite3.Error as e:
    print(f"Error: {e}")
    st.error(f"Error: {e}")
finally:
    conn.close()  

df_peso_velocidad = pd.DataFrame(result, columns=['Pokemon', 'Tipo de Pokemon', 'Generacion', 'Peso', 'Base', 'Puntos de Base'])

fig = px.bar(df_peso_velocidad.assign(Puntos_de_Base_str=df_peso_velocidad["Puntos de Base"].astype(str)), 
             x="Pokemon", y="Peso", color="Puntos_de_Base_str", 
             color_discrete_map={'5': '#6DC83E', '10': '#3C801A', '15': '#102C02'}, 
             barmode="stack")

st.dataframe(df_peso_velocidad, width=1000, hide_index=True)

st.plotly_chart(fig, use_container_width=True)





    
    
    