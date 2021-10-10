install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C simmarket.py

test:
	python -m pytest -vv --cov=simmarket test_simmarket.py

