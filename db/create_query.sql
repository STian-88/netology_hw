create table if not exists ganre(
id serial primary key,
name varchar(266),
description text
);

create table if not exists artist(
id serial primary key,
name varchar(255),
birthday date,
country varchar(255)
);

create table if not exists artist_ganre(
artist_id integer references artist(id),
ganre_id integer references ganre(id)
);

create table if not exists album(
id serial primary key,
name varchar(255),
release date
);

create table if not exists artist_ulbum(
artist_id integer references artist(id),
album_id integer references album(id)
);

create table if not exists mix_tape(
id serial primary key,
name varchar(255),
release date
);

create table if not exists track(
id serial primary key,
name varchar(255),
album integer references album(id),
mix_tape integer references mix_tape(id),
length integer not null
);