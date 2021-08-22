# Foodgram 

[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646??style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![GitHub](https://img.shields.io/badge/-GitHub-464646??style=flat-square&logo=GitHub)](https://github.com/)
[![docker](https://img.shields.io/badge/-Docker-464646??style=flat-square&logo=docker)](https://www.docker.com/)
[![NGINX](https://img.shields.io/badge/-NGINX-464646??style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![Python](https://img.shields.io/badge/-Python-464646??style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646??style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646??style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)

Проект Foodgram - продуктовый помощник, позволяет размещать рецепты, делиться и скачивать списки продуктов.

Учебный проект, выполненный в рамках курса python-разработчик от Яндекс.Практикум.

## Начало работы

Для запуска проекта на локальной машине в целях разработки и тестирования.

### Предварительная подготовка

#### Установка Docker
  Установите Docker, используя инструкции с официального сайта:
  - для [Windows и MacOS](https://www.docker.com/products/docker-desktop) 
  - для [Linux](https://docs.docker.com/engine/install/ubuntu/). Установите [Docker Compose](https://docs.docker.com/compose/install/)

### Установка проекта (на примере Linux)

  - Создайте папку для проекта YaMDb `mkdir yamdb` и перейдите в нее `cd foodgram`
  - Склонируйте этот репозиторий в текущую папку `git clone https://github.com/Dozo-org/foodgram-project-react`
  - Создайте файл `.env` командой `touch .env` и добавьте в него переменные окружения для работы с базой данных:
  Пример добавляемых настроек:
    ```
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    DB_HOST=postgres
    DB_PORT=5432
    ```
  - Запустите docker-compose `sudo docker-compose up -d` 
  - Примените миграции `sudo docker-compose exec web python manage.py migrate`
  - Соберите статику `sudo docker-compose exec web python manage.py collectstatic --no-input`
  - Создайте суперпользователя Django `sudo docker-compose exec web python manage.py createsuperuser --email 'admin@yamdb.com'`

### Тестирование и работа API

  **Доступные запросы и ожидаемая форма ответов описаны по адресу http://localhost/redoc/.**

## Подготовка удаленного сервера для развертывания приложения

Для работы с проектом на удаленном сервере должен быть установлен Docker и docker-compose.
Команда для установки докера:
```
sudo apt install docker.io
```
Инструкция по установке docker-compose:
```
https://docs.docker.com/compose/install/
```
Создайте папку проекта на удаленном сервере и скопируйте туда файлы docker-compose.yaml, Dockerfile, nginx/default.conf:
```
scp ./<FILENAME> <USER>@<HOST>:/home/<USER>/yamdb_final/
```

### Подготовка репозитория на GitHub

Для использования Continuous Integration и Continuous Deployment необходимо в репозитории на GitHub прописать Secrets - переменные доступа к вашим сервисам.
Переменые прописаны в workflows/foodgram_workflow.yaml

* DOCKER_PASSWORD, DOCKER_USERNAME - для загрузки и скачивания образа с DockerHub 
* USER, HOST, PASSPHRASE, SSH_KEY - для подключения к удаленному серверу 
* TELEGRAM_TO, TELEGRAM_TOKEN - для отправки сообщений в Telegram

### Развертывание приложения

1. При пуше в ветку main приложение пройдет тесты, обновит образ на DockerHub и сделает деплой на сервер. Дальше необходимо подлкючиться к серверу.
```
ssh <USER>@<HOST>
```
2. Выполните команды для применения миграций django-приложения и сборки статики:
```
sudo docker-compose exec web python manage.py migrate --noinput
sudo docker-compose exec web python manage.py collectstatic --no-input 
```
3. Для использования панели администратора по адресу http://<server_address>/admin/ необходимо создать суперпользователя.
```
docker-compose exec web python manage.py createsuperuser
```
5. К проекту по адресу http://<server_address>/redoc/ подключена документация API. В ней описаны шаблоны запросов к API и ответы. Для каждого запроса указаны уровни прав доступа - пользовательские роли, которым разрешён запрос.

## Авторы

* **Roman Rogachev** - автор, студент курса Python-разработчик в Яндекс.Практикум. Данный проект является учебным.
Если возникли вопросы или пожелания по проекту можете написать на почту - rogachew.r@yandex.ru

## Ссылки

Проект доступен по следующей ссылке <http://178.154.224.251/>

Учетная запись администратора:
  Email: admin@foodgram.com
  Password: foodgram

## Бейдж workflows

![example workflow](https://github.com/Dozo-org/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)
