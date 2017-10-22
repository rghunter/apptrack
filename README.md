## Develop

Startup the database with `docker compose up -d db`
Run migrations with `docker-compose run apptrack python manage.py migrate`
start apptrack `docker-compose up -d apptrack`

PSQL into the databse: `docker-compose exec db psql -U postgres apptrack`
