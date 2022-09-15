all: test

test:
	python3 -m doctest client.py
