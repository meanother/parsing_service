# Pulse parser


## Run
```shell script
git clone https://github.com/meanother/parsing_service.git; \
cd parsing_service; \
python3 -m venv env; \
source env/bin/activate; \
pip install -r req.txt; \
python main.py
```

## Log
```shell script
tail -f parser-service.log
```

## Result
```sqlite-sql
select * from pulse_parser pp;
```