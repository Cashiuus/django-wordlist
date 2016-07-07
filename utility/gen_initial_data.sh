#!/usr/bin/env bash

echo "[-->] Load migrations"
python manage.py migrate

echo "[-->] Load initial wordlist categories"
python manage.py loaddata initial_lists_data --traceback

