create table IF NOT EXISTS pulse_parser(
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


create table IF NOT EXISTS openinsider(
    id integer primary key,
    x varchar(10) null,
    filing_date timestamp null,
    trade_date date null,
    ticker varchar(50) null,
    insider_name varchar(255) null,
    insider_title varchar(255) null,
    trade_type varchar(50) null,
    price_raw varchar(50) null,
    price_formatted DECIMAL(10,5) null,
    qty varchar(50) null,
    owned_raw varchar(255) null,
    owned_formatted int null,
    own varchar(50) null,
    value_raw varchar(255) null,
    value_formatted int null,
    one_d varchar(50) null,
    one_w varchar(50) null,
    one_m varchar(50) null,
    six_m varchar(50) null,
    parse_time timestamp not null
);
