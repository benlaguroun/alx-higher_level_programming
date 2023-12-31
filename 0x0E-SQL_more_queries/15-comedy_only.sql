-- List all Comedy shows

SELECT ts.title AS 'show_title'
FROM tv_shows AS ts
JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
JOIN tv_genres AS tg ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy'
ORDER BY show_title ASC;
