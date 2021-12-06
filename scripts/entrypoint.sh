#!/bin/sh

set -o errexit
set -o nounset

if [ "$DB_ENGINE" = "postgres" ]
then
    echo "Waiting for DB: <$DB_ENGINE>"

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 1
    done

    echo "<$DB_ENGINE> started"
fi

uvicorn app.main:app --reload --host 0.0.0.0 --port $APP_PORT