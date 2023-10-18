-- List all cities in the database

SELECT c.id AS city_id, c.name AS city_name, s.name AS state_name
FROM cities AS c
LEFT JOIN states AS s ON c.state_id = s.id
ORDER BY c.id;
