pyclean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

migrate: pyclean
	env PYTHONPATH=. LOG_LEVEL=ERROR alembic upgrade head

downgrade: pyclean
	env PYTHONPATH=. LOG_LEVEL=ERROR alembic downgrade -1

miggen: pyclean
	env FLASK_APP=cli.py LOG_LEVEL=ERROR flask migrate-new $(name)

local:
    docker-compose -f docker-compose-local.yml up --build

run:
	docker-compose -f docker-compose-prod.yml up --build

install:
	pip install -r requirements.txt

clean: clean
	docker-compose -f docker-compose-local.yml down
	docker-compose -f docker-compose-local.yml rm
