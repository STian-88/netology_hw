-- 1 - Количесвто исполнителей в каждом жанре:
SELECT  ganre_name, count(artist_id) 
FROM artists_ganres ag
FULL JOIN  ganre g ON ag.ganre_id = g.ganre_id
GROUP BY ganre_name
ORDER BY ganre_name;

-- 2 - Количесвто треков вошедших в альбомы 2019 - 2020 годов:
SELECT count(track_name) 
FROM album a 
LEFT JOIN track t ON t.album_id = a.album_id
WHERE a.album_release BETWEEN 2019 AND 2020 ;

-- 3 - Средняя продолжительность треков по каждому альбому:
SELECT  album_name, date_trunc('seconds', avg(track_length)) AS average_track_length 
FROM track AS t 
LEFT JOIN album AS a ON t.album_id = a.album_id
GROUP BY a.album_name;

-- 4 - Все исполнители, которые не выпустили пльбомы в 2020 году:
SELECT DISTINCT artist_name
FROM artist AS a
LEFT JOIN artists_tracks AS at2 ON at2.artist_id = a.artist_id 
LEFT JOIN track AS t ON at2.track_id = t.track_id 
LEFT JOIN album AS a2 ON t.album_id = a2.album_id 
WHERE a2.album_release != 2020;

-- 5 - Название сборников, в которых присутствует конкретный исполнитель:
SELECT playlist_name 
FROM tracks_playlists AS tp 
JOIN playlist AS p on tp.playlist_id = p.playlist_id
JOIN artists_tracks AS at2 on tp.track_id = at2.track_id 
JOIN artist AS a on at2.artist_id = a.artist_id
WHERE a.artist_id = 3;

-- 6 - Название альбомов, в которых присутствуют исполнители более одного жанра:
SELECT DISTINCT album_name 
FROM album AS a
LEFT JOIN track AS t ON t.album_id = a.album_id 
LEFT JOIN artists_tracks AS at2 ON at2.track_id = t.track_id 
LEFT JOIN artist AS a2 ON at2.artist_id = a2.artist_id 
WHERE a2.artist_name IN (
    SELECT artist_name
    FROM artist AS a
    LEFT JOIN artists_ganres AS ag ON ag.artist_id = a.artist_id 
    LEFT JOIN ganre AS g ON ag.ganre_id = g.ganre_id
    GROUP BY artist_name
    HAVING count(g.ganre_id) > 1);

-- 7 - Наименование треков, которые не входят в сборники:
SELECT track_name 
FROM track AS t
LEFT JOIN tracks_playlists AS tp ON t.track_id = tp.track_id
WHERE tp.track_id IS NULL;

-- 8 - Исполнитель, написавший самый короткий по продолжительности трек:
SELECT artist_name 
FROM artist AS a
LEFT JOIN artists_tracks AS at2 ON at2.artist_id = a.artist_id 
LEFT JOIN track AS t ON at2.track_id = t.track_id
WHERE t.track_length = (
    SELECT min(track_length)
    FROM track);

-- 9 - Альбомы, содержащие наименьшее количесвто треков:
SELECT album_name 
FROM album AS a
LEFT JOIN track AS t ON t.album_id = a.album_id
GROUP BY album_name 
HAVING  count(t.track_id) = (
    SELECT count(track_id) FROM track AS t
    GROUP BY album_id
    ORDER BY count(track_id)
    LIMIT 1);