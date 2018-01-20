#!/bin/bash

source venv/bin/activate
export FLASK_APP=titlecard.py

flask run --host=0.0.0.0
