build:
	docker-compose build {{cookiecutter.project_slug}}

install-coreui:
	cd {{cookiecutter.project_slug}}/static/coreui && npm install

run:
	python3 manage.py runserver 0.0.0.0:8000

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

collectstatic:
	python3 manage.py collectstatic --noinput

createsuperuser:
	echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com', 'lQ228uqA6Hy6uL4gj1Bj');" | python3 manage.py shell