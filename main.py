# -*- coding: utf-8 -*-
import logging
from flask import Flask, request
import requests
from bs4 import BeautifulSoup
import re
import asyncio
# from prisma import Prisma
# from prisma.models import JobCount
import datetime
import subprocess

# Load data from config.ini file
# config = configparser.ConfigParser()
# config.read('config.ini')

# async def writer(data):
#     db = Prisma(auto_register=True)
#     await db.connect()

#     # write your queries here
#     resp = await JobCount.prisma().create_many(
#         data=data
#     )
#     await db.disconnect()
#     return resp

def scrape_jobs(country,jobTitle):
    url = f"https://www.linkedin.com/jobs/search/?keywords={jobTitle}&location={country}"

    headers = {
        "User-Agent": "Your User Agent String"
        # Add any other headers you might need
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        job_count_elem = soup.find("code", {"id": "totalResults"})
        if job_count_elem:
            job_count_comment = str(job_count_elem)
            job_count = re.search(r"<!--(\d+)-->", job_count_comment).group(1)
            return job_count
        else:
            return "N/A"
    else:
        return "N/A"

# Initial Flask app
app = Flask(__name__)

@app.route('/')
def home():
   return 'Hello, what did you have for breakfast?'

@app.route('/getJobData')
def getJobData():
   countries = ["Australia","India","United Kingdom","United States","Ireland"]
   jobs = ["Python", "Java"]
   lst=[]
   for country in countries:
       for job in jobs:
           job_count = scrape_jobs(country,job)
           lst.append({"country": country,"job_count":job_count,"job":job})
   return lst

# @app.route('/sendJobDataCron')
# def sendJobDataCron():
#    countries = ["Australia","India","United Kingdom","United States","Ireland"]
#    jobs = ["Python", "Java", "Data Scientist"]
#    lst=[]
#    current_datetime = datetime.datetime.now()
#    str_cur_dt= current_datetime.strftime("%Y-%m-%d %H:%M:%S")
#    parsed_datetime = datetime.datetime.strptime(str_cur_dt, "%Y-%m-%d %H:%M:%S")    
#    for country in countries:
#        for job in jobs:
#            job_count = int(scrape_jobs(country,job))
#            lst.append({"country": country, "count": job_count, "title": job, "timestamp": parsed_datetime})
#    resp = asyncio.run(writer(lst))        
#    return resp

# if __name__ == "__main__":
#     # Running server
#     app.run(debug=True)
