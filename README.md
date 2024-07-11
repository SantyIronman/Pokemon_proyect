### Readme: Análisis estadístico de Pokémon basado en Base de Datos de Pokémones 

#Pokemon_proyect

Este repositorio contiene un análisis estadístico descriptivo de Pokémon basado en una base de datos estructurada en SQL. A continuación, se presentan respuestas a preguntas específicas sobre diversas variables presentes en la base de datos

### Estructura del Proyecto

1. **Base de Datos**: 
   - La base de datos veekun-pokedex.sql contiene las tablas necesarias para almacenar información relevante sobre Pokémon, incluyendo sus estadísticas base como ataque, defensa, velocidad y nivel de salud.

2. **Análisis por Generación**:
   - Se realizó un análisis exhaustivo para determinar los mejores Pokémon en las primeras 4 generaciones basándose en sus puntos base. Los resultados se presentan detalladamente en los archivos correspondientes.

3. **Relación entre Estadísticas**:
   - Se exploró la relación entre el ataque y la defensa, así como entre la velocidad y el nivel de salud, por las 4 primeras generaciones de Pokémon. Estos análisis ayudan a entender qué combinaciones de estadísticas hacen que un Pokémon sea más efectivo en batalla.

### Requisitos

- Se requiere un servidor de base de datos SQL  como sqlite para ejecutar las consultas incluidas en este repositorio.

### Autor

Este proyecto fue desarrollado por el grupo de recuperación de computación II como parte de un estudio estadístico de análisis de datos de Pokémon.

### Licencia

Este repositorio está bajo libre licencia

---



#Planteamiento del Problema

Desde su introducción en 1996, los Pokémon han capturado la imaginación de millones de personas en todo el mundo. A lo largo de las primeras cuatro generaciones de juegos (Generación I a IV), se han introducido cientos de especies diferentes, cada una con características únicas que definen sus habilidades, estadísticas y tipología. Las personas más fanáticas de esta franquicia prefieren la primera generación de Pokémon aun así viendo Pokémon mejores que la primera generación, entonces es necesario realizar un análisis estadístico para proporcionar una comprensión más profunda de la estructura de los Pokémon a lo largo del tiempo.

###Marco Teórico

Pokémon = Una contracción del japonés Poketto Monsutā, que significa monstruo de bolsillo.

Pokémon es un proyecto que inció con la idea de crear un videojuego agradable para el público de los años 1990 cuando comenzaron a usarse consolas de videojuegos como el famoso “game boy”. En palabras de su creador:

"Diría que cuando comenzamos teníamos fe absoluta en lo que estábamos haciendo y queríamos llevar a los niños la alegría de descubrir criaturas especiales —los Pokémon—, de coleccionarlos, de combatir con ellos y de intercambiarlos: ese era nuestro sueño” – Junichi Masuda.

Los pokémon son criaturas de diferentes tipos y con diferentes habilidades. Actualmente en el universo del videojuego existen más de 800 criaturas ya que con cada generación que pasa esta lista se extiende con aproximadamente +80 pokémon por generación.

En el videojuego los pokémon viven en diferentes hábitats o entre los humanos que los crían y cuidan de ellos (llamados también entrenadores). Durante el transcurso del juego los pokémon adquieren experiencia y evolucionan para convertirse en pokémon más fuertes.

Cada pokémon cuenta con habilidades especiales iguales o diferentes a otros pokémon, para la cuarta generación hay más de 120 diferentes habilidades.

Existen 18 tipos de pokemon y cada pokemon puede ser de uno o dos tipos (Ej: Solo tierra o tierra y eléctrico)

• Normal.
• Lucha.
• Volador.
• Veneno.
• Tierra.
• Piedra.
• Bicho.
• Fantasma.
• Acero.
• Fuego.
• Agua.
• Planta.
• Eléctrico.
• Psíquico.
• Hielo.
• Dragón.
• Oscuro.
• Hada.

En el universo de Pokémon existen 6 Generaciones: 1° Generación de 1996 con 151 Pokémon; 2° Generación de 1999 con 100 Pokémon; 3° Generación de 2002 con 135 Pokémon; 4° Generación de 2006 con 108 Pokémon; 5° Generación de 2010 con 156 Pokémon; 6° Generación de 2013 con 72 Pokémon.



Este README proporciona una visión general del proyecto, detallando el contenido disponible y cómo puede ser utilizado para analizar datos de Pokémon.