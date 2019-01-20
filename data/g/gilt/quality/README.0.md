To add a new database migration script:

  1. Make sure you have head of master:
     git checkout master
     git fetch
     git rebase origin/master

  2. Create a local branch for your change
     git checkout -b tmp

  3. Create a file containing your upgrade script - e.g. new.sql

  4. Add your upgrade script
     /usr/local/lib/schema-evolution-manager-0.9.21/bin/sem-add ./new.sql
     git commit -m 'Add upgrade script to ...' scripts

  5. Push change

To upgrade your local postgresql database:

  sem-apply --host localhost --name sample_development --user postgres

or use the wrapper script:

  ./dev.rb

For more information on the schema evolution manager tools, look at
schema-evolution-manager/README.md
