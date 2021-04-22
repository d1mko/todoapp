## TODO APP

### Description
***
A simple todo app that allows users to manage their tasks.
### Technologies used
***
* Python 3.8
* Django
* Django Rest Framework
* PostgreSQL
* Svelte
* Docker

### How to run locally
***
##### Using Docker and docker-compose:
1. Install [Docker](https://www.docker.com/) and [docker compose](https://docs.docker.com/compose/).
2. Open a terminal and navigate to the project root folder.
3. Run the following `docker-compose` commands:

```
docker-compose build
docker-compose up -d
```
4. Apply migrations by using `docker-compose exec web python manage.py migrate`.
5. The backend project is running on http://localhost:8000, frontend - http://localhost:5000.

##### Without Docker and Compose:
1. [Install Python3.8](https://www.python.org/downloads/).
2. [Install PostgreSQL](https://www.postgresql.org/) and start it.
3. Open a terminal and navigate to the project root folder.
4. Set up virtual environment: [tutorial](https://docs.python.org/3/tutorial/venv.html).
5. Install necessary packages: `pip install requirements.txt`.
6. Configure database in `config/settings.py`
7. Run next commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```
8. The backend project is running on http://localhost:8000
9. [Install Node.js](https://nodejs.org/en/)   
10. To run frontend run next commands:
```
npm install
npm run dev
```
11. The frontend is running on http://localhost:5000

