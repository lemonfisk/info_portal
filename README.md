### PREPARE DESKTOP

1. sudo snap install pycharm-community --classic

sudo apt install git-all
git --version
git config --global user.name "MDI"
git config --global user.email "mdi@home.ru"

install docker

ssh-keygen
cat /home/mdi/.ssh/id_rsa.pub 



### Project: Informational Portal (info-portal)

1. sudo apt update
2. sudo apt upgrade
3. cd info_portal
2. sudo apt install python3-django
3. django-admin startproject info_portal .
4. python3 manage.py runserver
5. http://127.0.0.1:8000/

use virtenv
1. git clone
2. Pycharm - create venv
3. cd infoportal
4. source venv/bin/activate
5. curl -sSL https://install.python-poetry.org | python3 -
6. poetry init
7. poetry install

### RUN APPLICATION IN DOCKER
1. docker build -t my_app .
2. docker run -d -p 8080:8000 my_app

Diagnostic
docker run -it my_app /bin/bash


### RUN APPLICATION IN SERVER
1. python3 manage.py runserver
2. http://127.0.0.1:8000/
