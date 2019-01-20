

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Falterway%2Farm-prestashop-docker-cluster%2Fmaster%2Fazuredeploy.json" target="_blank">
    <img src="http://azuredeploy.net/deploybutton.png"/>
</a>
<a href="http://armviz.io/#/?load=https%3A%2F%2Fraw.githubusercontent.com%2Falterway%2Farm-prestashop-docker-cluster%2Fmaster%2Fazuredeploy.json" target="_blank">
    <img src="http://armviz.io/visualizebutton.png"/>
</a>

**Attention ! Don't use $ or space in variables **


There is no escaping :(


<pre>
                                                                                                 
                                                                                                 
                                                                                                 
                                                                                                 
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃                                    ARM                                                 ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
                                                                                                 
                                                                                                 
                                                          ┌──────────────────────┐               
                                                          │       node #1        │               
                                                          │                      │               
                                                          │ ┌──────────────────┐ │               
                                                          │ │   Docker swarm   │ │               
                                                          │ │     manager      │ │               
          ┌──────────────────────┐                        │ │         ┌──────┐ │ │               
          │       JumpBox        │                        │ │         │      │ │◀┼──┐            
          │                      │                        │ │         │ apps │ │ │  │            
          │ ┌──────────────────┐ │                        │ │         │      │ │ │  │            
          │ │      Docker      │ │                        │ │         └──────┘ │ │  │            
          │ │                  │ │                        │ └──────────────────┘ │  │            
          │ │         ┌──────┐ │ │                        │ ┌──────────────────┐ │  │            
          │ │         │      │ │ │                        │ │push              │ │  │            
          │ │         │consul│◀┼─┼────────────────────────┼─│ip, hostname,     │ │  │            
          │ │         │      │◀┼─┼──────────┐             │ │#node             │ │  │            
          │ │         └────▲─┘ │ │          │             │ └──────────────────┘ │  │            
          │ │              │   │ │          │             │ ┌──────────────────┐ │  │            
          │ │              │   │ │          │             │ │pull              │ │  │            
          │ │              │   │ │         ┌┼─────────────┼▶│id_rsa            │ │  │            
          │ └──────────────┼───┘ │         ││             │ │id_rsa.pub        │ │  │            
          │ ┌──────────────┼───┐ │         ││             │ └──────────────────┘ │  │            
          │ │key generation│   │ │         ││             └──────────────────────┘  │            
          │ │id_rsa        │───┼─┼─────────┘│                                       │            
          │ │id_rsa.pub    ────┼─┼─────────┐│                      ┌───┐        swarmkit         
          │ └──────────────────┘ │         ││                      │ 2 │         cluster         
          │                      │         ││                      └───┘            │            
          │                      │         ││             ┌──────────────────────┐  │            
          └──────────────────────┘         ││             │       node #2        │  │            
                                           ││             │                      │  │            
                   ┌───┐                   ││             │ ┌──────────────────┐ │  │            
                   │ 1 │                   ││             │ │   Docker swarm   │ │  │            
                   └───┘                   ││             │ │      worker      │ │  │            
                                           ││             │ │         ┌──────┐ │ │  │            
      ╔═══════════════════════════════════╗││             │ │         │      │ │ │  │            
      ║Workflow:                          ║││             │ │         │ apps │ │ │  │            
      ║- jumpbox created                  ║││             │ │         │      │ │ │  │            
      ║  - create docker server           ║││             │ │         └──────┘ │ │  │            
      ║  - spawn consul container         ║││             │ └──────────────────┘ │◀─┘            
      ║  - ssh keys generation            ║││             │ ┌──────────────────┐ │               
      ║  - put keys in consul             ║││             │ │push              │ │               
      ║                                   ║│└─────────────┼─│ip, hostname,     │ │               
      ║- #n docker nodes created          ║│              │ │#node             │ │               
      ║  - pull private orchestration ssh ║│              │ └──────────────────┘ │               
      ║keys from consul                   ║│              │ ┌──────────────────┐ │               
      ║  - create docker server           ║│              │ │pull              │ │               
      ║  - register ip, role, #n, in      ║└──────────────┼▶│id_rsa            │ │               
      ║consul                             ║               │ │id_rsa.pub        │ │               
      ║  - create swarm cluster           ║               │ └──────────────────┘ │               
      ║  - deploy application             ║               └──────────────────────┘               
      ║- take a coffee                    ║                                                      
      ╚═══════════════════════════════════╝                        ┌───┐                         
                                                                   │2' │                         
                                                                   └───┘                         
</pre>