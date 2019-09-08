#!/bin/bash
gunicorn --bind 0.0.0.0:5000 --log-level debug --worker-class gevent --workers 5 wsgi:app