FROM python:3.9-slim-buster AS compile-image
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

RUN python -m venv /opt/venv
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

FROM python:3.9-slim-buster AS build-image
COPY --from=compile-image /opt/venv /opt/venv
COPY src/ .
# Make sure we use the virtualenv:
ENV PATH="/opt/venv/bin:$PATH"
CMD ["gunicorn", "--bind=0.0.0.0:5000","-w 4", "server:app"]