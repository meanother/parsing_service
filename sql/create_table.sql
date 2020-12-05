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

/*
my_data = {
    'ticker': ticker,
    'inserted': i['inserted'],
    'HashTags': ', '.join(re.findall(r'#\w+', i['text'], re.MULTILINE | re.DOTALL)),
    'datetime': datetime.strptime(i['inserted'][:-6], '%Y-%m-%dT%H:%M:%S.%f').strftime("%Y-%m-%d %H:%M:%S"),
    'datetime_': datetime.strptime(i['inserted'], '%Y-%m-%dT%H:%M:%S.%f%z').replace(tzinfo=timezone('utc')).strftime("%Y-%m-%d %H:%M:%S"),
    'nextCursor': data.json()['payload']['nextCursor'],
    'Comments': i['commentsCount'],
    'Likes': i['likesCount'],
    'Name': i['nickname'],
    'Text': i['text'],
}
*/