CREATE TABLE IF NOT EXISTS album(
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
release date CHECK(release < current_date)
);

CREATE TABLE IF NOT EXISTS ganre(
id serial primary key,
name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS track(
id serial PRIMARY KEY,
name VARCHAR(255) NOT NULL,
length time NOT NULL,
ganre_id integer REFERENCES ganre(id),
album_id integer REFERENCES album(id)
);

CREATE TABLE IF NOT EXISTS country(
id serial PRIMARY KEY,
name varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS artist(
id serial PRIMARY KEY,
name varchar(255) NOT NULL,
birthday date not null check(birthday < current_date),
country_id integer REFERENCES country(id)
);

CREATE TABLE IF NOT EXISTS playlist(
id serial PRIMARY KEY,
name varchar(255) NOT NULL
); 

CREATE TABLE IF NOT EXISTS artists_tracks(
artist_id integer NOT NULL REFERENCES artist(id),
track_id integer NOT NULL REFERENCES track(id),
PRIMARY KEY(artist_id, track_id)
); 

CREATE TABLE IF NOT EXISTS artists_ganres(
artist_id integer NOT NULL REFERENCES artist(id),
ganre_id integer NOT NULL REFERENCES ganre(id),
primary key(artist_id, ganre_id)
);

CREATE TABLE IF NOT EXISTS tracks_playlists(
track_id integer NOT NULL REFERENCES track(id),
playlist_id integer NOT NULL REFERENCES playlist(id),
PRIMARY KEY(track_id, playlist_id)
);