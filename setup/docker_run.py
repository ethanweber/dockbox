#!/usr/bin/env python
from __future__ import print_function
import os
import argparse
import socket
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--command", type=str, default="", help="(optional) thing to run in container")
    args = parser.parse_args()
    if args.command and args.command != "":
        command = "bash -c \"{}\"".format(args.command)
    else:
        command = ""
    cmd = """\
    docker run \
      --name dockbox \
      -v {source_dir}:/dockbox \
      -v {bazel_cache}:{bazel_cache} \
      -it \
      --rm \
      dockbox-dependencies \
      {command}
    """.format(source_dir=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."),
               command=command,
               bazel_cache=os.path.join(os.environ["HOME"], ".cache", "bazel"))
    print("command:", cmd)
    os.system(cmd)
