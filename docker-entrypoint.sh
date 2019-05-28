#!/bin/sh

set -e

gunicorn -c etc/gunicorn.conf.py main:app

exec "$@"
