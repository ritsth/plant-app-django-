release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input

web: gunicorn contactsapi.wsgi
web: python PlantWebApp/manage.py runserver 0.0.0.0:$localhost
