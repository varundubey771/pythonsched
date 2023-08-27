#!/bin/bash
pip install -r requirements.txt
npx prisma generate
npx prisma migrate deploy
FLASK_APP=main.py flask run
