Scripts to create subscriptions to zendesk sections or forum topics

To use these scripts:
Clone the repo
pip install requests

Creating Section Subscriptions:

This script creates a subscription to every existing Help Center Section to the specified user_ids. Users will get notified of new articles created in each section and any comments posted. 

Edit create_section_subscriptions.py

If you don't want the user to get notified of new comments, set "include_comments" to False.


self.user_ids -- takes a list of user ids
self.zendesk -- The name of the help center. The name can be found in the url of the help center. https://[help_center_name].zendesk.com/
self.user -- Email address for your Zendesk account + the word /token
self.pwd -- API token for your Zendesk account

Creating Topic Subscriptions:

This script creates a subscription to every existing Community Forum Topic to the specified user_ids. Users will get notified of new articles created in each section and any comments posted. 

Edit create_topic_subscriptions.py

If you don't want the user to get notified of new comments, set "include_comments" to False.


self.user_ids -- takes a list of user ids
self.zendesk -- The name of the help center. The name can be found in the url of the help center. https://[help_center_name].zendesk.com/
self.user -- Email address for your Zendesk account + the word /token
self.pwd -- API token for your Zendesk account

# Overview

This script migrates a UserVoice KnowledgeBase, housing it as a category in a ZenDesk Help Center.

### href Migration

It migrates the intra-knowledgebase hrefs in the articles as you'd expect.

### img Migration

It doesn't touch the img src links, leaving those on UserVoice and elsewhere.

# Setup

    pip install uservoice
    pip install requests

# Usage

    python transferknowledgebase.py {uv_subdomain} {uv_api_key} {uv_api_secret} {zd_subdomain} {zd_email} {zd_api_token} {zd_destination_category_name}

# Updating the Script

Read up on the zendesk rest API and python examples to learn to edit the script.

```
sample dict to move from UserVoice

{
'formatted_text': '<img src="https://foobar.uservoice.com/assets/91625817/SwipeUp.jpg"> 
'title': 'eh', 
'position': 2, 
'topic': {'id': 32361, 'name': 'Manaacks'},
'updated_by': {'name': 'Ain', 'title': 'Adventurport', 'url': 'http://foobar.uservoice.com/users/-ain', 'created_at': '2015/08/31 16:25:21 +0000', 'updated_at': '2016/01/06 12:44:17 +0000', 'id': 99331452, 'avatar_url': 'https://secure.gravatar.com/avatar/6da6d5ce7bd589a68c119.png', 'karma_score': 0, 'email': 'ain@foobar.com'}, 'title': 'Troubleshooting', 'url': 'http://foobar.uservoice.com/knowledgebase/articles/171267-troubleshooting', 'text': "Troubleshooting\n\n  If foobar can't locate a GPS signal, follow these instructions to make sure location services are turned on.not work if you are in a car or if you are near metal or\n    magnetic things.\n  \n\n  &nbsp;", 'created_at': '2013/02/26 01:05:14 +0000', 'question': 'Troubleshooting', 'updated_at': '2015/11/30 06:33:33 +0000', 'answer_html': '<h1>Troubleshooting<br></h1>\n\n  <br>If foobar can\'t locate a GPS signal, <a href="http://help.foobar.com/knowledgebase/articles/171276-gisn-t-lo">follow these instructions</a> to make sure location services are turned on.<br>\n\n\n\n\n\n\n\n<p class="p1"><span class="s1">If location services are turned on, force close the app completely by double tapping the Home button and then swiping up the  GPS window.</span></p><br><span><img src="https://foobar.uservoice.com/assets/91625817/SwipeUp.jpg"></span><br>\n\n            <br>If shutting down the app doesn\'t work, try restarting your\n    phone.<br><br><br>Please note:\n\n  <ul>\n    <li>The compass will not work if you are in a car or if you are near metal or\n    magnetic things.</li>\n  </ul>\n\n  <p>&nbsp;</p><div></div>', 'topic': {'id': 28921, 'name': 'Troubleshooting'}, 
'uses': 7, 
'published': True, 
'instant_answers': 4, 
'path': '/knowledgebase/articles/171267-troubleshooting', 
'id': 171267
}


sample dict to create on ZenDesk

{
body:  '<img src="https://foobar.zendesk.com/hc/en-us/article_attachments/204747168/add_sources_1.jpg">
name:  'Adding and Managing Map Sources', 
title: 'Adding and Managing Map Sources', 
url:   'https://foobar.zendesk.com/api/v2/help_center/en-us/articles/216117167-Adding-and-Managing-Map-Sources.json', u'vote_sum': 0, u'created_at': u'2016-01-06T16:32:38Z', u'source_locale': u'en-us', u'comments_disabled': True, u'html_url': u'https://foobar.zendesk.com/hc/en-us/articles/2161d7r67-Adding-and-Managing-Map-Sources',
u'updated_at': u'2016-01-06T18:39:59Z', 
u'section_id': 203d37127, 
u'label_names': [], 
u'locale': u'en-us',
u'vote_count': 0, 
u'draft': False, 
u'promoted': False, 
u'position': 0, 
u'author_id': 392d70d078, 
u'outdated': False, 
u'id': 216dd167
}
```# Download and Create JSON for Zendesk Help Center

