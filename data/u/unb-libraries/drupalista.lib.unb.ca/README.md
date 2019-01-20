# Drupalista
## Introduction
Interact with CargoDock deployed Kubernetes hosted Drupal containers via Slack.

![Drupalista uli](img/drupalista-uli.png "Drupalista uli")

## Required environment variables

 * ```SLACK_TOKEN``` : The slack token used to connect drupalista to your slack instance.
 * ```KUBE_NODE``` : The IP or hostname of the kubernetes API node.
 * ```KUBE_NODE_PORT``` : The port of the kubernetes node to use for API access.
 * ```KUBE_ADMIN_CA_KEY``` : The admin CA to assert to the kube client API.
 * ```KUBE_ADMIN_ADMIN_PEM``` : The admin cert to assert to the kube client API.
 * ```KUBE_ADMIN_CA_KEY``` : The admin cert key to assert to the kube client API.

## Commands
 * ```list_sites``` : List instances controllable by Drupalista.
 * ```clear_cache``` : Rebuild the cache of a specific instance
 * ```uli``` : Provide a ULI link for the specified instance
 * ```hostfile``` : Deliver a hostfile to use for development purposes (if domains are not resolved to k8s cluster)

## License
 - Drupalista is licensed under the MIT License:
   - http://opensource.org/licenses/mit-license.html
 - Attribution is not required, but much appreciated:
   - `Drupalista by UNB Libraries`
