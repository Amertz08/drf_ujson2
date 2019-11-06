
install:
	@pip install \
	--force-reinstall \
	.[dev]

test:
	@python setup.py test

dist:
	@python setup.py sdist bdist_wheel

clean:
	@rm -rf \
	dist/ \
	build/ \
	.tox/ \
	.pytest_cache
