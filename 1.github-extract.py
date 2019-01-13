#!/usr/bin/env python

from glob import glob
import shutil
import requests
import pickle
import fnmatch
import tempfile
import json
import os

# Find Dockerfiles on Github instead
if not os.path.exists('data'):
    os.mkdir('data')

# Helper functions

def write_file(content, output_file, mode='w'):
    with open(output_file, mode) as filey:
        filey.writelines(content)
    return output_file

def recursive_find_files(base, patterns):
    '''a wrapper to recursive find to find more than one pattern'''
    results = []
    for pattern in patterns:
        result = list(recursive_find(base, pattern))
        result = [x for x in result if os.path.isfile(x)]
        results = results + result
    return results

def recursive_find(base, pattern=None):
    if pattern is None:
        pattern = "*"

    for root, dirnames, filenames in os.walk(base):
        for filename in fnmatch.filter(filenames, pattern):
            yield os.path.join(root, filename)

def clone(url, tmpdir=None):
    '''clone a repository from Github'''
    if tmpdir is None:
        tmpdir = tempfile.mkdtemp()
    name = os.path.basename(url).replace('.git', '')
    dest = '%s/%s' %(tmpdir, name)
    return_code = os.system('git clone %s %s' %(url, dest))
    here = os.getcwd()
    if return_code == 0:
        return dest
    print('Error cloning repo.')

# Input files include the original 1000, plus items retrieved per organization
items = pickle.load(open('github/github_dockerfiles.pkl', 'rb'))
len(items)
#1000

for i in range(0, len(items)):

    item = items[i]

    # only include Dockerfiles
    if item['name'].lower() == "dockerfile":
        repo = item['repository']['html_url']
        username = repo.split('/')[-2]
        reponame = repo.split('/')[-1]
        letter = username[0].lower()
        folder = os.path.join('data', letter, username, reponame)   

        if os.path.exists(folder):
            print('Already parsed %s' % folder)
            continue

        cloned = clone(repo)
        dockerfiles = recursive_find_files(cloned,['Dockerfile'])
        readmes = recursive_find_files(cloned, ['readme*','README*'])

        if len(dockerfiles) > 0 and len(readmes) > 0:
            print('Found %s dockerfiles for %s' %(len(dockerfiles), repo))
            if not os.path.exists(folder):
                os.makedirs(folder)

            # Save Dockerfiles 
            for d in range(0, len(dockerfiles)):
                outfile = '%s/Dockerfile.%s' % (folder, d)
                dockerfile = dockerfiles[d]
                if os.stat(dockerfile).st_size > 0:
                    shutil.copyfile(dockerfile, outfile)

            # Save all readmes into one README.md
            metadata = os.path.join(folder, 'README.md')
            empty = True
            with open(metadata, 'w') as filey:
                for readme in readmes:
                    if os.stat(readme).st_size > 0:
                        empty = False
                        with open(readme, 'r') as readme_file:
                            content = readme_file.read()
                        filey.writelines(content)

            # If there isn't any metadata after all
            if empty is True:
                print('No metadata for %s/%s' % (username, reponame) )
                shutil.rmtree(folder)
                # If we don't have other repos under this username
                if len(glob('%s/*' % os.path.dirname(folder))) == 0:
                    shutil.rmtree(os.path.dirname(folder))

        # Clean up
        shutil.rmtree(os.path.dirname(cloned))
    
# Next, do the same for organizations
orgs = glob('github/github_orgs_*.json')
