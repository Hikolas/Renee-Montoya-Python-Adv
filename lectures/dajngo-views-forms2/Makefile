
migrations:
	@docker exec -it -w /trello trello_api python src/manage.py makemigrations

migrate:
	@docker exec -it -w /trello trello_api python src/manage.py migrate

app:
	@mkdir -p src/apps/$(name)
	@docker exec -it -w /trello trello_api python src/manage.py startapp $(name) src/apps/$(name)

start_compose:
	@docker-compose -f docker-compose-dev.yml up

test_env:
	@cat ./docker/envs/env_example > ./docker/envs/.env-local

test:
	@docker exec -it -w /trello trello_api pytest --ds=src.config.settings.test tests

test_user:
	@docker exec -it -w /trello trello_api python src/manage.py createsuperuser

shell:
	@docker exec -it -w /trello trello_api python src/manage.py shell

bash:
	@docker exec -it -w /trello trello_api bash

collectstatic:
	@docker exec -it -w /trello trello_api python src/manage.py collectstatic