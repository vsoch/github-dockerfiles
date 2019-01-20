
# Getting Started w/ Mixtapes DB
1.  Navigate to your project root directory and copy the contents of this repository to that location.
2.  Create a copy of `make_env.dist` and rename it to `make_env`.  Update with your project specific information.
3.  `make build`
4.  `make start`
4.  `make init`

# Success
1.  Consider downloading and using RoboMongo as a database administration GUI.  It's free!  https://robomongo.org/download
2.  You will be able to successfully connect to your database on port `27017` using the admin login credentials you provided in your `make_env` file.
3.  Data is volume mapped to the `/data` folder in the project.  This will allow you to rebuild your contianer without loosing your data.  The contents of this folder should never be commited back to your project repository.


# Further Reading

Manual for MongoDB configuration:  https://docs.mongodb.com/manual/reference/configuration-options/
