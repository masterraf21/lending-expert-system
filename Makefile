all: run

run: 
	python3 src/main.py c

web:
	python3 src/main.py w

web-prod:
	python3 src/main.py w prod

testz:
	python3 src/test.py

json:
	python3 src/main.py j ../test/${TEST}