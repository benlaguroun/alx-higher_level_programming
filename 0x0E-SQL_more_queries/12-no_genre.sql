-- List all TV shows without a linked genre

SELECT s.title AS show_title, COALESCE(g.genre_id, '') AS genre_id
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g ON s.id = g.show_id
WHERE g.genre_id IS NULL
ORDER BY s.title ASC, genre_id ASC;
