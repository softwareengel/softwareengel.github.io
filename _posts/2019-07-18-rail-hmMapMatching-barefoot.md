---
layout: post
title: Rail map matching - hmm hidden markow matching 
categories: [ai, hmm, hidden markow chain, map matchig, rail]
tags: [ai, hmm, hidden markow chain, map matchig, rail]
--- 
![Map and Tack calculated with barefoot](/pic/capture_005_18072019_150834.jpg)
Rail map matching: pqsql, barefoot, java, virtualbox, ubuntu, osmosis, qgis 

# Rail Map Matching - barefoot 

<https://github.com/bmwcarit/barefoot> 

## Install 


+ Oracle VM Virtual Box 
+ Ubuntu Linux Server: <http://releases.ubuntu.com/18.04/> ; <http://releases.ubuntu.com/18.04/ubuntu-18.04.2-live-server-amd64.iso> 

+ VM Settings:

![VM Settings](/pic/capture_001_18072019_144944.jpg)

### config 

#### rail-types.json:

    {
    "tags":
        [
        {
            "tag":"railway","id":1,"values":
            [
                {
                "name":"rail",
                "id":101,
                "priority":0.9,
                "maxspeed":130
                }
            ]
        }
        ]
    }



 
 #

### import-rail-arnsberg

    #!/bin/bash

    set -o errexit -o nounset

    if [ "$#" -eq "6" ] && ( [ "$6" = "slim" ] || [ "$6" = "normal" ] )
    then
        input=$1
        database=$2
        user=$3
        password=$4
        config=$5
        mode=$6
    elif [ "$#" -eq "0" ]
    then
        input=/mnt/map/osm/railmap-latest-arnsberg.osm
        database=arnsberg
        user=osmuser
        password=pass
        config=/mnt/map/tools/rail-types.json
        mode=slim
    else
        echo "Error. Say '$0 osm-file database user password bfmap-config slim|normal' or run with defaults '$0'."
        exit
    fi

and update osmosis command, if using .osm-Files 

    osmosis --read-xml file=${input} --tf accept-ways railway=* --write-pgsql user="${user}" password="${password}" database="${database}"


## Run 

    sudo docker ps -a 
    sudo docker stop barefoot-oberbayern
    sudo docker start barefoot-oberbayern

![putty shell for docker](/pic/capture_002_18072019_145914.jpg)

### View PostgreSql Data in PgAdmin:

![PgAdim III](/pic/capture_004_18072019_150336.jpg)

Data Table with ways:
![PgAdim III](/pic/capture_003_18072019_150333.jpg)

### View in Qgis 2.18

View Points and Relations from PGSql Data and Track 
![Map and Tack calculated with barefoot](/pic/capture_005_18072019_150834.jpg)

### Eclipse: 

+ C:\java\eclipse-jee-2019-03-R-win32-x86_64\eclipse

+ Maven build install - skiptests 


### config file oberbayern-rail.properties
    database.host=192.168.3.68
    database.port=5432
    database.name=oberbayern
    database.table=bfmap_ways
    database.user=osmuser
    database.password=pass
    database.road-types=./map/tools/rail-types.json

### input file 
x0001-002-arnsberg.json 

    [{"point": "POINT(7.411564 51.545052)","time":"2014-09-10 06:54:07+0200","id":"\\x0001"},
    {"point": "POINT(7.420255 51.535264)", "time":"2014-09-10 06:56:07+0200","id":"\\x0001"},
    {"point": "POINT(7.426305 51.528816)", "time":"2014-09-10 06:58:07+0200","id":"\\x0001"},
    {"point": "POINT(7.447957 51.516552)", "time":"2014-09-10 07:00:07+0200","id":"\\x0001"}
    ]

x0001-002-arnsberg.geojson

    {"coordinates": [[7.411564,51.545052],[7.420255,51.535264],[7.426305, 51.528816],[7.447957,51.516552]],"type": "LineString"}