The localization and PDF utils use the generated JSON files.

# Set PythonPath

    export PYTHONPATH=$PYTHONPATH:..
# Localizing Zendesk Help Center

## Install Requirements

    brew install python3
    pip install -r requirements.txt    
    export PYTHONPATH=$PYTHONPATH:..

## Config Gengo and Zendesk

    cp _sample_project_settings.py project_settings.py

## Config for One Article at a Time

To do one article at a time, you should configure these settings:

 * GENGO_PUBLIC_KEY 
 * GENGO_PRIVATE_KEY
 * ZENDESK_EMAIL
 * ZENDESK_SUBDOMAIN
 * ZENDESK_TOKEN
 * DATA_CONFIG = { unlocalized_words: [], 'locales_to_translate': [] }

## Config for Batch Localizing Articles/Sections/Categories

If you want to do more than one article at a time, set up the rest of DATA_CONFIG in project_settings.py.

## Usage

Retrieve one article from ZenDesk, and package to send to Gengo:

    python3 ZenDeskLocalizer.py package-article ZENDESK_ID    

Retrieve a batch of articles based on project_settings.py files from ZenDesk, and package to send to Gengo:

    python3 ZenDeskLocalizer.py package    

Post to Gengo:

    python3 ZenDeskLocalizer.py post    

Check your dashboard on Gengo for the order to complete (can take days), then retrieve the files:

    python3 ZenDeskLocalizer.py retrieve    

Post the translations to  ZenDesk:

    python3 ZenDeskLocalizer.py update    
This script searches for all articles, sections and categories in an existing Zendesk Help Center and copies them to a new one

To use this script:
Clone the repo
pip install requests

Usage:

Edit clone.py, replacing these exisiting variables with your account info:

self.origin_brand -- The name of the help center you want to copy from. The name can be found in the url of the help center. https://[help_center_name].zendesk.com/
self.new_brand -- The name of the help center you want to copy to. The name can be found in the url of the help center. https://[help_center_name].zendesk.com/

self.origin_username - Email address for your origin Zendesk account + the word /token
self.origin_token -- API token for your origin Zendesk Account

self.new_username - Email address for your new Zendesk account + the word /token
self.new_token - API token for your new Zendesk Account

(origin and new creditials will be the same if you are copying between brands on the same account)

Notes:
This script only copies the URL for photos. If you delete the photos from the origin help center, they will break in the new one# Install wkhtmltopdf

Because the pip install didn't work for me, install a static binary from http://wkhtmltopdf.org/

Install other Python requirements

    pip install -r requirements.txt
    export PYTHONPATH=$PYTHONPATH:..

# Config

If you didn't already do this using this localize script, you need to clone and update the config file.

    cp ../localize/_sample_project_settings.py ../localize/project_settings.py

# Install Chinese Fonts (if on Ubuntu Linux, Mac has these by default)

Thanks for help from [this blog post](http://cnedelcu.blogspot.com/2015/04/wkhtmltopdf-chinese-character-support.html).

    apt-get install fonts-wqy-microhei ttf-wqy-microhei fonts-wqy-zenhei ttf-wqy-zenhei 

Note: package names might be different if you aren't under Ubuntu (try apt-cache search ... to search for packages)
Then, run this command to update the font cache:

    fc-cache -f -v

# Generate and Post PDFs

    python ZendeskPDFMaker.py create  
    python ZendeskPDFMaker.py post 
