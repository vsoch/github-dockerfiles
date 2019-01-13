# prom2teams

This image installs [prom2teams](https://github.com/idealista/prom2teams) and exposes some of its configuration via environment variables.

## Environment Variables

| Name                  | Default                         |
|-----------------------|---------------------------------|
| PROM2TEAMS_CONFIGPATH | /home/prom2teams/prom2teams.ini |
| PROM2TEAMS_CONNECTOR  | [None]                          |
| PROM2TEAMS_HOST       | 0.0.0.0                         |
| PROM2TEAMS_LOGLEVEL   | INFO                            |
| PROM2TEAMS_PORT       | 8089                            |

## Kubernetes

There are some pre-baked k8s configs in [k8s](k8s).