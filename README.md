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
poetry-runserver
poetry-makemigrations
poetry-migrate
poetry-shell
poetry-test
poetry-createsuperuser
poetry-startapp <app-name>
poetry-startproject <project-name> <location>
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
