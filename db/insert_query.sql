insert into ganre(name, description)
values('metal', 'Heavy metal evolved in from hard rock, psychedelic rock, 
and blues rock in late 1960s and 1970s with notable acts such as Black Sabbath, 
Judas Priest and Motörhead. The popularity of heavy metal soared in the 1980s with bands such as Iron Maiden, 
Metallica and Guns n Roses. It has a rougher style and heavier sound than other forms of rock music, 
with notable subgenres such as thrash metal, death metal and black metal.'
);

insert into ganre(name, description)
values('Rock', 'Rock music is a broad genre of popular music that originated as "rock and roll" in the United States in the late 1940s and early 1950s, 
developing into a range of different styles in the mid-1960s and later, particularly in the United States and the United Kingdom.'
);

insert into ganre(name, description)
values('Jazz', 'Jazz is a music genre that originated in the African-American communities of New Orleans, 
Louisiana, United States, in the late 19th and early 20th centuries, with its roots in blues and ragtime.'
);

insert into ganre(name, description)
values('Electronic', 'Electronic music is music that employs electronic musical instruments, 
digital instruments, or circuitry-based music technology in its creation. 
Contemporary electronic music includes many varieties and ranges from experimental art music to popular forms such as electronic dance music (EDM).'
);

insert into ganre(name, description)
values('Pop ', 'Pop is a genre of popular music that originated in its modern form during the mid-1950s in the United States and the United Kingdom. 
The terms popular music and pop music are often used interchangeably, 
although the former describes all music that is popular and includes many disparate styles.'
);

insert into artist (name, birthday, country)
values ('Bruce the Shark', '01.01.2010', 'Russia'),
('Bob Parr (Mr. Incredible)', '02.02.2012', 'USA'),
('Nemo', '01.01.2010', 'Netherlands'),
('Remy', '14.10.1956', 'Italy'),
('Sulley Sullivan', '24.09.1972', 'Moldova'),
('Mike Wazowski', '18.08.2001', 'Vatican'),
('Merida', '05.07.2005', 'Scotland'),
('Joy', '05.05.2015', 'Inside Out')

insert into mix_tape (name, release)
values 
('Best metall tracks', '01.06.2021'),
('Best tracks ever', '06.08.2030'),
('My favorite tracks', '04.12.2022'),
('Это репчик, чувак', '14.10.1952'),
('For train', '21.11.2010'),
('For sleep', '01.06.2001'),
('For my wedding', '20.07.1927'),
('Hits', '01.12.2025'),

insert into album (name, release)
values 
('First love', '01.01.2001'),
('Second love', '02.02.2002'),
('Last love', '03.03.2003'),
('My love', '04.04.2004'),
('With love', '05.05.2005'),
('For love', '06.06.2006'),
('Love in mi hart', '07.07.2007'),
('About love', '08.08.2008');

insert into track (name, album, mix_tape, length)
values ('one', '1', '8', '180'),
('two', '2', '7', '260'),
('three', '3', '6', '186'),
('four', '4', '5', '187'),
('five', '5', '4', '183'),
('six', '6', '3', '183'),
('seven', '7', '2', '189'),
('eight', '8', '1', '240'),
('nine', '1', '8', '245'),
('ten', '2', '7', '163'),
('eleven', '3', '6', '134'),
('twelve', '4', '5', '246'),
('thirteen', '5', '4', '247'),
('fourteen', '6', '3', '249'),
('fifteen', '7', '2', '123'),
('sixteen', '8', '1', '154');

insert into artist_ganre (artist_id, ganre_id)
values 
('1', '1'),
('2', '1'),
('3', '1'),
('4', '2'),
('5', '2'),
('6', '3'),
('7', '4'),
('8', '3'),
('1', '4'),
('1', '2'),
('8', '1'),
('8', '2'),
('4', '1'),
('3', '5'),
('6', '5'),
('8', '5'),
('5', '5');

insert into artist_ulbum (artist_id, album_id)
values 
('1', '1'),
('2', '2'),
('3', '3'),
('4', '4'),
('5', '5'),
('6', '6'),
('7', '7'),
('1', '2'),
('1', '3'),
('1', '4'),
('8', '1'),
('8', '7');

insert into artist_mix_tape (artist_id, mix_tape_id)
values 
('1', '1'),
('2', '2'),
('3', '3'),
('4', '4'),
('5', '5'),
('6', '6'),
('7', '7'),
('8', '8'),
('1', '8'),
('2', '7'),
('3', '6'),
('4', '5'),
('5', '4'),
('6', '3');