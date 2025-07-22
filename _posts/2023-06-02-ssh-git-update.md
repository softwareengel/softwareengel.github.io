---
layout: post
title: Update Openssh Git Public Key for VScode on Windows 
categories: [HowTos, ssh, git]
tags: [ssh, git, openssh]
---

![](../pics/2023-06-02-ssh-git-update_image_1.png)

# Update Git Pub Key for VScode on Windows 

Problem git pull im terminal 

``` bat
L:\>git pull  
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.      

Please make sure you have the correct access rights
and the repository exists.
```

Check 
```
L:\>git remote -v
origin  git@github.com:softwareengel/softwareengel.github.io.git (fetch)
origin  git@github.com:softwareengel/softwareengel.github.io.git (push) 
```

```
L:\>ssh git@github.com -v
OpenSSH_for_Windows_8.1p1, LibreSSL 3.0.2
debug1: Reading configuration data C:\\Users\\engels/.ssh/config
debug1: Connecting to github.com [140.82.121.3] port 22.        
debug1: Connection established.
debug1: identity file C:\\Users\\engels/.ssh/id_rsa type -1
debug1: identity file C:\\Users\\engels/.ssh/id_rsa-cert type -1    
debug1: identity file C:\\Users\\engels/.ssh/id_dsa type -1
debug1: identity file C:\\Users\\engels/.ssh/id_dsa-cert type -1    
debug1: identity file C:\\Users\\engels/.ssh/id_ecdsa type -1       
debug1: identity file C:\\Users\\engels/.ssh/id_ecdsa-cert type -1  
debug1: identity file C:\\Users\\engels/.ssh/id_ed25519 type -1     
debug1: identity file C:\\Users\\engels/.ssh/id_ed25519-cert type -1
debug1: identity file C:\\Users\\engels/.ssh/id_xmss type -1        
debug1: identity file C:\\Users\\engels/.ssh/id_xmss-cert type -1   
debug1: Local version string SSH-2.0-OpenSSH_for_Windows_8.1
debug1: Remote protocol version 2.0, remote software version babeld-57a54e01
debug1: no match: babeld-57a54e01
debug1: Authenticating to github.com:22 as 'git'
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256
debug1: kex: host key algorithm: ssh-ed25519
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ssh-ed25519 SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU
debug1: Host 'github.com' is known and matches the ED25519 host key.
debug1: Found key in C:\\Users\\engels/.ssh/known_hosts:7
debug1: rekey out after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey in after 134217728 blocks
debug1: pubkey_prepare: ssh_get_authentication_socket: No such file or directory
debug1: Will attempt key: C:\\Users\\engels/.ssh/id_rsa
debug1: Will attempt key: C:\\Users\\engels/.ssh/id_dsa
debug1: Will attempt key: C:\\Users\\engels/.ssh/id_ecdsa
debug1: Will attempt key: C:\\Users\\engels/.ssh/id_ed25519
debug1: Will attempt key: C:\\Users\\engels/.ssh/id_xmss
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519-cert-v01@openssh.com,ecdsa-sha2-nistp521-cert-v01@openssh.com,ecdsa-sha2-nistp384-cert-v01@openssh.com,ecdsa-sha2-nistp256-cert-v01@openssh.com,sk-ssh-ed25519-cert-v01@openssh.com,sk-ecdsa-sha2-nistp256-cert-v01@openssh.com,rsa-sha2-512-cert-v01@openssh.com,rsa-sha2-256-cert-v01@openssh.com,ssh-rsa-cert-v01@openssh.com,sk-ssh-ed25519@openssh.com,sk-ecdsa-sha2-nistp256@openssh.com,ssh-ed25519,ecdsa-sha2-nistp521,ecdsa-sha2-nistp384,ecdsa-sha2-nistp256,rsa-sha2-512,rsa-sha2-256,ssh-rsa>
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey
debug1: Next authentication method: publickey
debug1: Trying private key: C:\\Users\\engels/.ssh/id_rsa
debug1: Authentications that can continue: publickey
debug1: Trying private key: C:\\Users\\engels/.ssh/id_dsa
debug1: Trying private key: C:\\Users\\engels/.ssh/id_ecdsa
debug1: Trying private key: C:\\Users\\engels/.ssh/id_ed25519
debug1: Trying private key: C:\\Users\\engels/.ssh/id_xmss
debug1: No more authentication methods to try.
git@github.com: Permission denied (publickey).
```



Originaler Openssh Private key in id_rsa in User - Ordner   

    C:\Users\xxxxUSERxxx\.ssh

![](../pics/2023-06-02-ssh-git-update_image_2.png)

Mit ssh-keygen public Key aus private Key erstellen 

```
(.venv) (base) PS C:\Users\engels\.ssh> ssh-keygen.exe -y -f .\id_rsa
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCwwDAa8DdJO+ddXmvqkpI4VUMEmjSqsbn+aINOYhFUamd4UAwRIS3AA/0Ns28HJbsgLinmDXLkyxpws2oyrynAVB3vYX050GYQttH2jUbSakjKkmPdLpaIZi79f1LGRSy2VEdDplcPkxZjXgW3SAEBDxc/8Btaqvq6QyfEkmucmNNbBUK79f1LGRSy2VEdDplcPkxZjXgW3SAEBDxc/8Btaqvq6QyfEkmucmNNbBUKAVcsjDn/rV4N03UwwrnKInfltkHUzqGeC13L4Ev9iIj6Ij0OJEmic8U64KWQFgRFOG75+nxOL33EgrJWykRcLrFuHUoBQbK7EaEHBHyZbTZNHrxuKpoQKPzB8hnhkUC8/u6xafC+vs2rOOjBjL1fSvgma1rERd4EGfrSRiSVWPPngEPZquBhVGrljZk9GJWjYZEzc8+hiG+blSl4M8mFcB7HyZbTZNHrxuKpoQKPzB8hnhkUC8/u6xafC+vs2rOOjBjL1fSvgma1rERdnCEjy5mDcCb1F8J9o3aYfCJIM2M1Ind/q0qW4dNcKtsVZEzZuZ/glzg5VBLr4lInNP83aHY71dtuW52U1pY8PKJwQCkmqAufRkX+VQOZFROqtXjnb0GEcws7TtKlsvmm/0IlABiQjubc3JRAH1r5pJKR04P+QmqlUkismbwhEGQ5t3OmzRAizFzeTzxSVCpFcTvP8GCM+nPSfG+rUKe6EOHZEzZuZ/glzg5VBLr4lInNP83aHY71dtuW52U1pY8PKJwQCkmqAufRkX+VolA0Qa36x57FMOJDYv3bSSVILbhHo2KfishS4rWqVRW7MBWclL3hpFETPQj0ya0qeImZqO7rIwFuw== engels@T470p
```

Datei id_rsa.pub erstellen (nicht nötig)

![](../pics/2023-06-02-ssh-git-update_image_3.png)

Pub Key bei Github eintragen 

![](../pics/2023-06-02-ssh-git-update_image_4.png)


![](../pics/2023-06-02-ssh-git-update_image_5.png)

Testen 
```
L:\>git pull
Already up to date.
syn```
Erfolg: Neuer Pub-Key wurde benutzt 

![](../pics/2023-06-02-ssh-git-update_image_6.png)
