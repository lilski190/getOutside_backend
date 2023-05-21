FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

WORKDIR /getOutside_backend

COPY requirements.txt /getOutside_backend/

ADD . /getOutside_backend/

RUN pip install -r requirements.txt

#EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
