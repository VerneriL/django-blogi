#!/usr/bin/env python

import os

import django

from django.contrib.auth import get_user_model

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'koodausblogi.settings')
    django.setup()

    username=os.environ.get('ADMIN_USER_NAME', 'admin')
    email=os.environ.get('ADMIN_USER_EMAIL', '')
    password=os.environ['ADMIN_USER_PASSWORD']

    if username:
        return
    else:
        print(f"Creating superuser named {username!r}")
        user_model = get_user_model()
        user_model.objects.create_superuser(username=username, email=email, password=password)

if __name__=='__main__':
    main()