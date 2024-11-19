# Git Flow Process

This is a Django demo project that demonstrates the git flow process

## Prerequisites

- Python 3.11 (minimum)
- (Optinoal) Docker installed on your machine
- (Optional) Docker Compose installed on your machine

## Project Setup (Docker)

### 1. Clone the Repository

```sh
git clone git@github.com:jiaulislam/git-flow.git
cd git-flow
```

### 2. Run Project with Docker

```sh
docker build -t git-flow .
docker run --name git-flow-container -p 8080:8080 git-flow
```

### 3. Run Tests

```sh
docker exec -it git-flow-container pytest
```
> previously while running docker container specifically named the container with 'git-flow-container'

## Project Setup (virtualenv)

### 1. Clone the Repository

```sh
git clone git@github.com:jiaulislam/git-flow.git
cd git-flow
```

### 2. Install UV

```sh
pip install uv
```

### 3. Create Virtual Environment

```sh
# default system python
uv venv
# with specific python
uv venv --python 3.13
```

### 4. Activate the VirtualEnv

```sh
source ./venv/bin/activate
```

### 5. Install dependencies

```sh
uv sync
```

### 5. Make migrations & Run Project with Poetry VirtualEnv

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
```

## Run Tests

```sh
pytest
```

# For Development Contribution
For development purpose before commiting on the project please install `pre-commit`. So our hooks on every commit to automatically point out issues in code such as missing semicolons, trailing whitespace, and debug statements. By pointing these issues out before code review, this allows a code reviewer to focus on the architecture of a change while not wasting time with trivial style nitpicks.

```sh
pre-commit install
pre-commit run -c ./pre-commit-config.yaml
```
