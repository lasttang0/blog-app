<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

# Django Blog Project with REST API

Blog App — это локальное веб-приложение Django, предназначенное для управления личным блогом. Также в приложении
представлена функциональность REST API для доступа к данным блога.



<!-- TABLE OF CONTENTS -->

<details>
  <summary>Содержание</summary>

- [Системные требования](#системные-требования)
- [Установка](#установка)
- [Запуск](#запуск)
- [REST API](#rest-api)
- [Скриншоты](#скриншоты)
- [Непрерывная интеграция](#непрерывная-интеграция)
- [Качество кода](#качество-кода)
- [Лицензия](#лицензия)
- [Контакты](#контакты)

</details>

## Системные требования

Прежде чем продолжить, убедитесь, что на вашем компьютере установлено следующее программное обеспечение:

- Python (версия 3.x): Вы можете загрузить Python по ссылке [python.org](https://www.python.org/downloads/).

## Установка

Чтобы настроить проект, выполните следующие действия в командной строке:

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/lasttang0/blog-app.git
   cd blog-app
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```   

3. Примените миграции:

   ```bash
   python manage.py migrate
   ```      

4. Создайте суперпользователя:

   ```bash
   python manage.py createsuperuser
   ```     

## Запуск

1. Запустите локальный сервер:

   ```bash
   python manage.py runserver
   ```

2. Теперь вы можете получить доступ к своему блогу в веб-браузере по адресу:

   ```arduino
   http://127.0.0.1:8000/
   ```   

3. Административный интерфейс доступен по адресу:

   ```bash
   http://127.0.0.1:8000/admin/
   ```

## REST API

Вы можете использовать REST API для доступа к данным вашего блога. Точки доступа API расположены по адресу:

   ```bash
   http://127.0.0.1:8000/api/v1/
   ```

![REST API](https://github.com/lasttang0/blog-app/blob/main/screenshots/rest.png?raw=true)

## Скриншоты

Несколько скриншотов приложения:

**Страница поста в блоге**

![Post page](https://github.com/lasttang0/blog-app/blob/main/screenshots/post.png?raw=true)

**Страница администрирования**

![Admin page](https://github.com/lasttang0/blog-app/blob/main/screenshots/admin.png?raw=true)

## Непрерывная интеграция

[![Build and Test](https://github.com/lasttang0/blog-app/actions/workflows/build.yml/badge.svg)](https://github.com/lasttang0/blog-app/actions/workflows/build.yml)

Этот проект постоянно интегрируется и тестируется с помощью GitHub Actions. Автоматические тесты и проверки выполняются
для обеспечения качества кода и поддержания работоспособности проекта.

## Качество кода

- В код включены строки документации, обеспечивающие чёткую и доступную документацию для каждого модуля, функции и
  класса.

- Код проекта покрывается модульными тестами для обеспечения устойчивости и надёжности.

![Tests coverage](https://github.com/lasttang0/blog-app/blob/main/screenshots/tests.png?raw=true)

## Лицензия

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Распространяется по лицензии MIT. Ознакомьтесь с LICENSE.md для получения дополнительной информации.



<!-- CONTACT -->

## Контакты

Ссылка на проект: [https://github.com/lasttang0/blog-app](https://github.com/lasttang0/blog-app)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

