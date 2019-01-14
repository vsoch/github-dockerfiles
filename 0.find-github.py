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

def save_json(content, output_file, mode='w'):
    with open(output_file, mode) as filey:
        filey.writelines(json.dumps(content, indent=4))
    return output_file

# Find Dockerfiles on Github instead
if not os.path.exists('github'):
    os.mkdir('github')

# We are only allowed 1000 results per search
def search_github(baseurl, token, headers, items=None):
    if items == None:
        items = []
    for page in range(1, 11):
        url = baseurl + '&page=%s' % page
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print('Obtained %s' % url)
            result = response.json()
            items = items + result['items']
            if len(result['items']) == 0:
                print('No results for %s' % url)
                return items
            elif len(result['items']) < 100:
                print('Done searching %s' % url)
                return items
            else:
                print('Problem with page %s, stopping.' % page)
                return items
        seconds = choice(list(range(10,25)))
        sleep(seconds)
    return items

# github-dockerfiles are the first 1000, no limits on search
url = 'https://api.github.com/search/code?q=Dockerfile+filename:Dockerfile&per_page=100'
items = search_github(url, token, headers)
save_json(items, 'github/github_dockerfiles.json')
pickle.dump(items, open('github/github_dockerfiles.pkl', 'wb'))

# Get list of organizations
orgs = []
url = 'https://api.github.com/organizations?per_page=100'
while True:
    print('Asking for %s' % url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        orgs = orgs + response.json()
        match = re.search('<(.*?)>', response.headers['Link'])
        url = response.headers['Link'][match.start()+1:match.end()-1]
    else:
        print('Problem with %s' % url)
        break
    if len(orgs) % 1000 == 0:
        pickle.dump(orgs, open('github/github_orgs.pkl', 'wb'))

# rate limit exceeded at:
# https://api.github.com/organizations?per_page=100&since=14987782
save_json(orgs, 'github/github_orgs.json')
pickle.dump(orgs, open('github/github_orgs.pkl', 'wb'))

# Next, search for Dockerfiles within organizations
baseurl = 'https://api.github.com/search/code?q=Dockerfile+filename:Dockerfile+org=%s&per_page=100'

for i in range(1492, len(orgs)):
    item = orgs[i]
    org = item['login']
    url = baseurl % org
    org_items = search_github(url, token, headers)
    if len(org_items) > 0:
        print('Found %s results for %s' %(len(org_items), org))
        save_json(org_items, 'github/github_orgs_%s.json' % org)
    else:
        print('No results for %s' % org)

# Next, search equivalently but limit to oranizations we've found
users = set()
for item in items:
    user = item['repository']['full_name'].split('/')[0]
    users.add(user)

len(users)
# 604