### start server 

    C:\java\jdk1.8u181\bin\javaw.exe -Dfile.encoding=UTF-8 -classpath "C:\src\git\barefoot\target\classes;C:\Users\engels\.m2\repository\com\esri\geometry\esri-geometry-api\1.1\esri-geometry-api-1.1.jar;C:\Users\engels\.m2\repository\org\codehaus\jackson\jackson-core-asl\1.9.12\jackson-core-asl-1.9.12.jar;C:\Users\engels\.m2\repository\org\json\json\20090211\json-20090211.jar;C:\Users\engels\.m2\repository\org\postgresql\postgresql\9.2-1003-jdbc4\postgresql-9.2-1003-jdbc4.jar;C:\Users\engels\.m2\repository\net\sf\geographiclib\GeographicLib-Java\1.46\GeographicLib-Java-1.46.jar;C:\Users\engels\.m2\repository\org\slf4j\slf4j-api\1.7.10\slf4j-api-1.7.10.jar;C:\Users\engels\.m2\repository\ch\qos\logback\logback-classic\1.0.9\logback-classic-1.0.9.jar;C:\Users\engels\.m2\repository\ch\qos\logback\logback-core\1.0.9\logback-core-1.0.9.jar;C:\Users\engels\.m2\repository\org\zeromq\jeromq\0.3.5\jeromq-0.3.5.jar" com.bmwcarit.barefoot.matcher.ServerControl --geojson config/server.properties config/arnsberg.properties


    2019-07-18 16:04:29,719 INFO  [main] ServerControl: initialize server
    2019-07-18 16:04:29,721 INFO  [main] ServerControl: read database properties from file config/arnsberg.properties
    2019-07-18 16:04:29,723 INFO  [main] Loader: load map from file C:\src\git\barefoot\arnsberg.bfmap
    2019-07-18 16:04:29,788 INFO  [main] RoadMap: inserting roads ...
    2019-07-18 16:04:30,133 INFO  [main] RoadMap: inserted 14111 (28222) roads and finished
    2019-07-18 16:04:30,163 INFO  [main] RoadMap: ~5 megabytes used for road data (estimate)
    2019-07-18 16:04:30,196 INFO  [main] RoadMap: index and topology constructing ...
    2019-07-18 16:04:30,389 INFO  [main] RoadMap: index and topology constructed
    2019-07-18 16:04:30,421 INFO  [main] RoadMap: ~3 megabytes used for spatial index (estimate)
    2019-07-18 16:04:30,421 INFO  [main] ServerControl: read tracker properties from file config/server.properties
    2019-07-18 16:04:30,438 INFO  [main] MatcherServer: matcher.radius.max=200.0
    2019-07-18 16:04:30,438 INFO  [main] MatcherServer: matcher.distance.max=15000.0
    2019-07-18 16:04:30,438 INFO  [main] MatcherServer: matcher.lambda=0.0
    2019-07-18 16:04:30,438 INFO  [main] MatcherServer: matcher.sigma=10.0
    2019-07-18 16:04:30,438 INFO  [main] MatcherServer: matcher.threads=8
    2019-07-18 16:04:30,438 INFO  [main] MatcherServer: matcher.shortenturns=true
    2019-07-18 16:04:30,438 INFO  [main] MatcherServer: matcher.interval.min=1000
    2019-07-18 16:04:30,438 INFO  [main] MatcherServer: matcher.distance.min=0.0
    2019-07-18 16:04:30,438 INFO  [main] AbstractServer: server.port=1234
    2019-07-18 16:04:30,438 INFO  [main] AbstractServer: server.timeout.request=15000
    2019-07-18 16:04:30,438 INFO  [main] AbstractServer: server.timeout.response=60000
    2019-07-18 16:04:30,438 INFO  [main] AbstractServer: server.connections=20
    2019-07-18 16:04:30,438 INFO  [main] ServerControl: starting server on port 1234 with map arnsberg
    2019-07-18 16:04:30,441 INFO  [main] AbstractServer: listening on port 1234 ...


### python client call 
![call server by python client](/pic/capture_009_18072019_162520.jpg)

    C:/Python/Python27/python.exe c:/src/git/barefoot/util/submit/batch.py --host 127.0.0.1 --port 1234 --file C:\src\git\barefoot\src\test\resources\com\bmwcarit\barefoot\matcher\x0001-002-arnsberg.json 

