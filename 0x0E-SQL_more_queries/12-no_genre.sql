-- Script that lists all shows contained in hbtn_0d_tvshows without genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_shows_genres
ON tv_show.id = tv_show_genre.show_id
WHERE tv_show_genre.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
