#!/usr/bin/env bash

set -e

ROOT_APP_DIR="{{cookiecutter.project_slug}}"
APP_NAME=$1

APP_CLASS_NAME=`echo "${APP_NAME^}" | sed -r 's/_([a-z])/\U\1/gi' | sed -r 's/^([A-Z])/\l\1/'`
APP_CLASS_NAME="${APP_CLASS_NAME^}"

APP_DIR=$ROOT_APP_DIR/${APP_NAME}

create_module() {
    path=$1
    mkdir $path
    touch $path/__init__.py
}

# Create app folder
echo "Create app: ${APP_NAME}"

create_module "$APP_DIR"
create_module "$APP_DIR/migrations"

# Create admin.py file
echo "from django.contrib import admin
from . import models
" > $APP_DIR/admin.py


# Create apps.py file
echo "from django.apps import AppConfig


class ${APP_CLASS_NAME}Config(AppConfig):
    name = \"$ROOT_APP_DIR.$APP_NAME\"
    verbose_name = \"$APP_CLASS_NAME\"

    def ready(self):
        pass" > $APP_DIR/apps.py

# Create models.py file
echo "from django.db import models
" > $APP_DIR/models.py

# Create serializers.py file
echo "from rest_framework import serializers
from . import models
" > $APP_DIR/serializers.py

# Create urls.py file
echo "from django.urls import path

from . import views

urlpatterns = [
    # path('demo', views.DemoView.as_view(), name='demo'),
]

" > $APP_DIR/urls.py

# Create views.py file
echo "from rest_framework.views import APIView
" > $APP_DIR/views.py

# Append install app
APPEND_APP_INSTALL='# APPEND_NEW_APP #'
APP_INSTALL="'$ROOT_APP_DIR.$APP_NAME.apps.${APP_CLASS_NAME}Config',"
sed -i "s/$APPEND_APP_INSTALL/$APP_INSTALL\n    $APPEND_APP_INSTALL/g" config/settings/base.py

# Append root url
APPEND_NEW_URL='# APPEND_NEW_URL #'
NEW_URL="path('v1/$APP_NAME/', include(('$ROOT_APP_DIR.$APP_NAME.urls', '$ROOT_APP_DIR.$APP_NAME'), namespace='$APP_NAME')),"
sed -i "s|$APPEND_NEW_URL|$NEW_URL\n    $APPEND_NEW_URL|g" config/urls.py