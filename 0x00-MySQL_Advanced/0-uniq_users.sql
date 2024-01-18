--creates table users
--with attributes id, email, name
CREATE TABLE IF NOT EXISTS users(
	id int PRIMARY KEY AUTO_INCREMENT NOT NULL,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255)
);
