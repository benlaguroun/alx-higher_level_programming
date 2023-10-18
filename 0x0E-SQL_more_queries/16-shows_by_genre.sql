-- List all shows and their linked genres

SELECT ts.title AS 'show_title', tg.name AS 'genre_name'
FROM tv_shows AS ts
LEFT JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres AS tg ON tsg.genre_id = tg.id
ORDER BY ts.title ASC, tg.name ASC;
