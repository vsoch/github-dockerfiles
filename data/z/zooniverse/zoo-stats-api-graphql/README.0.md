# Zoo_stats Benchmarking

### Results
Database benchmarking performed as below with database sizes of 100K, 200K, 300K, 10M and 100M. Results saved in `./results folder` both before and after addition of event_type/user_id and event_type/project_id compound indexes. Numbering is as follows: "20": 100K and 200K database size results; "21": 100K, 200K, 300K and 10M database size results; "22": 100K, 200K, 300K, 10M and 100M database size results. Yes and No refer to use (or not) of two concurrent database writers. 

__Compare `./results/no_Indexes/test_output-22-yes_writes.png` with `./results/with_Indexes/test_output-22-yes_writes.png` to see the effects of adding indexes__

### Generating data files
1. Generate maximum database size CSV file
    * Edit `create_csv_data.rb` to match required attributes
    * Run `ruby create_csv_data.rb` (*__Warning: ~200GB file per 1 billion rows__*)

0. (Independent) Split main file into test files
    * Edit `writing_script_non-appending.sh` to match required number of files and the end line of each file
    * Currently setup to have 15 files, cumulatively 100K, 200K, 300K, 400K, 500K, 750K, 1M, 2M, 5M, 10M, 20M, 50M, 100M, 500M, 1B (each file contains the number of rows indicated)
    * Run `./writing_script_non-appending.sh`(*__Warning: Ensure free storage space about equal to original file__*)

0. (Cumulative) Split main file into test files
    * Edit `writing_script.sh` to match required number of files and the start and end line of each file
    * Currently setup as above (each file contains difference between it and the previous file)
    * Run `./writing_script.sh` (*__Warning: Ensure free storage space equal to original file__*)

0. Add below to timescale in docker-compose.yml, where {PATH_TO_DATA} contains the above generated data
```
volumes:
  - {PATH_TO_DATA}:/mnt/
```


### Running tests (Setup for Independent test files)
1. Edit testing_script.sh `file_array=`, `sizes=`, `sizes_i=` (data file names and sizes) and `path=` (path to data files)

0. Add or Edit list of inputs (i.e. `quick_list=(0 1)`)
    * This will run tests on the files at the indexes 0 and 1 in `file_array`
    * Can run database sizes multiple times, with multiple entries in list (allows replication of cold-runs)

0. Run `./testing_script.sh {Number of repeats} {yes/no}` (yes/no concurrent database writers)
    * Requires manual changing of input directory
    * Iterates through set list
    * Resets database
    * Imports from CSV file with name in `file_array`
    * Stops and starts database to ensure cold startup
    * Runs database tests either of below

Test without writers
* writes is 'no'
* `run_database_tests.rb` is run and given database_size and number of repeats (see below)

Test with concurrent database writers
* writes is 'yes'
* Foreman is run (given database_size, temp file and number of repeats as environmental variables)
* Foreman starts processes listed in Procfile
* writer1/2: two independent runs of `generate_events.rb {Starting event_id}` which adds random events using `../seeds/generator_class.rb` (*__Warning: These generated events are actually inserted into the database__*)
* test: run `run_database_tests.rb > $temp_file` (output to temp_file)
* After test run, temp_file is appended to output_file

`run_database_tests.rb`
* Gets database_size (only used for CSV output) and repeat_count from arguments or environmental variables
* Notification subscription setup (need to subscribe to ActiveSupport notifications in order to access the reported SQL load time. This time is printed when using rails/console)
* Runs tests repeat_count times, first run is cold-run
* Uses Timescale time_bucket query for specific random user, both comment and classifications are run separately
* Parses recorded notifications for those matching the queries and sums their duration
* This data could be split if desired


### Running tests using current database
To save time resetting the database, use `./no_db_refresh_testing_script.sh {Number of repeats} {yes/no}` (yes/no concurrent database writers)
* Runs as above without Iteration or Database resetting/importing
* Requires manual addition of previously generated output file (perhaps already including smaller database sizes) and setting of current database size


### Generating graphs
Run `python3 generate_graphs.py`
* Generates line graph for each CSV file in the `./testing_results/` directory
* Each graph is shown and saved as PNG file
This uses a tool called [`lambda-uploader`](https://github.com/rackerlabs/lambda-uploader)
to maintain the Lambda script.

## Install

```
pip install -r requirements.txt
```

## Deployment

```
lambda-uploader --config zoo-stats-api-graphql_staging.json
```

## Useful settings in that config file

* The name is just a unique identifier for this specific lambda function
* The role specified in it must have access to the Kinesis stream
* The handler consists of two parts. The first is basically just the filename
  of the python script (without extension). The second is the name of the
  function inside that Python file that should be called.  Here it's called
  `zoo-stats-api-graphql.py` with a function `lambda_handler`, therefore the handler
  field is set to `zoo-stats-api-graphql.lambda_handler`
