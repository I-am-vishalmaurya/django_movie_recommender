# Django Movie Recommender Backend
A simple Django backend for the Movie Recommender project. It uses
[Django](https://www.djangoproject.com/) as a backend and for rest-api implementation it uses [django-rest-framework](https://www.django-rest-framework.org/).

Total 400,000 Movies Data were collected using the TMDB API. Only 10,000 movies were filtered
out to reduce the size of the database.

For user authentication [Djoser](http://djoser.readthedocs.io) is used, which is a simple
authentication library for Django.

### How to set up the Django Server:
1. Create a virtual environment for the django project first. For example, I created a virtual environment for the project using [virtualenv](https://virtualenv.pypa.io/en/stable/userguide/installation.html).
2. Install the dependencies using the following command: `pip install -r requirements.txt`
3. Create a database using the following command: `python manage.py makemigrations && python manage.py migrate`
4. Import the movies data and movie details in respective tables.
5. Create a .env file in the `finalYearProject` directory of the project and add the following lines:
   1. secret_key=<your secret key>
   2. DATABASE_NAME=<your database name>
   3. LOCAL_DB_PASSWORD=<your database password>
   4. DEBUG=True
   5. EMAIL_HOST=<your email host>
   6. EMAIL_HOST_PASSWORD=<your email host password>
6. Run the server using the following command: `python manage.py runserver`
7. Go to the `http://localhost:8000/docs/` to see the api endpoints.

The defualt database used by the current code is sqlite and the database name is `movie_recommendation_db`.

You can choose mysql as your database if you want to use the mysql database.

### Here are the screenshots for the API documentation
[![API Documentation](https://user-images.githubusercontent.com/9554297/84598961-f9c8b580-b8c1-11ea-9c0c-e9f8d9f9f9d9.png)](https://user-images.githubusercontent.com/9554297/84598961-f9c8b580-b8c1-11ea-9c0c-e9f8d9f9f9d9.png)



