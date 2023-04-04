# Notifications POC


## General project dependencies

 - [poetry](https://python-poetry.org/)
 - [django](https://www.djangoproject.com/)
   - [django-rest-framework.](https://www.django-rest-framework.org/)
 - [kafka](https://kafka.apache.org/)
   - [zookeeper](https://zookeeper.apache.org/)
 - [vault](https://www.vaultproject.io/)


## Development project dependencies

 - [pre-commit](https://pre-commit.com/)
   - [black](https://github.com/psf/black)
   - [flake8](https://gitlab.com/PyCQA/flake8)
   - [isort](https://gitlab.com/PyCQA/isort)  # TODO
   - [bandit](https://gitlab.com/PyCQA/bandit)
 - [django-extensions](https://django-extensions.readthedocs.io/)
 - [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/)


## Local development setup


#### using `docker-compose`
```bash
docker-compose -p notification-poc -f config/compose.yaml up --build -d
```
