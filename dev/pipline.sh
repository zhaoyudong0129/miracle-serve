#!/usr/bin/env bash
echo "***start git pull***"
git pull
echo "***start pip install ***"
pip install -r requirements.txt
echo "***start migrate ***"
python manage.py migrate
echo "***start collectstatic***"
python manage.py collectstatic
echo "***restart miracle***"
supervisorctl -c dev/supervisord.conf restart miracle