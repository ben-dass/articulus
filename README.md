# Articulus

Create articles and measure words written!

## First Steps

```bash
brew install pipx
pipx install poetry

# This should automatically put you in the virtual environment.
# Make sure to add Django or any other depencendies to the pyproject.toml file.
poetry install

# Troubleshooting
poetry env list
poetry env info
poetry env remove <environment-name-as-listed>
```

## Poetry commands

```bash
# Creating a project
poetry run django-admin startproject <project-name> .

# Creating an app
poetry run django-admin startapp app

# Running Django app
poetry run python manage.py runserver

# Migrations
poetry run python manage.py migrate

# Create super user
poetry run python manage.py createsuperuser
```

## Using venv instead of poetry

```bash
# Create a virtual environment.
python3 -m venv .venv

source venv/bin/activate
# or
venv-enter

# Ensure Django is installed in the virtual environment.
python -m pip install Django

deactivate
# or
venv-exit
```

### Aliases

```bash
alias venv-enter="source .venv/bin/activate"
alias venv-exit="deactivate"
```
