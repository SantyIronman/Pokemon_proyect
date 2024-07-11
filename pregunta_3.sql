--Promedio, valor minimo, valor maximo de los puntos de base según el tipo de Pokémon que sean bebé 
CREATE VIEW Pregunta_3 AS
SELECT
	types.identifier AS "Tipo",
	stats.identifier AS "Puntos_de_Base",
	count(pokemon_types.type_id) AS "Total_de_Pokemon",
	min(pokemon_stats.base_stat) AS "Minimo_de_Puntos",
	max(pokemon_stats.base_stat) AS "Maximo_de_Puntos",
	avg(pokemon_stats.base_stat) AS "Promedio_de_Puntos"
FROM pokemon_stats
LEFT JOIN pokemon_types ON pokemon_stats.pokemon_id = pokemon_types.pokemon_id
LEFT JOIN types ON pokemon_types.type_id = types.id
LEFT JOIN stats ON pokemon_stats.stat_id = stats.id
LEFT JOIN pokemon_species ON pokemon_species.id = pokemon_types.pokemon_id
WHERE pokemon_species.is_baby = "1"
GROUP BY types.identifier,stats.identifier;