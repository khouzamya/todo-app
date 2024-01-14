FROM python:3.11
WORKDIR /app
COPY . /app
RUN pip install -r req.txt
ENV DJANGO_SUPERUSER_USERNAME=demo
ENV DJANGO_SUPERUSER_PASSWORD=Test@12345
ENV DJANGO_SUPERUSER_EMAIL=demo@todo.com
RUN DJANGO_SECRET_KEY=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())") \
    && echo "DJANGO_SECRET_KEY =${DJANGO_SECRET_KEY}" > .env
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py createsuperuser --no-input

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]