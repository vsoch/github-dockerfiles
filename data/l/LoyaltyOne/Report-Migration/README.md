# Report-Migration
Contain all scripts related to AMMIS Report migration created by Data Ninjas

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

The DBToFile program converts PostgreSQL info into output files. 

Installation:  
Note: Installation depends on if Internet Connectivity is possible - this may be revised before going to integration environment.  
Install PostgreSQL v. 11.1 client - run: sudo apt-get install postgresql  
Install Python v. 3.7.1 - check if it's already installed with: python --version  
If not, then run: sudo apt-get install python3  
Install Psycopg2 - run: pip install psycopg2  
Install Pycryptodome - run: pip install pycryptodome  
Create the report.tbl_gen_params and report.tbl_report_params tables using the two DDLs found in /Scripts/DDLs/Inserts.  

Using the Program:  
Run the .bat file corresponding to the reports you want to generate. These .bat files should contain a simple command which runs DBToFile.py (report id). The reports should generate in the Output folder. This report id corresponds to the report_id from the report.tbl_gen_params table.

# Docker
## Build locally
```
docker build -t report_migration .
```

## Run locally foreground
```
docker run -it --rm --name report_migration_local --env OPSWISE_SERVER_HOST="opswise-dev.loyalty.com" --env OPSWISE_SERVER_IP="172.25.9.181" report_migration:latest bash
```

## Run locally background
```
Start docker container in background
docker run --detach -it --rm --name report_migration_local --env OPSWISE_SERVER_HOST="opswise-dev.loyalty.com" --env OPSWISE_SERVER_IP="172.25.9.181" report_migration:latest bash

Get inside the background container
docker exec -it report_migration_local bash

```

## Kill background running container
```
Kill
docker kill report_migration_local
```

# Run opswise trigger with proper environment variables
Note: take care of the `.` at the start of the command - it shows that execute the environment file in same thread
```
. /docker.env && echo "run command here"
```
