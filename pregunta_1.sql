--¿Cuál es el promedio, valor minimo, valor maximo en punto base de los Pokemon segun su generacion?
CREATE VIEW Pregunta_1 AS
SELECT
	generations.identifier AS "Generaciones",
	stats.identifier AS "Puntos_de_Base",
	count (pokemon_species.generation_id) AS "Total_de_Pokemon",
	min(pokemon_stats.base_stat) AS "Valor_Minimo",
	max(pokemon_stats.base_stat) AS "Valor_Maximo",
	round (avg(pokemon_stats.base_stat), 2) AS "Promedio" 
FROM pokemon_stats
LEFT JOIN pokemon_species ON pokemon_stats.pokemon_id = pokemon_species.id
LEFT JOIN generations ON pokemon_species.generation_id = generations.id
LEFT JOIN stats ON pokemon_stats.stat_id = stats.id
GROUP BY pokemon_stats.stat_id, "Generaciones"
HAVING "Generaciones" IS NOT NULL;