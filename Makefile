lint:
	flake8 ./internal ./src ./tests

test:
	pytest --cov=Eureka ./tests