#!/bin/bash
set -e
python3 manage.py collectstatic --noinput
honcho start
