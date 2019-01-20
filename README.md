# GitHub Dockerfiles

Here we will put together a dataset that attemps to extract Dockerfile and
associated metadata from Github repositories. Specifically, the metadata
should include text from a README.md (or similar) that might describe the
repository. We take the following steps:

## Github API Search

We start with the script [0.find-github.py](0.find-github.py) that has sections
that do the following:

 - A general search for files named Dockerfile across all code. We are limited to 1000 results, and these 1000 results are saved under [github/github-dockerfiles.pkl](github/github-dockerfiles.pkl) and [github/github-dockerfiles.json](github/github-dockerfiles.json)
 - From the limited result, I learned that to get more specific results I would need to make the search more specific. Thus, I used up my rate limit to extract a listing of organizations, saved to [github/github-orgs.pkl](github/github-orgs.pkl) and [github/github-orgs.json](github/github-orgs.json).
 - From the list of organizations I again did a search to find Dockerfiles within the organization. For organizations that had some sort of result, they are saved in the format `github/github-org-<orgname>.json` and `github/github-org-<orgname>.pkl` Since I only needed a reasonably sized subset, I stopped at index 7090 of the organizations list when I had extracted lists of Dockerfiles for 1071 organizations. This is in addition to the first 1000 returned by the general search.

## Download

To retrieve data for the repositories (meaning the Dockerfiles and metadata) I then parsed
through the organization Dockerfile results, and the original 1000 general results. For
each, we create a subfolder under [data](data) that is organized by the lowercase first letter of
the Github organization, and then within has a folder hierarchy for the Github organization
name and the repository name. Within each folder we save the Dockerfile(s) and a single text
file with combined README.md (and similar) extracted from the repository. This step was 
performed by [1.github-extract.py](1.github-extract.py).

## Container Trees
