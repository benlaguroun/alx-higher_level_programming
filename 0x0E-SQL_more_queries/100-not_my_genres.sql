-- List all genres not linked to the show 'Dexter'

SELECT tg.name AS 'genre_name'
FROM tv_genres AS tg
LEFT JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
LEFT JOIN tv_shows AS ts ON tsg.show_id = ts.id
WHERE ts.title IS NULL OR ts.title <> 'Dexter'
GROUP BY genre_name
ORDER BY genre_name ASC;
