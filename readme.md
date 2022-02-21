# challenge-restapi-django
An User Profile CRUD application made with Django for a job interview

FYI: Project created in windows 10 OS. The cmds described in referred steps may change if you are using Linux/MacOS. IDE: Visual Studio Code

## Describing Rest API

#### Rest API endpoints:
<ul>
   <li>POST /api/profile => Create user profile.</li>
   <li>GET /api/profile => Get all profiles (using pagination and search option ie: /profile?name='Marco' gets all profiles with that name).</li>
   <li>GET /api/profile/{ìd} => Get a single user profile.</li>
</ul>

#### Representation of user profile data:

<pre>
{
"firstName": "Marco Túlio", : String
"lastName": "Fonseca", : String
"age":'32', : Integer
"sex": "M" : Enum
}
</pre>

## How to run this application locally?

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
       - Create virtual env: python -m venv /path/to/new/virtual/environment or python3 -m venv /path/to/new/virtual/environment
       - Activate venv or env file:  execute this command in windows inside venv or env folder: . .\Scripts\activate or source .\Scripts\activate
       - Install dependencies: pip install -r requirements.txt <br/>
       - Make migration of db: python manage.py migrate <br/>
       - Run server locally: python manage.py runserver<br/>
