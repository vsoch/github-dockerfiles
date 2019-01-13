#!/usr/bin/env python

from bs4 import BeautifulSoup
import html2text
import requests
import pickle
from random import choice
from time import sleep
import json
import os

# Before running this file, source the .env file included
token = os.environ.get('GITHUB_TOKEN')
headers = {'Authorization': 'token %s' % token }
url = 'https://api.github.com/search/code?q=Dockerfile+filename:Dockerfile&per_page=100'
items = []

# Find Dockerfiles on Github instead
if not os.path.exists('github'):
    os.mkdir('github')

for page in range(12, 5000):
    output_file = 'github/%s.json' % page
    if not os.path.exists(output_file):
        response = requests.get(url + '&page=%s' % page, headers=headers)
        if response.status_code == 200:
            print('Obtained page %s' % page)
            result = response.json()
            with open(output_file, 'w') as filey:
                filey.writelines(json.dumps(result, indent=4))
            items = items + result['items']
        else:
            print('Problem with page %s, stopping.' % page)
            break
    seconds = choice(list(range(10,25)))
    sleep(seconds)

# One final save!
pickle.dump(items, open('github_dockerfiles.pkl', 'wb'))
