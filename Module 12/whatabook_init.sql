/*
    Title: whatabook.init.sql
    Author: Jessica Harman
    Date: 25 September 2022
*/

CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

INSERT INTO store(locale)
    VALUES('123 Sesame Street, NY, NY 00000');

INSERT INTO book(book_name, author, details)
    VALUES('Count With Me', 'The Count', 'Counting Book');

INSERT INTO book(book_name, author, details)
    VALUES('Alphabet Book', 'Big Bird', 'A book with letters');

INSERT INTO book(book_name, author, details)
    VALUES('Be a Good Friend', 'Big Bird', "A book about friendship");

INSERT INTO book(book_name, author)
    VALUES('The Cookie Bookie', 'Cookie Monster');

INSERT INTO book(book_name, author)
    VALUES('Be Kind', 'Maria');

INSERT INTO book(book_name, author)
    VALUES("People in Your Neighborhood", 'Bob');

INSERT INTO book(book_name, author)
    VALUES('123, 456, 789 Lady Bug Picnic', 'Lady Bug');

INSERT INTO book(book_name, author)
    VALUES('Helping Out', 'Gordon');

INSERT INTO book(book_name, author)
    VALUES('Goldfish Care', 'Elmo');

INSERT INTO user(first_name, last_name) 
    VALUES('Jane', 'Austen');

INSERT INTO user(first_name, last_name)
    VALUES('Anne', 'Bronte');

INSERT INTO user(first_name, last_name)
    VALUES('George', 'Elliot');

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jane'), 
        (SELECT book_id FROM book WHERE book_name = 'Be Kind')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Anne'),
        (SELECT book_id FROM book WHERE book_name = 'The Cookie Bookie')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'George'),
        (SELECT book_id FROM book WHERE book_name = 'Helping Out')
    );
