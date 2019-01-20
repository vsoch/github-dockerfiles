##Docker Drupal Mysql

Derivated from mysql 5.6

### Description

```
Operating system: ubuntu:14.04
Mysql: 5.6
```

The server is automatically configured using a set of default and optimized configurations, which resides on /etc/mysql/conf.d/.


File: custom.cnf

```
max_allowed_packet = 512M
key_buffer_size = 128M
max_allowed_packet = 128M
table_open_cache = 64
sort_buffer_size = 64K
read_buffer_size = 256K
read_rnd_buffer_size = 256K
net_buffer_length = 2K
thread_stack = 240K
query_cache_type = 1
query_cache_size = 256M
query_cache_limit = 32M
max_heap_table_size = 92M
join_buffer_size = 4M
thread_cache_size = 4
```

innodb.cnf

```
innodb_buffer_pool_size = 1024M
innodb_additional_mem_pool_size = 20M
innodb_log_file_size = 256M
innodb_log_buffer_size = 32M
innodb_flush_log_at_trx_commit = 0
innodb_doublewrite = 0
innodb_support_xa = 0
innodb_file_per_table = 1
```





