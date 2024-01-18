--creates table users
CREATE TABLE IF NOT EXISTS users(
	id int AUTO_INCREMENT PRIMARY KEY,
	email varchar(255) NOT NULL,
	name varchar(255)
);
