import django
django.setup()
from django.contrib.auth.models import User;

username = 'amcat';
password = 'amcat';
email = 'amcat@example.com';

if User.objects.filter(username=username).count()==0:
    User.objects.create_superuser(username, email, password)
    print('Superuser {username!r} created.'.format(**locals()))
else:
    print('User {username!r} already existed .')

