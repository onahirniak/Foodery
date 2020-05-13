#!/bin/sh
set -e

case $1 in
     migrate)
          python manage.py db upgrade
          ;;
    test)
          python manage.py test
          ;;
     *)
          python manage.py run
          ;;
esac
