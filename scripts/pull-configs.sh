#!/bin/bash
cd /
scp -r cumulus@172.16.83.254:~/local-git-repo/test/configs/$HOSTNAME/* .
ifreload -a
systemctl enable frr
systemctl start frr

