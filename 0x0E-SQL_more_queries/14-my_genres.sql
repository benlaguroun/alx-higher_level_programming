-- List all genres for the show 'Dexter'

SELECT DISTINCT tg.name AS 'genre'
FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
JOIN tv_genres tg ON tsg.genre_id = tg.id
WHERE ts.title = 'Dexter'
ORDER BY tg.name ASC;
