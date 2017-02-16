# wait for elastic and postgres
set -e
python3 wait_services.py
if ! (psql -h postgres -U postgres -lqtA | grep -q "^amcat|"); then
    createdb -h postgres -U postgres amcat
fi
python3 -m amcat.manage migrate
python3 -m amcat.manage shell < /etc/amcat/create_superuser.py
python3 -m amcat.manage runserver 0.0.0.0:8000
