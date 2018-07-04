init:
	pip install -r requirements.txt

dev:
	sudo pip install -e .

test:
	py.test tests

.PHONY: init test
