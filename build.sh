#!/usr/bin/env bash
# exit on error
set -o errexit
pg_ctl -D postgresql://user:CDu8F1LcFO42KbqGbyRVcBKXFYaE9h50@dpg-ch5sff4s3fvuobaiaun0-a/db_lj4s start
sleep 5
flask db init
flask db migrate
flask create-init-tags
flask create users
flask create articles
