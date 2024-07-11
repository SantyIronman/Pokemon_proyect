--¿Cuántos y sus puntos base de los Pokémon hay en cada habitats?
CREATE VIEW Pregunta_5 AS
SELECT 
	pokemon_habitats.identifier AS "Habitats", 
	stats.identifier AS "Puntos_de_Base",
	count(pokemon_types.type_id) AS "Total_de_Pokemon",
	min(pokemon_stats.base_stat) AS "Minimo_de_Puntos",
	max(pokemon_stats.base_stat) AS "Maximo_de_Puntos",
	round(avg(pokemon_stats.base_stat), 2) AS "Promedio_de_Puntos"
FROM pokemon_stats
LEFT JOIN pokemon_species ON pokemon_stats.pokemon_id = pokemon_species.id
LEFT JOIN stats ON pokemon_stats.stat_id = stats.id
LEFT JOIN pokemon_habitats ON pokemon_species.habitat_id = pokemon_habitats.id
LEFT JOIN pokemon_types ON pokemon_stats.pokemon_id = pokemon_types.pokemon_id
GROUP BY pokemon_habitats.identifier;