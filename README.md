# dockbox

# Building Locally

    sudo ./setup/install_titan_prereqs.sh
    - follow the same steps as in docker

# Building In Docker

Make sure that you can run `docker` without `sudo`. To set that up, just do:

    sudo usermod -aG docker $USER

and then log out and back in. You should only ever have to do this once. 

### First, build the docker image

    cd setup
    ./docker_build.py

    if on mac because there are slight differences
    ./docker_mac_build.py

### Get inside the docker shell

    ./docker_run.py

# Checklist for updating Drake

    - [ ] Edit the clone_drake.sh script with the correct repo and tag

# Steps to get drake working
    - cd /dockbox
    - ./clone_drake.sh
    - cd drake
    - sudo .setup/ubuntu/16.04/install_prereqs.sh
    - bazel build examples/valkyrie/box_atlas
    Once built
    - ./bazel-bin/examples/valkyrie/box_atlas

# Steps to connect LCM from Docker with Ubuntu
    - Docker must be configured properly to use with LCM input and output to interface outside of the container
    - Run ifconfig to find the network associated with the docker container, usually “docker0”
    - See https://lcm-proj.github.io/multicast_setup.html for more info
    - Run export LCM_DEFAULT_URL=udpm://239.255.76.67:7667?ttl=1 both inside Docker container (if passing data out) and outside Docker (if passing data in)
    Run after Docker container has started
    - sudo ifconfig “docker0” multicast
    - sudo route add -net 224.0.0.0 netmask 240.0.0.0 dev “docker0”
