CREATE TABLE masters (id integer PRIMARY KEY, name text NOT NULL UNIQUE, style text);
INSERT INTO masters (name, style) VALUES
    ('Master Po Ping', 'Improvised and Panda Kung Fu'),
    ('Master Shifu', 'Red Panda Kung Fu'),
    ('Grand Master Oogway', 'Shaolinquan and T''ai chi ch''uan'),
    ('Master Tigress', 'Black Tiger Kung Fu'),
    ('Master Viper', 'Viper Kung Fu'),
    ('Master Monkey', 'Monkey Kung Fu'),
    ('Master Mantis', 'Southern Praying Mantis Kung Fu'),
    ('Master Crane', 'Fujian White Crane Kung Fu');
