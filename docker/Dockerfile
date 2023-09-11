FROM python:3.11-slim-bullseye

ADD requirements.txt .

RUN \
	set -e; \
	# create virtual environment
	python -m venv ve; \
	# update pip, setuptools
	ve/bin/pip install -U pip setuptools; \
	# install requirements
	ve/bin/pip install -r requirements.txt

ADD analysis.py .

ENTRYPOINT ["/ve/bin/python", "/analysis.py"]
