# Verwende das offizielle Python-Image als Basis
FROM python:3.9

# Setze das Arbeitsverzeichnis im Container
WORKDIR /getOutside_backend

# Kopiere die Anforderungen in das Arbeitsverzeichnis
COPY requirements.txt /getOutside_backend/

# Installiere die Anforderungen
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den Rest des Codes in das Arbeitsverzeichnis
COPY . /getOutside_backend/

#Sqlite database
COPY db.sqlite3 /getOutside_backend/


# Setze die Umgebungsvariable für die Produktionsumgebung (optional)
ENV DJANGO_SETTINGS_MODULE=myproject.settings.production

# Führe die Migrationsbefehle aus (optional)
RUN python manage.py migrate

# Öffne den Port, den die Django-Anwendung verwendet
EXPOSE 8000

# Starte den Django-Entwicklungsserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
