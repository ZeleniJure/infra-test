# Consul Agent role
Installs a Consul cluster to provided hosts.
The only mandatory variable is the number of servers expected in the cluster (`bootstrap_expect`).

Consul Agent configuration may be adjusted and parametrized, since it is generated when the role is applied.
This way makes it easy to add support for various configurations (e.g. installing clients)

Currently role supports installing consul servers only.
There's no monitoring :/

## Quick start
Following is an example playbook which uses this role to install into simulator hosts:
```yaml
---
- name: Install Consul to the local simulator
  hosts: "{{ target | default('docker') }}"
  roles:
    - consul-agent
  vars:
    # Because I don't know how to format this to be int instead of string when scaffolding :/
    bootstrap_expect: 3
  tasks:
   - name: Start service
     command: "echo Starting Consul..."
     notify:
       - start consul

```

## Disclamer
Consul configuration here would need some love....
There's no encryped gossip, we are assuming TSL is terminated on the load balancer, ....
