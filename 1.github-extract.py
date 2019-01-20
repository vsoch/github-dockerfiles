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

def cat_files(outfile, infiles):
    empty = True
    with open(outfile, 'w') as filey:
        for infile in infiles:
            if os.stat(infile).st_size > 0:
                try:
                    empty = False
                    with open(infile, 'r') as inf:
                        content = inf.read()
                        filey.writelines(content)
                except UnicodeDecodeError:
                    pass
    return empty


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

def parse_item(item):
    '''parse an item, meaning a search result from the Github API to describe a
       Dockerfile
    '''
    # only include Dockerfiles
    if item['name'].lower() == "dockerfile":
        repo = item['repository']['html_url']
        username = repo.split('/')[-2]
        reponame = repo.split('/')[-1]
        letter = username[0].lower()
        folder = os.path.join('data', letter, username, reponame)   

        if os.path.exists(folder):
            print('Already parsed %s' % folder)
            return

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

            # If the main repository has a main readme, save it
            readme_mains = glob("%s*" %os.path.join(cloned, 'README'))
            readme_mains = [x for x in readme_mains if os.path.isfile(x)]
            if len(readme_mains) > 0:
                metadata = os.path.join(folder, 'README.md')
                empty = cat_files(metadata, readme_mains)

                # Don't write to file again
                readmes = [x for x in readmes if x not in readme_mains]

            # If we only have ONE dockerfile, save one readme
            if len(dockerfiles) == 1:
                metadata = os.path.join(folder, 'README.0.md')
                empty = cat_files(metadata, readmes)
                if empty is True:
                    print('No metadata for %s/%s' % (username, reponame) )
                    shutil.rmtree(folder)

            # Otherwise, match dockerfiles with readmes
            else:
                dirnames = [os.path.dirname(x) for x in readmes]
                for d in range(len(dockerfiles)):
                    dockerfile = dockerfiles[d]
                    dirname = os.path.dirname(dockerfile)  
                  
                    # All readme.* files in the same folder
                    matches = [x for x in readmes if dirname in x]
                    metadata = os.path.join(folder, 'README.%s.md' % d)
                    if len(matches) > 0:
                        with open(metadata, 'w') as filey:
                            for match in matches:
                                if os.stat(match).st_size > 0:
                                    try:
                                        with open(match, 'r') as mfile:
                                            content = mfile.read()
                                        filey.writelines(content)
                                    except:
                                        pass

                    # No matches, clean up dockerfile
                    else:
                        dockerfile = '%s/Dockerfile.%s' % (folder, d)
                        if os.path.exists(dockerfile):
                            os.remove(dockerfile)

                # If we get down here and there are no readmes, save
                # all of them to one
                if len(glob('%s/README*' %folder)) == 0:
                    metadata = os.path.join(folder, 'README-cat.md')
                    empty = cat_files(metadata, readmes)
                    if empty is True:
                        shutil.rmtree(os.path.dirname(folder))

                # If we don't have other repos under this username
                try:
                    if len(glob('%s/*' % os.path.dirname(folder))) == 0:
                        shutil.rmtree(os.path.dirname(folder))
                except FileNotFoundError:
                    pass

        # Clean up
        shutil.rmtree(os.path.dirname(cloned))

# Input files include the original 1000, plus items retrieved per organization
items = pickle.load(open('github/github_dockerfiles.pkl', 'rb'))
len(items)
#1000

for i in range(594, len(items)):
    item = items[i]
    parse_item(item)
    
# Next, do the same for organizations (yes, code is redundant, deal with it)
orgs = glob('github/github_orgs_*.json')
# len(orgs)
# 1071

for i in range(0, len(orgs)):
    print('Parsing org %s of %s' %(i, len(orgs)))
    with open(orgs[i], 'r') as filey:
        content = json.loads(filey.read())
    for item in content:
        # For some reason asked for Github creds
        if "soundcloud" in orgs[i]:
            continue
        parse_item(item)
