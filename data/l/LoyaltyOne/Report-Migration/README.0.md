### Deploy Service stack manually

* **Prerequisites:**
	* Install [ecs-service](https://www.npmjs.com/package/ecs-service).

```bash
ecs-service deploy <stack-name> <app-version> \
templates/service.json \
dev.params.json \
-e dev.env \
-t dev.tags.json \
-r us-east-1 \
-p assumed_role
```
##### Example

```bash
ecs-service deploy dev-report-migration 0.1.2  \
templates/service.json \
dev.params.json \
--env-file dev.env \
--tag-file  dev.tags.json \
-r us-east-1 \
-p assumed_role 
```The DBToFile.py program converts database info into output files.  

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



