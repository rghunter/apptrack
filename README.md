## Develop

Startup the database with `docker compose up -d db`
Run migrations with `docker-compose run apptrack python manage.py migrate`
start apptrack `docker-compose up -d apptrack`

PSQL into the databse: `docker-compose exec db psql -U postgres apptrack`

On startup, you will need to create an admin user: `docker compose run apptrack python manage.py createsuperuser`

Once the application has started up, it can be reached at: http://127.0.0.1:8000/apptrack/

## Heroku

Setting the default app for the heroku cli requires adding the heroku git repo to your git remotes: `git remote add heroku git@heroku.com:bts-scholarship.git`
Running heroku database migraions: `heroku run --app bts-scholarship python manage.py migrate`
