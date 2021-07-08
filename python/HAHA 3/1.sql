CREATE TABLE books(
    isbn VARCHAR(200) NULL,
	title VARCHAR(600) NULL,
	subtitle VARCHAR(500) NULL,
	author VARCHAR(200) NULL,
	published DATETIME NULL,
	publisher VARCHAR(200) NULL,
	pages INT NULL,
	description TEXT NULL,
	website VARCHAR(500) NULL
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;




SELECT title,published FROM books
WHERE published LIKE '%2014%';



