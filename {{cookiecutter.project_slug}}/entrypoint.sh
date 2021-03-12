#!/bin/bash
set -e

# Create admin account if not exists
cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model

User = get_user_model()  # get the currently active user model,

User.objects.filter(username='admin').exists() or \
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
EOF


python3 manage.py collectstatic --noinput
honcho start
