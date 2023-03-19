# Task: Deploy Consul

Infrastructure deployment for VMs using [Ansible](http://docs.ansible.com/).

Repository contains [simulated VMs](#simulated-vms-as-local-playground) aganst which you may run the deployment playbooks. Linting and automation is out of scope of this repo.

Also check the [community version](https://github.com/ansible-community/ansible-consul/)!

## Quick start: Setup and install Consul to local simulated VMs

1. Setup and activate python virtual environment.

        python3 -m venv venv
        source venv/bin/activate
2. Make sure python requirements are installed: `pip install -r requirements.txt`
3. Start simulation VMs:

        docker compose up -d
  
    > NOTE that the simulator generates new SSH keys each time the docker image is rebuilt, thus, when you ssh into containers, you will get your `known_hosts` polluted. You should clean it up after use...

4. Move to the ansible folder, list hosts and ping simulator VMs

        cd ansible
        ansible -i inventory/simulator.yaml all --list-hosts
        ansible -i inventory/simulator.yaml all -m ping
5. Install Consul: `ansible-playbook -i inventory/simulator.yaml playbooks/local-simulator.yaml`
6. Try to connect with a consul client(`docker exec consul-client consul members`) should return something like:

        Node     Address             Status  Type    Build   Protocol  DC       Partition  Segment
        server1  192.168.160.3:8301  alive   server  1.15.1  2         dc-test  default    <all>
        server2  192.168.160.5:8301  alive   server  1.15.1  2         dc-test  default    <all>
        server3  192.168.160.2:8301  alive   server  1.15.1  2         dc-test  default    <all>
        client1  192.168.160.4:8301  alive   client  1.15.1  2         dc-test  default    <default>

7. Open UI: `open http://localhost:8500/`


## Simulated VMs as local playground
Simulated VMs are nothing more than docker containers with python and sshd agent installed and running.
They may be started using the `docker-compose.yaml`, which will also bring up the Consul client.

## Requirements

- python3 (v3.8 or grater) using `venv` for virtual environments
- when using simulator, docker with docker compose is used
- knowledge of [Ansible](http://docs.ansible.com/)
