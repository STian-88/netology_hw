create table if not exists album(
id serial primary key,
name varchar(255) not null,
release date check(release < current_date)
);

create table if not exists ganre(
id serial primary key,
name varchar(255) unique not null
);

create table if not exists track(
id serial primary key,
name varchar(255) not null,
length time not null,
ganre_id integer references ganre(id),
album_id integer references album(id)
);

create table if not exists country(
id serial primary key,
name varchar(255) not null
);

create table if not exists artist(
id serial primary key,
name varchar(255) not null,
birthday date not null check(birthday < current_date),
country_id integer references country(id)
);

create table if not exists playlist(
id serial primary key,
name varchar(255) not null
); 

create table if not exists artists_tracks(
artist_id integer not null references artist(id),
track_id integer not null references track(id),
primary key(artist_id, track_id)
); 

create table if not exists artists_ganres(
artist_id integer not null references artist(id),
ganre_id integer not null references ganre(id),
primary key(artist_id, ganre_id)
);

create table if not exists tracks_playlists(
track_id integer not null references track(id),
playlist_id integer not null references playlist(id),
primary key(track_id, playlist_id)
);