#### Result 


### File out-track.geojson:


    {"coordinates":[[[7.412295835732849,51.54529733200804],[7.4124008,51.5451756],[7.4127597,51.5447682],[7.4131486,51.5443269],[7.4136452,51.543764],[7.4139897,51.5433763],[7.4143295,51.5430003],[7.4146292,51.5426685],[7.4149986,51.5422578],[7.4154803,51.5417218],[7.4158467,51.5413186],[7.4162044,51.5409199],[7.4165159,51.5405754],[7.4169859,51.5400528],[7.4170475,51.5399838],[7.4172386,51.5397756],[7.4173638,51.5396334],[7.4176969,51.539265],[7.4181662,51.5387516],[7.4184877,51.5383883],[7.4188244,51.5380172],[7.419317,51.5374722],[7.4195916,51.5371621],[7.4198479,51.5368737],[7.4201865,51.5364694],[7.4205274,51.5360338],[7.4206624,51.5358545],[7.4208326,51.5356172],[7.4209480206329035,51.53544932693059]],[[7.420948020632903,51.53544932693059],[7.4208326,51.5356172],[7.4206624,51.5358545],[7.4205274,51.5360338],[7.4201865,51.5364694],[7.4198479,51.5368737],[7.4195916,51.5371621],[7.419317,51.5374722],[7.4188244,51.5380172],[7.4184877,51.5383883],[7.4181662,51.5387516],[7.4176969,51.539265],[7.4173638,51.5396334],[7.4172386,51.5397756],[7.4170475,51.5399838],[7.4169859,51.5400528],[7.4165159,51.5405754],[7.4162044,51.5409199],[7.4158467,51.5413186],[7.4154803,51.5417218],[7.4149986,51.5422578],[7.4146292,51.5426685],[7.4143295,51.5430003],[7.4139897,51.5433763],[7.4136452,51.543764],[7.4131486,51.5443269],[7.4127597,51.5447682],[7.4124008,51.5451756],[7.4120928,51.5455328],[7.4122585,51.5453698],[7.4123719,51.5452612],[7.4125133,51.5451235],[7.412795,51.5448035],[7.4133154,51.5442173],[7.4137231,51.5437535],[7.4141261,51.5432986],[7.4145374,51.5428389],[7.4148042,51.5425437],[7.4150757,51.5422421],[7.4155347,51.541736],[7.4159077,51.5413247],[7.4161825,51.5410161],[7.4164957,51.5406692],[7.416781,51.5403557],[7.4170416,51.5400662],[7.4171065,51.5399935],[7.4172908,51.5397881],[7.4176342,51.5394069],[7.4179989,51.5390062],[7.4182679,51.5387059],[7.4186387,51.5382974],[7.4190916,51.5377936],[7.4194279,51.5374219],[7.4196882,51.5371316],[7.4199455,51.5368375],[7.4203262,51.5363774],[7.4206538,51.5359484],[7.4209309,51.53557],[7.4211731,51.535214],[7.4213842,51.5348754],[7.4216315,51.5344683],[7.4218351,51.5341075],[7.4219741,51.533842],[7.422157,51.5334638],[7.4223847,51.5329794],[7.4225445,51.5326399],[7.4226446,51.5324271],[7.4227609,51.5321799],[7.4228608,51.5319676],[7.4230906,51.5314697],[7.4232876,51.5310783],[7.4233915,51.5308927],[7.423553,51.5306272],[7.4237595,51.5303268],[7.4238457,51.5302128],[7.4242411,51.5297311],[7.4249401,51.5289507],[7.42534861292923,51.52848770314045]],[[7.42534861292923,51.52848770314045],[7.4254312,51.5283941],[7.4259577,51.5278023],[7.4261563,51.5275953],[7.4263194,51.527435],[7.4265384,51.5272294],[7.4267902,51.5270068],[7.4273055,51.5265945],[7.4277896,51.5262216],[7.4282653,51.5258498],[7.4286436,51.5255428],[7.4287624,51.5254399],[7.4288763,51.5253378],[7.4290423,51.5251903],[7.4292464,51.5249908],[7.4294292,51.5248008],[7.4296032,51.5246177],[7.4300141,51.5241625],[7.4306824,51.5234232],[7.431315,51.5227242],[7.4318355,51.522133],[7.4324029,51.521495],[7.4326328,51.5212387],[7.4327941,51.5210728],[7.4329669,51.5209055],[7.4332048,51.5206925],[7.4333192,51.5205954],[7.4334392,51.5205001],[7.4335705,51.5203949],[7.4336935,51.5203044],[7.4338566,51.5201867],[7.4340457,51.520056],[7.4343301,51.5198742],[7.434591,51.5197167],[7.4347827,51.5196088],[7.435041,51.5194716],[7.4353586,51.5193053],[7.4355702,51.5192005],[7.4356499,51.5191631],[7.4358105,51.5190875],[7.4360403,51.5189803],[7.4363929,51.5188267],[7.4365811,51.5187484],[7.4371738,51.5185165],[7.4376581,51.5183455],[7.4380383,51.5182226],[7.4388122,51.5179877],[7.4396781,51.5177353],[7.4401118,51.5176091],[7.4405285,51.5174874],[7.4410115,51.5173548],[7.4414193,51.5172515],[7.4417125,51.5171823],[7.4419624,51.5171246],[7.4422724,51.5170614],[7.4425693,51.517003],[7.4428433,51.5169534],[7.4431176,51.5169052],[7.4434301,51.5168569],[7.4437864,51.5168063],[7.4440677,51.5167703],[7.444453,51.5167277],[7.4448055,51.516693],[7.4450153,51.516675],[7.4452077,51.5166592],[7.4453737,51.5166483],[7.4455085,51.5166398],[7.4460496,51.5166134],[7.4463133,51.5166041],[7.4466712,51.5165968],[7.4471607,51.5165876],[7.4476912,51.5165839],[7.44795747747437,51.516582265027914]]],"type":"MultiLineString"}

