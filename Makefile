lint:
	@echo "Running linter flake8" & flake8 ./internal ./src ./tests

test:
	@echo "Running test" & pytest --cov ./tests

all: lint test