all: test

test:
	python3 -m doctest client.py

clean:
	rm -rf __pycache__
