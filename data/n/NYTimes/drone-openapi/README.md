# drone-openapi

### Publish Open API spec files from a Drone pipeline

This plugin accepts a team name along with a valid Open API spec file and it will post the given information to the given uploader_url.

### Drone versions

This plugin supports Drone 0.4 and 0.6+ (0.5 is deprecated).

The examples below are for secrets in the 0.4 format, where the GCP Service Account json must be passed to the `key` parameter in .drone.yml, using the `$$SECRET_NAME` notation.

For Drone 0.6+, the plugin expects credentials in the `OPENAPI_API_KEY` environment variable. See the [official documentation](http://docs.drone.io/manage-secrets/). Either: 
  - Name the secret `OPENAPI_API_KEY` and inlclude it in the `secrets` block, or
  - follow "Alternate Names" in the doc, setting the `target` to `OPENAPI_API_KEY`.


### Basic example config to publish the puzzles.yaml spec file under the games team:

	notify:
	  openapi:
        team: games
        spec: puzzles.yaml
	    key: $$OPENAPI_KEY
		uploader_url: https://openapi-repo.example.com/uploader
	    when:
	      event: tag
