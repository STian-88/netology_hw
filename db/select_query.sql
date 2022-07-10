-- название и год выхода альбомов, вышедших после 2003 года
select name, release from ulbum
where date_part('year', release) > 2003

-- название и продолжительность самого длительного трека;
select name,round(length_sec / 60., 1) from track
where length_sec = (select max(length_sec) from track);

-- название треков, продолжительность которых не менее 3,5 минуты;
select name from track 
where round(length_sec / 60., 1) > 3.5;

-- названия сборников, вышедших в период с 2000 по 2022 год включительно;
select name from mix_tape
where date_part('year', release) between 2000 and 2022;

-- исполнители, чье имя состоит из 1 слова;
select name from artist 
where name not like '% %';

-- название треков, которые содержат слово "мой"/"my";
select name from track 
where name like '%мой%' or name like '%my%';
