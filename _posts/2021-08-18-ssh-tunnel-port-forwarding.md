---
layout: post
title: ssh-tunnel-port-forwarding
categories: [ssh-tunnel, port-forwarding]
tags: [ssh, tunnel, port, forwarding]
--- 

# ssh-tunnel-port-forwarding

Enable port forwarding with ssh tunnel

## Setup

    |DBServer:1443|<-|sshTunelPC|-|FW|-|FW|->|443:sshd:2222|<-|DBClient|

- Keygen

``` bash
ssh-keygen ... File dog2
```

- SshdServer

    set password

``` bash
passwd
```

- Edit ssh - config

        nano /etc/ssh/sshd_config

    and add/update

        GatewayPorts yes

    Edit
        .ssh/authorized_keys

    and add (from dog2.pub)

``` bash
        echo  "ssh-rsa AAAAB3NzaC1yc2EAAAABJ ... 6PQ== rsa-key-20170517" > authorized_keys
```

    and edit, no login possible:

        command="/bin/false" ssh-rsa AAAAB3NzaC1yc2EAAAADAQAB...

    Restart sshd

        sudo systemctl restart sshd

- sshTunelPC

        ssh-add dog2
        ssh pi@192.168.2.43 -i dog2 -R 0.0.0.0:5555:192.168.2.230:80 -o gatewayports=yes -N
        ssh pi@hq.softwareengel.de -i dog2 -R 0.0.0.0:5555:DBServer:1443 -o gatewayports=yes -N

- Check IP+Port (0.0.0.0:5555(!))

        netstat -ltn

        pi@raspberrypi:~ $ netstat -ltn
        Active Internet connections (only servers)
        Proto Recv-Q Send-Q Local Address           Foreign Address         State      
        tcp        0      0 0.0.0.0:5555            0.0.0.0:*               LISTEN     
        tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN     
        tcp        0      0 0.0.0.0:3000            0.0.0.0:*               LISTEN     
        tcp        0      0 0.0.0.0:19999           0.0.0.0:*               LISTEN     
        tcp        0      0 127.0.0.1:34303         0.0.0.0:*               LISTEN     
        tcp6       0      0 :::5555                 :::*                    LISTEN     
        tcp6       0      0 :::22                   :::*                    LISTEN     

## add ssh key to remote

ssh-copy-id
