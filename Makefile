lint:
	flake8 ./internal ./src ./tests

test:
	pytest ./tests