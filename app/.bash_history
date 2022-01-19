pwd
cd /root/
ls
django-admin startproject agenda .
ls
python manage.py startapp contatos
python3 manage.py startapp contatos
exit
ls
cd /root/
ls
python3 manage.py migrate
exit
cd /root/
python3 manage.py makemigration
python3 manage.py migrate
exit
