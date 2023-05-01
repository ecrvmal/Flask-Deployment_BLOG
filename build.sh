#!/usr/bin/env bash
# exit on error
set -o errexit

flask db init
flask db migrate
flask create-init-tags
flask create users
flask create articles
