INSERT INTO country (name)
VALUES ('Австралия'), ('Австрия'), ('Азербайджан'), ('Албания'), ('Алжир'), ... ;
;

insert into ganre(name)
values ('Классическая музыка'), ('Народная музыка'), ('Духовная музыка'), ('Латиноамериканская музыка'),
('Блюз'), ('Ритм-н-блюз'), ('Джаз'), ('Шансон'), ('Романс'), ('Авторская музыка');
;

insert into artist(name, founded, country_id)
values ('XXXTentacion', '2013 ', '160'), ('Аффинаж', '2012', '157'), ('Стрелки', '1997', '157'), ... ;
;

insert into album (name, release)
values ('Тот, кому не нужно счастье', '2021'),
('Bad Vibes Forever', '2019'),
('Мимо. Ранен. Убит', '2020'), ... 

insert into playlist (name)
values ('Отечественная музыка'), 
('Зарубежная музыка'), 
('Хорошая музыка'), ...  
;

insert into track (name, length, ganre_id , album_id)
values ('Ветер, который дует с полей', '3:37', '13', '2'),
('bad vibes forever', '2:30', '14', '3'),
('I Changed Her Life', '1:48', '14', '3'),
('Такси', '3:20', '15', '4'),
('Хостел', '5:24', '15', '4'), ... 
;

insert into artists_ganres (artist_id, ganre_id)
values ('3', '17'),
('4', '14'),
('5', '15'), ... 
;

insert into artists_tracks (artist_id, track_id)
values('3', '2'), ('3', '3'),
('4', '4'), ('4', '5'), ... 
;

insert into tracks_playlists (track_id, playlist_id)
values ('2', '1'), ('2', '3'), ('2', '7'), ...
;
