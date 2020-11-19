# SABO TRIGRS Database Management

## Installation

Make sure you have python and pip installed on your environment. Please use terminal and type python to check.

Clone this repo

```bash
git clone https://github.com/MarianoZeinnico/sabo-trigrs-database-management.git
```

Create MYSQL database with this settings :

```bash
DB_NAME: sabo_trigrs_database
USER: root
PASSWORD: root
```

Or if you prefer your own MYSQL settings, please open settings.py and edit on this part :

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sabo_trigrs_database',
        'USER': 'root',
        'PASSWORD': 'root',
    }
}
```

Enter project folder and install virtualenv

```bash
virtualenv env
```

Activate virtual environment

```bash
Windows : env\Script\activate.bat
Mac & Unix : source env/bin/activate
```

Install package for project requirements

```bash
pip install requirements.txt
```

Run django migration for database :

```bash
python manage.py migrate
```

Create superadmin :

```bash
python manage.py createsuperadmin
```

Run project :

```bash
python manage.py runserver
```

In default, the website will be running on port 8000. If port 8000 is using by another app, you can perform runserver above following with the port number that you want.

And now, you can access the app in :

```bash
{{url}}/login
```

Use your superuser credentials to access it.