### View output Track as geojson:
![json Tack calculated with barefoot](/pic/capture_006_18072019_151124.jpg)


## Reference

<https://github.com/bmwcarit/barefoot> 

![git barefoot](/pic/Screenshot_2019-07-18_bmwcarit_barefoot.png)


### History 

engels@barefoot:~$ history

    1  ifconfig
    2  cd barefoot/
    3  sudo docker build -t barefoot-map ./map
    4  sudo docker run -it -p 5432:5432 --name="barefoot-oberbayern" -v ${PWD}/map/:/mnt/map barefoot-map
    5  exit
    6  sudo apt-get update
    7  git clone https://github.com/bmwcarit/barefoot.git
    8  curl http://download.geofabrik.de/europe/germany/bayern/oberbayern-latest.osm.pbf -o barefoot/map/osm/oberbayern.osm.pbf
    9  sudo apt-get install mc
    10  sudo mc
    11  df
    12  exit
    13  sudo doccker ps -a
    14  sudo docker ps -a
    15  sudo docker start barefoot
    16  sudo docker start barefoot-map
    17  sudo docker start barefoot-oberbayern
    18  sudo docker ps -a
    19  sudo docker attach barefoot-oberbayern
    20  exit
    21  ifconfig
    22  sudo docker ps -a
    23  sudo docker start barefoot-oberbayern
    24 *
    25  sudo docker stop barefoot-oberbayernsudo docker stop barefoot-oberbayern
    26  sudo docker ps -a
    27  sudo docker start barefoot-oberbayern
    28  sudo docker ps -a
    29  history

### history in container 

root@0c005fe230a5:/# history


    1  sudo mc
    2  sudo apt-get install mc
    3  sudo mc
    4  /etc/init.d/postgresql restart
    5  exit
    6  p
#### Import Data in PGsql 

    7  bash /mnt/map/osm/import-rail.sh
    8  bash /mnt/map/osm/import-rail-arnsberg.sh
    9  exit

### SFtp Data transfer 

![git barefoot](/pic/capture_007_18072019_152058.jpg)
