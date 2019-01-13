# Assignment: Create Stack with Secrets

* Let's use our Drupal compose file from last assignment (compose-assignment-2)
* Rename image back to official `drupal:8.2`
* Remove `build:`
* Add secret via `external:`
* use environment variable `POSTGRES_PASSWORD_FILE`
* Add secret via cli `echo "<pw>" | docker secret create psql-pw -`
* Copy compose into a new yml file on you Swarm node1

# Solution

```
echo "mypass" | docker secret create psql-pw -

docker stack deploy -c docker-compose.yml drupal
```
