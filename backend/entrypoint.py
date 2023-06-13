#!/usr/bin/env python

import os


def run(command):
    """run terminal command"""
    return os.system(command)


run('python manage.py wait_for_db')
run('python manage.py makemigrations')
run('python manage.py migrate')
run('python manage.py collectstatic --no-input')

if os.environ['DEBUG'] == 'True':
    run('python manage.py runserver 0.0.0.0:8000')
else:
    run('gunicorn backend.wsgi:application -c ./deploy/gunicorn/config.py')
