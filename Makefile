# @see http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.DEFAULT_GOAL := help
.PHONY: help
help: ## provides cli help for this makefile (default)
	@grep -E '^[a-zA-Z_0-9-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: ci
ci : lint tests ## run continuous integration process

.PHONY: coverage
coverage: coverage_run coverage_html ## output the code coverage in htmlcov/index.html

coverage_run:
	poetry run coverage run -m unittest discover "tests"

coverage_html:
	poetry run coverage html
	@echo "$ browse htmlcov/index.html"

.PHONY: lint
lint: ## run pylint
	poetry run pylint --rcfile=.pylintrc src

.PHONY: tests
tests: tests_units tests_acceptances ## run automatic tests

.PHONY: tests_units
tests_units: ## run only unit tests
	poetry run pytest "tests/units"

.PHONY: tests_acceptances
tests_acceptances: ## run only acceptance tests
	poetry run pytest "tests/acceptances"
