all: run

run: 
	python3 src/main.py c

testz:
	python3 src/test.py

test-json:
	python3 src/main.py j ../test/${TEST}