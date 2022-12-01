create table reference (
    id serial primary key,
    type text
);

create table book (
    id serial primary key,
    book_id integer references reference,
    keyword text unique,
    author_surname text,
    author_name text,
    title text,
    year text,
    publisher text
);