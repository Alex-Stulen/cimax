makemigrations:
	sudo docker-compose exec backend python manage.py makemigrations

migrate:
	sudo docker-compose exec backend python manage.py migrate

createsuperuser:
	sudo docker-compose exec backend python manage.py createsuperuser

collectstatic:
	sudo docker-compose exec backend python manage.py collectstatic --no-input

backendshell:
	sudo docker-compose exec -it backend sh

dbshell:
	sudo docker-compose exec -it db sh

nginxshell:
	sudo docker-compose exec -it backend_nginx sh
