createdb -h postgres -U postgres amcat
set -e
python3 -m amcat.manage migrate
python3 -m amcat.manage shell < /etc/amcat/create_superuser.py
python3 -m amcat.manage runserver 0.0.0.0:8000
