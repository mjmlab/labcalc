## Makefile to intall `labcalc` in the path and run the test script

install:
	python setup.py install

test:
	py.test --cov=./ labcalc/tests
