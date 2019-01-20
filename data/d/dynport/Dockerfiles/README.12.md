# docker-gc

## Usage

	# delete all exited containers and ubuntu images older than 7 days
	docker run -i -v /var/run/docker.sock:/var/run/docker.sock -e IMAGE_PREFIX=ubuntu: -e MAX_AGE=7 quay.io/dynport/docker-gc
