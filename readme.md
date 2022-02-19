# challenge-restapi-django
An User CRUD application made with Django for a job interview

#### How to run this application locally on Windows?

#### 1 Install python and db.

1.1. First of all, install last stable version of python (https://www.python.org/downloads/)                 
          -  02/18/2022: last version was python -v 3.10.2 <br/>
          -  Edit environment variable PATH and add %PYTHONPATH%. <br/>
          -  set variable %PYTHONPATH% with value: _**your directory to python**_ <br/>
          -  Restart PC  <br/>
      
1.2. Install Postgresql database <br/>
          -  for my purpose, I installed latest version 14.2 (https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) <br/>
          -  Follow the wizard, set a password for localhost and port (default: 5432) and it's done. <br/>
          
#### 2 Django Project
   
2.1. Download Django Project to your workspace<br/>
       - Clone repo: git clone https://github.com/devmustache/challenge-restapi-django.git <br/>
2.2. Setting up environment file <br/>
       - cp env.example .env<br/>
       - change .env file to your credentials and settings of postgres<br/>
2.3. Up and running <br/>
       - Install dependencies: pip install -r requirements.txt <br/>
       - Make migration of db: python manage.py migrate <br/>
       - Run server locally: python manage.py runserver<br/>
