# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Step 1: Install coreui theme

`make install-coreui`

## Step 2: Install requirements

`pip3 install -r requirements.txt`

## Step 3: Run

- with docker: `docker-compose up -d`

- without docker: `make run`

## Create new app
```
./startapp.sh <app_name>
```

## Utils commands

```
# remove all migration files
make remove-all-migrations

# remove all tables in database
python3 manage.py reset_db

# show all urls
python3 manage.py show_urls

```