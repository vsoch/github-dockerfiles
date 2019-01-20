Automatic Kelp Recognition
---

This is attempt to reduce the overall volume of data needed to be process by Floating Forests (www.floatingforests.org).

What This Does
---

The script takes all the JPGs in the directory and searches them for kelp. If it finds any, it creates a filename*_kelped*.jpg version. It works on temporary PNG duplicates of the JPGs, so they will not be altered.

The script scans each image's pixels for contiguous regions of kelp-colour. When it finds such pixels, it checks to see if they are bordered by water-coloured pixels. If they are, these regions are recorded as kelp in *kelp_results.csv* and marked on the *_kelped* images in green.

All files are checked for kelp, water, and cloud. True/false values for each are recorded in *file_results.csv*.

Simplistically, you can adjust the *@types* hash in the script, which changes the definition of the colours of cloud, water, and kelp.


Usage and Requirements
---
You'll need a recent Ruby version and the ChuknyPNG gem (chunky_png).

`ruby find-kelp.rb` will start going through any JPGs. Be sure to remove previous *_kelped* files before running the script to avoid endless *_kelped_kelped* files forming.Floating Forests Data Pipeline
---

This readme is intended to give an overview of the process used to create data for use on http://www.floatingforests.org/. The process tansforms both Landsat 4/5, 7 and 8 raw scenes into small jpegs suitable for the classification interface.

It's worth noting the scripts were not originally intended to be open-source, and thus should be treated as something more like a guideline on how we did it, rather than a set of ready-to-use scripts for your own processing. Basically, use at your own risk.

The coastline detection and image-splicing was created by Chris Snyder, the USGS (LANDSAT) API functions and some modifications as by Robert Simpson.

ImageMagick, PostGres 
---

All need to be working. I recommend Homebrew for Imagemagick. I recommend http://postgresapp.com/ for Macs users.

Setup database
---

Coastline detection is done via the PostGIS plugin for Postgres. Before beginning, you'll need to have Postgres/PostGIS installed on your machine. See above.

`create database kelp_world;`   
`psql kelp_world < world.pg`

Install gems
`bundle install`

Usage
---

Create a api-details.rb file with correct USGS username and password. See -example file.

Modify the @places hash in the get-data.rb script to point it at the required lat/long and region. Then run

`ruby get-data.rb`

It will create subdirectories for the created data and directories within each location for the LANDSAT scenes.

It will then process the downloaded data and create a Zooniverse manifest.json file, ready for upload to S3.

Example Docker usage:

```
docker run -it --rm -v /data/:/data/ -e "DATA_DIR=/data/" -v $PWD/config/api-details.rb:/src/api-details.rb -v $PWD/config/db.yml:/src/db.yml zooniverse/kelp-import-pipeline ruby get-data.rb
```

Future Improvements
---

kelp-recognition.rb still seems to think some clouds are kelp.

Use a different method for cloud detection in the get-data.rb script? (possibly check out the kelp-recongnition code).

