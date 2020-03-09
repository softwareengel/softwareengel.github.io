# InfluxDB 

InfluxDB is the open source time series database
https://portal.influxdata.com/downloads/ 

https://hub.docker.com/_/influxdb 


# Telegraf 

Telegraf is the open source server agent to help you collect metrics from your stacks, sensors and systems.

https://www.influxdata.com/time-series-platform/telegraf/ 

![Screenshot 2020 01 17 Influx Db Telefraf](pic/Screenshot-2020-01-17_influx-db-telefraf.png)




# Grafana

https://github.com/torkelo/grafana

docker run -d -p 3000:3000 --name=grafana -e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource" -e "GF_SECURITY_ADMIN_PASSWORD=secret" grafana/grafana



## Grafana on Raspi 

https://github.com/fg2it/grafana-on-raspberry/

https://bintray.com/fg2it/deb/grafana-on-raspberry/v5.1.4

![Screenshot 2020 01 17 Rpi Graphana Select Data Sources](pic/Screenshot-2020-01-17_Rpi_graphana-select-data-sources.png),

![Screenshot 2020 01 17 Rpi Grafana Dashboard](pic/Screenshot-2020-01-17_Rpi_grafana-dashboard.png)

![Screenshot 2020 01 17 Rpi Grafana Explore](pic/Screenshot-2020-01-17_Rpi_grafana-explore.png)


# Grafana + Telegraf + Influx 

https://www.bjoerns-techblog.de/2017/05/installation-von-influxdb-telegraf-und-grafana-auf-dem-raspberry-pi-3/#data-image-svg-xml-3Csvg-20xmlns-http-www-w3-org-2000-svg-20viewBox-0-200-20400-20197-3E-3C-svg-3E-933317 

https://canox.net/2018/01/installation-von-grafana-influxdb-telegraf-auf-einem-raspberry-pi/

http://padcom13.blogspot.com/2015/12/influxdb-telegraf-and-grafana-on.html

Webinterface geht nur bis Version 1.5 (?!) 

![Screenshot 2020 01 21 Rpi Influx D B Webinterface](pic/Screenshot-2020-01-21_Rpi-influxDB-webinterface.png)

## Chonograf 

https://portal.influxdata.com/downloads/ 

![Screenshot 2020 01 21 Rpi Chohograph Influx D B Hostlist](pic/Screenshot-2020-01-21_Rpi_chohograph-influxDB-hostlist.png)

![Screenshot 2020 01 21 Rpi Chohograph Influx D B](pic/Screenshot-2020-01-21_Rpi_chohograph-influxDB.png)

![Screenshot 2020 01 21 Rpi Chohograph Influx D B Data Graph](pic/Screenshot-2020-01-21_Rpi_chohograph-influxDB-data-graph.png)

![Screenshot 2020 01 21 Rpi Chronograf Influx D B Admin](pic/Screenshot-2020-01-21_Rpi-chronograf-influxDB-admin.png)


## Python loggin Skript für influxDB

https://engineer.john-whittington.co.uk/2016/11/raspberry-pi-data-logger-influxdb-grafana/ 

Feeigaben Dev-Netz 

![Screenshot 2020 01 21 Rpi Dev Netz](pic/Screenshot-2020-01-21_Rpi-DevNetz.png)


# memcached 

Sessionspeicher 

# redis

in memory db / Key - Val- Store 

# Mongo DB 

Dokument speicher auch für csv / JSON 

# Maria DB 

OSS Fork von MySQL 

