Docker image for running subscriptions

Build image using

    docker build -t p2pu/subscribe .

Run image using

    docker run --name subscribe --link some-postgres-container:postgres -p 8000:80 -e DATABASE_URL=postgres://user:password@postgres:5432/db-name -d p2pu/subscribe

Requirements:

- Postgres db running in seperate image.
