SHELL := /bin/bash
clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf buildgit
	rm -rf dist
	rm -rf *.egg-info 
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf .pytest_cache
	rm -rf SistemaTCC.egg-info
	pip install -e .[dev] --upgrade --no-cache

purge:
	pip uninstall -e .['dev']

SHELL := /bin/bash
db:
	@( \
		source venv/bin/activate; \
		pip install -e .[dev] --upgrade --no-cache; \
		sqlite_web sistemaTCC/sistemaTCC.db; \
	)

SHELL := /bin/bash
flask:
	@( \
		source venv/bin/activate; \
		pip install -e .[dev] --upgrade --no-cache; \
		FLASK_APP=sistemaTCC/app.py FLASK_ENV=development flask run; \
	)

