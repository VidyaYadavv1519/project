# Platform for finding OpenSource Projects

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
![Vite](https://img.shields.io/badge/vite-%23646CFF.svg?style=for-the-badge&logo=vite&logoColor=white)
![Vue.js](https://img.shields.io/badge/vuejs-%2335495e.svg?style=for-the-badge&logo=vuedotjs&logoColor=%234FC08D)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white)

## Description
This is a platform for creating and joining Open Source Projects

## Designs
We use [Figma](https://www.figma.com/file/8EOzvY1pVd4EGF7NBt8frL/Prototyp?type=design&node-id=1-77&mode=design&t=9J3ZG8qwHYkMZzDV-0) to create our designs.

## Backend
The backend is made with django and the django restframework.

## Frontend
The frontend is made with vite and vue.js.

## LICENSE
[License](MIT-LICENSE.txt)

## How to install
1. Install  [Docker](https://docs.docker.com/install) and [Docker-Compose](https://docs.docker.com/compose)

2. Clone this repository with the following command:
    ```bash
    git clone https://github.com/to-sta/project.git
    ```

3. In the root directory is a file `.env.example` that you can use as your `.env`.

4. Then run docker-compose with the following command:
    ```bash
    docker-compose build
    docker-compose up
    ```

5. To use the django backend you have to create a superuser first.
    ```bash
    python manage.py createsuperuser
    ```

# Contributing

If you want to contribute to the project you can create an issue or ask to be assigned to an open issue.

Contributing workflow:
1. [Fork](https://docs.github.com/de/get-started/quickstart/fork-a-repo) the repo
2. Create a new branch with a name related to your changes
    ```bash
    git branch <branchName>
    ```
3. Make your changes and stage the commit
4. run [pre-commit](https://docs.docker.com/install)
to ensure code quality. If you haven't installed pre-commit yet then you can do so with the following command:
    ```bash
    pip install pre-commit
    ```
5. commit your changes
    ```bash
    git push origin <branchName>
    ```
6. [open a Pull Request](https://docs.github.com/de/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) with related title and description
