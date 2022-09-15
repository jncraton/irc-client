all: test

test:
	python3 -m doctest irc.py

clean:
	rm -rf __pycache__
