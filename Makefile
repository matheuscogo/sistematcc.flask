clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	rm -rf .cache
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf htmlcov
	rm -rf .tox/
	rm -rf docs/_build
	rm -rf .pytest_cache
	rm -rf SistemaTCC.egg-info
	pip install -e .[dev] --upgrade --no-cache

install:
	pip install -e .['dev']

purge:
	pip uninstall -e .['dev']

venv:
	python3 -m venv venv
	source venv/bin/activate

test:
	FLASK_ENV=test pytest tests/ -v --cov=sistemaTCC

run:
	export FLASK_APP=sistemaTCC/app.py
	export FLASK_ENV=development
	flask run --host=192.168.5.1

