FROM python:3.10.9

COPY requirements.txt /tmp/requirements.txt

RUN python -m pip install --timeout 300000 -r /tmp/requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 3000

CMD ["streamlit", "run",  'main.py', "0.0.0.0", " --port", "3000"]