FROM python:3.11-slim-bullseye

ADD requirements.txt .
ADD entrypoint.sh .

RUN \
	set -ex; \
	python -m venv ve; \
	set +x; \
	. ve/bin/activate; \
	set -x; \
	pip install -U pip; \
	pip install -r requirements.txt

ENTRYPOINT ["entrypoint.sh"]
