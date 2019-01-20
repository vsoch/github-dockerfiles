# Engine Yard Container Services Examples

Here are a few examples that show how Engine Yard Container Services
can be used to deploy containers in EY Cloud.

1. [simplesvc](./simplesvc)
2. [spina](./spina)
3. [rails_activejob](./rails_activejob)

## Container Services in EY Cloud

To access the Container Services feature in EY Cloud, select "Container Service Definitions" in the "Tools" menu.
EY Cloud provides a private Docker registry. It can be accessed through the "Docker Repositories" menu item in the "Tools" menu.

## General Setup

### Load Balancing

The simplesvc and spina examples use an App Load Balancer.
Make sure you have one setup in the Region and Network you'll use for the examples.
