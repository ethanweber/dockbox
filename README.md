# dockbox - a tool for "box atlas" in drake

# Code Explanation - Box

- box_atlas
This code is usable and simple. In the /drake/examples/valkyrie/box_atlas.h file, there are some user-modified variables. By editing the names of bodies that correspond to the correct alias groups file (in this case `atlas.alias_groups`), you can specify the string names by editing one of the private variable names. The program will use this specified data to publish the x,y,z position and velocities over the robot_state_t LCM type. It's called box_atlas because we only care about a few points on the robot. The center of mass (specified as the x,y,z values in the pose translation component) and the specified bodies.

- box
This file is not very clean, but it contains all the necessary code to create QP inputs and control any robot with a valid URDF file. The box.cc and box.h files are used with the box binary (`bazel run --config gurobi box`). This works to specify some controls, but I didn't finish this development for what was needed. It could easily be picked up for later use with the current drake controller.

# Building Locally

    sudo ./setup/install_dockbox_prereqs.sh
    - and follow the same steps as in docker

# Building In Docker

Make sure that you can run `docker` without `sudo`. To set that up, just do:

    sudo usermod -aG docker $USER

and then log out and back in. You should only ever have to do this once.

### First, build the docker image

    // if using linux
    cd setup
    ./docker_build.py

    // if using mac because there are slight differences
    ./docker_mac_build.py

### Enter the docker container shell

    ./docker_run.py

# Checklist for updating the repo

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
