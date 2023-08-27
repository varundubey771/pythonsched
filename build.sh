#!/bin/bash
pip install -r requirements.txt
npx prisma generate
npx prisma migrate deploy
flask run
