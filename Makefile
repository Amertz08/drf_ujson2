
install:
	@pip install \
	--force-reinstall \
	.[dev]

test:
	@python -m pytest

dist:
	@python setup.py sdist bdist_wheel

upload:
	@twine upload dist/*

clean:
	@rm -rf \
	dist/ \
	build/ \
	.tox/ \
	.pytest_cache
