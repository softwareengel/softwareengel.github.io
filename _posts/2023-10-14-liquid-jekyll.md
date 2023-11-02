
# Liquid

## Jekyll

install in wsl

``` bash
C:\Windows\System32>wsl --install -d Ubuntu-22.04
Ubuntu 22.04 LTS ist bereits installiert.
Ubuntu 22.04 LTSwird gestartet...
```
---
```
Installing, this may take a few minutes...
Please create a default UNIX user account. The username does not need to match your Windows username.
For more information visit: https://aka.ms/wslusers
Enter new UNIX username: engels
New password:
Retype new password:
passwd: password updated successfully
Installation successful!
Windows-Subsystem für Linux ist jetzt im Microsoft Store verfügbar!
Sie können ein Upgrade durchführen, indem Sie "wsl.exe --update" ausführen oder https://aka.ms/wslstorepage
Durch die Installation von WSL aus dem Microsoft Store erhalten Sie schneller die neuesten WSL-Updates.
Weitere Informationen finden Sie unter https://aka.ms/wslstoreinfo

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

Welcome to Ubuntu 22.04.2 LTS (GNU/Linux 5.10.102.1-microsoft-standard-WSL2 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

This message is shown once a day. To disable it please create the
/home/engels/.hushlogin file.
```
---
``` bash
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt install ruby-full
sudo apt-get install make gcc gpp build-essential zlib1g zlib1g-dev ruby-dev dh-autoreconf
sudo gem update
sudo gem install bundler
sudo gem install jekyll
sudo gem install jekyll-admin

```

---
neues Projekt 

``` bash
jekyll new myblog
cd myblog/

```

in GEmfile einfügen 
```
gem 'jekyll-admin', group: :jekyll_plugins
```
---

```
bundle install
```
noch **_config.yml** anpassen

und dann 

``` bash
bundle exec jekyll serve
```

## V2

```bash
sudo apt-get update -y && sudo apt-get upgrade -y
```

https://kreativ-anders.de/blog/jekyll-fur-wsl/

## Liquid template engine

<https://github.com/Shopify/liquid>

<https://shopify.github.io/liquid/>

<https://github.com/Shopify/liquid/wiki>

