#!/bin/bash


# Kali style
apt-get -y install python python-pip python3 virtualenv virtualenv-clone \
    virtualenvwrapper

source /usr/share/virtualenvwrapper/virtualenvwrapper.sh

mkvirtualenv py2-django -p /usr/share/python
deactivate

mkvirtualenv py3-django -p /usr/share/python3
pip install -r requirements/local.txt

# SQLITE3

# POSTGRESQL
#apt-get -y install postgresql
#service postgresql start
#createdb -E UTF-8 django_wordlist

cd ../
python manage.py check
bash utility/gen_initial_data.sh

echo "Now run python manage.py runserver"
exit 0
