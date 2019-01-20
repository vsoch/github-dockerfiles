# Overview of Process

**Create a replica**, turn off replication, turn off backups. end up with standalone db instance

**Break tables up into 2 types**. "isolated" (small) tables and "dependent" (large) tables:
*   "isolated" tables should be small and are  simply copied from the replica to the sqldump
*   "dependent" tables are too big to copy so we hand-pick records to dump

Script requires a **"table_config.rb"** file with the names of the dependent tables (ones to not copy)

1. copy dependent tables into tmp_db
2. copy isolated tables into tmp_db
3. create a mysql dump (.mysql.gz) file of the tmp_db


# [TODO] How I came about this process
0. Found this article, step 3 sounded like a great approach http://mechanics.flite.com/blog/2012/11/15/3-methods-to-extract-a-subset-of-your-data-using-mysqldump/
1. take a look at all tables that are bigger than 1GB
determine which ones you typically need
in our case users and items (and their associated info) is what we need most

2. write a script to join all the data for each record you care about and create a dump
concatenate both dumps

``` sql
size_command = "SELECT
     table_name AS 'Table', round(((data_length + index_length) / 1024/ 1024), 2) 'Size in MB'
FROM information_schema.TABLES
WHERE table_schema = 'shop_2_28_2017'
ORDER BY (data_length + index_length) DESC;"
```

users
  orders
  cash_credits
    cash_credit_debits
      cash_credits
  invitations
    users
  orders
    order_transactions
    order_products
    addresses
    order_addresses

items
  item_pails
  photos
  item_prices
  characteristics

### Tables using > 100 MB of space

| Database  | Table                | Size in MB |
|-----------|----------------------|------------|
| shop_1_16 | users                |    6346.73 |
| shop_1_16 | items                |    6281.83 |
| shop_1_16 | cash_credits         |    4644.91 |
| shop_1_16 | invitations          |    3135.34 |
| shop_1_16 | order_transactions   |    2898.22 |
| shop_1_16 | characteristics      |    2742.00 |
| shop_1_16 | order_products       |    2543.19 |
| shop_1_16 | item_pails           |    1878.00 |
| shop_1_16 | photos               |    1798.56 |
| shop_1_16 | addresses            |    1725.75 |
| shop_1_16 | orders               |    1372.63 |
| shop_1_16 | order_addresses      |    1163.66 |
| shop_1_16 | cash_credit_debits   |    1056.19 |
| shop_1_16 | item_prices          |     758.64 |
| shop_1_16 | assets               |     716.53 |
| shop_1_16 | item_scores          |     696.20 |
| shop_1_16 | concierge_bags       |     375.73 |
| shop_1_16 | shipments            |     362.22 |
| shop_1_16 |concierge_bag_requests|     223.41 |
| shop_1_16 | item_assets          |     211.83 |
