isort-src:
	isort ./Eureka ./tests

isort-docs:
	isort ./docs/src -o Eureka

isort-examples:
	isort ./examples -o Eureka -p app

format: isort-src isort-docs isort-examples
	black .

lint:
	flake8 ./Eureka ./tests

test:
	pytest --cov=Eureka/ --cov-report=term-missing --cov-fail-under=100