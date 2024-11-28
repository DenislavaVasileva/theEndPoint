# The End Point - Django Project

## Description:

This website serves as a community platform for ice-climbers who aim to conquer the world's eight-thousanders—mountains
with altitudes above 8,000 meters.
Built using Django Framework, it allows users to share experiences and learn more about the most challenging
peaks on Earth.

## Features

- **Public Section**: Allows users to view blog posts and access detailed information about the 14 eight-thousanders.
- **Private Section**: Enables users to add their own posts, comment on others' posts, and add their favorite peaks to their wish list.
- **Admin Section**: Provides tools for managing mountains, posts, and user roles.

## Project Setup:

**1.Clone the repository:**

    git clone https://github.com/DenislavaVasileva/theEndPoint.git

**2.Run the following command to install the listed requirements:**

    pip install -r requirements.txt
### requirements.txt:
- asgiref==3.8.1
- certifi==2024.8.30
- charset-normalizer==3.4.0
- Django==5.1.2
- django-unfold==0.41.0
- idna==3.10
- pillow==11.0.0
- psycopg==3.2.3
- python-dotenv==1.0.1
- requests==2.32.3
- six==1.16.0
- sqlparse==0.5.1
- tzdata==2024.2
- urllib3==2.2.3

**3.DATABASE Setup:**

Create a `.env` file in the root directory of the project to store your database credentials securely.
Add the following lines to the `.env` file:
- DATABASE_USER=your_username
- DATABASE_PASSWORD=your_password


In the `settings.py` file, the database configuration will automatically use the credentials from your `.env` file:


    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "your_db_name",
            "USER": os.getenv('DATABASE_USER'),
            "PASSWORD": os.getenv('DATABASE_PASSWORD'),
            "HOST": "127.0.0.1",
            "PORT": "5432",
        }
    }
**4.Settings.py configuration:**

In the `.env` file add the following line:
- SECRET_KEY=the_one_provided_in_the_survey

In the `settings.py` file the SECRET_KEY configuration will use the credentials from the `.env` file:
    
    SECRET_KEY = os.getenv('SECRET_KEY')

**5.Apply migrations:**
    
    python manage.py migrate
**6.Create a Superuser:**

To access the admin panel, create a superuser by running the following command in the terminal:

    python manage.py createsuperuser

You will be prompted to enter:

- Username
- Email
- Password

After completing this step, you can log into the admin panel at:

    http://127.0.0.1:8000/admin/

**7.Run the following commands to load the initial data into the database:**

    python manage.py loaddata categories.json
    python manage.py loaddata peaks.json
    python manage.py loaddata groups.json

**8.Start the development server:**

    python manage.py runserver


## Known Issues
- **Database Migrations**:
The database migrations may fail if the database is not properly configured or set up.
- **Python Compatibility**:
This project is built with Python 3.13, which is not compatible with psycopg2 or psycopg2-binary.
As a result, psycopg is used for database interactions. However, for users working with lower versions of Python,
psycopg may not function as expected.
In such cases, it is recommended to switch to psycopg2 or psycopg2-binary for compatibility.