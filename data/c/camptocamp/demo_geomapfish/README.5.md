sudo -u postgres pg_dump --schema-only --dbname=${db} --schema=geodata > 15-schema-geodata.sql
sudo -u postgres pg_dump --schema-only --dbname=${db} --schema=edit > 16-schema-edit.sql
sudo -u postgres pg_dump --data-only --dbname=${db} --schema=${schema} > 18-data-main.sql
sudo -u postgres pg_dump --data-only --dbname=${db} --schema=${schema}_static > 19-data-main-static.sql
#sudo -u postgres pg_dump --format=c --table=planet_osm_point --dbname=osm > osm.dump
sudo -u postgres pg_dump --insert --table=planet_osm_point --dbname=osm > osm.sql
