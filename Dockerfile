FROM python:3
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["bash", "-c", "uwsgi --http 0.0.0.0:8000 --wsgi-file myapp.py --callable app --py-autoreload 1"]
