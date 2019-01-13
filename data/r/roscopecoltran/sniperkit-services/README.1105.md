All this image does it track docker:dnid, add zabbix, install s6 add a few packages for easier navigation and update the Docker Daemon to commence in experimental mode to support --squash --compress and prune functions and switch to overlay2 filesystem.

However, there are some environment variables:

Below is the complete list of available options that can be used to customize your installation.

| Parameter         | Description                                                    |
|-------------------|----------------------------------------------------------------|
| `DEBUG_MODE`      | Enable Debug Mode - Default: `FALSE`                            |
| `ENABLE_CRON`     | Enable Cron - Default: `TRUE`                                   |
| `ENABLE_SMTP`     | Enable SMTP services - Default: `TRUE`						|
| `ENABLE_ZABBIX`   | Enable Zabbix Agent - Default: `TRUE`                           |
| `TIMEZONE`        | Set Timezone - Default: `America/Vancouver`                     |

If you wish to have this send mail, set `ENABLE_SMTP=TRUE` and configure the following environment variables. See the [MSMTP Configuration Options](http://msmtp.sourceforge.net/doc/msmtp.html) for further information on options to configure MSMTP

| Parameter         | Description                                                    |
|-------------------|----------------------------------------------------------------|
| `SMTP_HOST`      | Hostname of SMTP Server - Default: `postfix-relay`                            |
| `SMTP_PORT`      | Port of SMTP Server - Default: `25`                            |
| `SMTP_DOMAIN`     | HELO Domain - Default: `docker`                                   |
| `SMTP_MAILDOMAIN`     | Mail Domain From - Default: `example.org`						|
| `SMTP_AUTHENTICATION`     | SMTP Authentication - Default: `none`                                   |
| `SMTP_USER`     | Enable SMTP services - Default: `user`						|
| `SMTP_PASS`   | Enable Zabbix Agent - Default: `password`                           |
| `SMTP_TLS`        | Use TLS - Default: `off`                     |
| `SMTP_STARTTLS`   | Start TLS from within Dession - Default: `off` |
| `SMTP_TLSCERTCHECK` | Check remote certificate - Default: `off` |

See The [Official Zabbix Agent Documentation](https://www.zabbix.com/documentation/2.2/manual/appendix/config/zabbix_agentd) for information about the following Zabbix values

| Zabbix Parameters | Description                                                    |
|-------------------|----------------------------------------------------------------|
| `ZABBIX_LOGFILE` | Logfile Location - Default: `/var/log/zabbix/zabbix_agentd.log` |
| `ZABBIX_LOGFILESIZE` | Logfile Size - Default: `1` |
| `ZABBIX_DEBUGLEVEL` | Debug Level - Default: `1` |
| `ZABBIX_REMOTECOMMANDS` | Enable Remote Commands (0/1) - Default: `1` |
| `ZABBIX_REMOTECOMMANDS_LOG` | Enable Remote Commands Log (0/1)| - Default: `1` |
| `ZABBIX_SERVER` | Allow connections from Zabbix Server IP - Default: `0.0.0.0/0` |
| `ZABBIX_LISTEN_PORT` | Zabbix Agent Listening Port - Default: `10050` |
| `ZABBIX_LISTEN_IP` | Zabbix Agent Listening IP - Default: `0.0.0.0` |
| `ZABBIX_START_AGENTS` | How many Zabbix Agents to Start - Default: `3 | 
| `ZABBIX_SERVER_ACTIVE` | Server for Active Checks - Default: `zabbix-proxy` |
| `ZABBIX_HOSTNAME` | Container hostname to report to server - Default: `docker` |
| `ZABBIX_REFRESH_ACTIVE_CHECKS` | Seconds to refresh Active Checks - Default: `120` |
| `ZABBIX_BUFFER_SEND` | Buffer Send - Default: `5` |
| `ZABBIX_BUFFER_SIZE` | Buffer Size - Default: `100` |
| `ZABBIX_MAXLINES_SECOND` | Max Lines Per Second - Default: `20` |
| `ZABBIX_ALLOW_ROOT` | Allow running as root - Default: `1` |
| `ZABBIX_USER` | Zabbix user to start as - Default: `zabbix` |


