-- название и год выхода альбомов, вышедших после 2018 года
select name, release from album
where release > 2018;

-- название и продолжительность самого длительного трека;
select name, length from track
where length = (select max(length) from track);


-- название треков, продолжительность которых не менее 3,5 минуты;
select name, length from track
where length < '03:00';

-- названия альбомов, вышедших в период с 2000 по 2022 год включительно;
select name from album
where release between 2000 and 2022;

-- исполнители, чье имя состоит из 1 слова;
select name from artist 
where name not like '% %';

-- название треков, которые содержат слово "я"/"i";
select name from track
where name ilike '%я%' or name ilike '%i%';
