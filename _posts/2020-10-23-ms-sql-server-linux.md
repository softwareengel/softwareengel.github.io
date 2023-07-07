---
layout: post
title: MS SQL Server Linux 
categories: [MS, SQL, SQL Server, Linux]
tags:  [MS, SQL, SQL Server, Linux]
---
MS SQl Server on Linux - only x86 (!) 
- [MS SQL Server Linux](#ms-sql-server-linux)
- [2020-10-21](#2020-10-21)
  - [Ubuntu Version Ubuntu 16.04 (xenial)](#ubuntu-version-ubuntu-1604-xenial)
  - [resize partition](#resize-partition)
- [Version MSMS MS SQl Server Management Studio](#version-msms-ms-sql-server-management-studio)

# MS SQL Server Linux 

    install ms sql server 
    install mc


# 2020-10-21 

see: https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-ssis?view=sql-server-ver15
```bash
sudo add-apt-repository "$(curl https://packages.microsoft.com/config/ubuntu/16.04/mssql-server-2019.list)"

sudo apt-get update
sudo apt-get install -y mssql-server-is
sudo /opt/ssis/bin/ssis-conf setup

sudo /opt/mssql/bin/mssql-conf set sqlagent.enabled true 
sudo curl -o /etc/apt/sources.list.d/mssql-server.list https://packages.microsoft.com/config/ubuntu/16.04/mssql-server-2017.list
sudo /opt/mssql/bin/mssql-conf setup 


systemctl status mssql-server
systemctl status mssql-server --no-pager
systemctl restart  mssql-server
```
<https://www.mssqltips.com/sql-server-tip-category/226/sql-server-on-linux/>


## Ubuntu Version Ubuntu 16.04 (xenial)

``` bash
curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

sudo apt-add-repository https://packages.microsoft.com/ubuntu/16.04/prod

sudo apt-get update

Ubuntu 18,04 (Bionic)

curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

sudo apt-add-repository https://packages.microsoft.com/ubuntu/18.04/prod

sudo apt-get update

Ubuntu 20,04 (Fokus)

curl -sSL https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -

sudo apt-add-repository https://packages.microsoft.com/ubuntu/20.04/prod

sudo apt-get update
```

## resize partition 
```
sudo fdisk /dev/sda2

Created a new DOS disklabel with disk identifier 0x49744b09.

Command (m for help): p
Disk /dev/sda2: 10 GiB, 10734272512 bytes, 20965376 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x49744b09
```
__

    sudo fdisk /dev/sda2

-- 

# Version MSMS MS SQl Server Management Studio 


    SQL Server Management Studio						15.0.18338.0
    SQL Server Management Objects (SMO)						16.100.41011.9
    Microsoft Analysis Services Client Tools						15.0.19205.0
    Microsoft Data Access Components (MDAC)						10.0.19041.1
    Microsoft MSXML						3.0 6.0 
    Microsoft .NET Framework						4.0.30319.42000
    Operating System						10.0.19041

