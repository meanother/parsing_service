# Pulse parser


## Initialize
```shell script
git clone https://github.com/meanother/parsing_service.git; \
cd parsing_service; \
python3 -m venv env; \
source env/bin/activate; \
pip install -r req.txt
```

### Run pulse parser
```shell script
python run_pulse.py
```

### Run openinsider parser
```shell script
python run_openisider.py
```

## Log
```shell script
tail -f parser-service.log
tail -f openinsider-service.log
```

## Result
```sqlite-sql
select * from pulse_parser pp;
select * from openinsider os;
```