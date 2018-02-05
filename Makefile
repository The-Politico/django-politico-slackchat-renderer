test:
	pytest -v

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

dev:
	gulp --cwd chatrender/staticapp/

database:
	dropdb chatrender --if-exists
	createdb chatrender
