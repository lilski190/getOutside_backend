# Verwende das offizielle Python-Image als Basis
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED 1

# Setze das Arbeitsverzeichnis im Container
WORKDIR /getOutside_backend

# Kopiere die Anforderungen in das Arbeitsverzeichnis
COPY requirements.txt /getOutside_backend/

# Kopiere den Rest des Codes in das Arbeitsverzeichnis
ADD . /getOutside_backend/

# Installiere die Anforderungen
RUN pip install -r requirements.txt


# Öffne den Port, den die Django-Anwendung verwendet
#EXPOSE 8000

# Starte den Django-Entwicklungsserver
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
