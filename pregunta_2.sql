--¿Cuáles son las 10 habilidades más comunes en el universo de Pokémon
CREATE VIEW Pregunta_2 AS
SELECT 
	count(pokemon_abilities.pokemon_id) AS "Total_Pokemon",
	ability_names.name As "Habilidad"
FROM pokemon_abilities
LEFT JOIN ability_names ON pokemon_abilities.ability_id = ability_names.ability_id
GROUP BY ability_names.name
HAVING ability_names.local_language_id = "7"
ORDER BY Total_Pokemon DESC
LIMIT 10;