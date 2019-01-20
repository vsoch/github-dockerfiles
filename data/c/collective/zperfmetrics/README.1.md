A minimal graphite installation with graphite-api instead of graphite-web. The container runs two running processes (carbon-cache and gunicorn) managed by supervisord.

### Usage

    docker run -ti -d --name graphite -v ./conf:/opt/graphite/conf  -v ./data:/opt/graphite/storage/whisper -P ennexa/graphite

### Ports
The image exposes 4 ports

- Graphite-Api  : 8000
- Carbon : 2003/2004/7002

### Volumes
The image exports 2 volumes

- Carbon configuration directory at `/opt/graphite/conf`
- Whisper data location at `/opt/graphite/storage/whisper`

