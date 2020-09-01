#!/usr/bin/env python

"""CentOS required chcon -R -t ssh_home_t ~/keys/"""

import subprocess

with open("password.lst") as f:
    for line in f.readlines():
        line = line.rstrip()
        if line.startswith('#'):
            continue
        if len(line) < 5:
            continue
        p = subprocess.Popen('ssh-keygen -N "%s" -f key-"%s"' % (line, line), shell=True)
        p.wait()
