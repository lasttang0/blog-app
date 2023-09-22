<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

# Django Blog Project with REST API

Blog App is the local Django web application designed for managing a personal blog. Additionally, it provides REST API
functionality for accessing blog data.



<!-- TABLE OF CONTENTS -->

<details>
  <summary>Table of Contents</summary>

- [System Requirements](#system-requirements)
- [Installation](#installation)
- [Launch](#launch)
- [REST API](#rest-api)
- [Screenshots](#screenshots)
- [Translations](#translations)
- [Continuous Integration](#continuous-integration)
- [Code Quality](#code-quality)
- [License](#license)
- [Contact](#contact)

</details>

## System Requirements

Before you begin, make sure you have the following software installed on your system:

- Python (version 3.x): You can download Python from [python.org](https://www.python.org/downloads/).

## Installation

To set up the project, follow these steps on command line:

1. Clone the repository:

   ```bash
   git clone https://github.com/lasttang0/blog-app.git
   cd blog-app
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```   

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```      

4. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```     

## Launch

1. Start the local server:

   ```bash
   python manage.py runserver
   ```

2. You can now access your blog in a web browser at:

   ```arduino
   http://127.0.0.1:8000/
   ```   

3. The administrative interface is available at:

   ```bash
   http://127.0.0.1:8000/admin/
   ```

## REST API

You can use the REST API to access your blog's data. API endpoints are available at:

   ```bash
   http://127.0.0.1:8000/api/v1/
   ```

![REST API](https://github.com/lasttang0/blog-app/blob/main/screenshots/rest.png?raw=true)

## Screenshots

Here are some screenshots of the application:

**Post page**

![Post page](https://github.com/lasttang0/blog-app/blob/main/screenshots/post.png?raw=true)

**Admin page**

![Admin page](https://github.com/lasttang0/blog-app/blob/main/screenshots/admin.png?raw=true)

## Translations

- [Russian Translation](README_ru.md)

## Continuous Integration

[![Build and Test](https://github.com/lasttang0/blog-app/actions/workflows/build.yml/badge.svg)](https://github.com/lasttang0/blog-app/actions/workflows/build.yml)

This project is continuously integrated and tested using GitHub Actions. Automated tests and checks are run to ensure
code quality and maintain project health.

## Code Quality

- Docstrings are included in the code to provide clear and accessible documentation for each module, function, and
  class.

- The project's codebase is covered by unit tests to ensure robustness and reliability.

![Tests coverage](https://github.com/lasttang0/blog-app/blob/main/screenshots/tests.png?raw=true)

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See LICENSE.md for more information



<!-- CONTACT -->

## Contact

Project Link: [https://github.com/lasttang0/blog-app](https://github.com/lasttang0/blog-app)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

