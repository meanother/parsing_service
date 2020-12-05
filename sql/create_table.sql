create table pulse_parser(
    id integer primary key,
    ticker varchar(50) not null,
    post_date timestamp not null,
    post_date_utc timestamp not null,
    hashtags varchar(255) null,
    cursor NUMERIC not null,
    comments int not null,
    likes int not null,
    username varchar(255) not null,
    text blob null,
    instruments varchar(500) null,
    parse_time timestamp not null
);
