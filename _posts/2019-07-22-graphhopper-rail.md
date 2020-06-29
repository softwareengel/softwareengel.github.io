---
layout: post
title: Graphhopper Rail, Street + Truck
categories: [routing]
tags: [Graphhopper, routing, api, web]
--- 
# Graphhopper Rail, Street + Truck 

<https://github.com/geofabrik/OpenRailRouting> 

## Start MapMatch 
    set log4j.configurationFile = log4j2.yaml
    java  -Dgraphhopper.datareader.file=ulm.osm -jar target/railway_routing-0.0.1-SNAPSHOT-jar-with-dependencies.jar import config.yml
    java  -Dgraphhopper.datareader.file=ulm.osm -jar target/railway_routing-0.0.1-SNAPSHOT-jar-with-dependencies.jar match -V alltracks --gpx-location=gpx/gh_track_6TP.gpx  config.yml 


## gh_track_6TP.gpx
    <?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" creator="Graphhopper version 0.11" version="1.1" xmlns:gh="https://graphhopper.com/public/schema/gpx/1.1">
    <metadata><copyright author="OpenStreetMap contributors"/><link href="http://graphhopper.com"><text>GraphHopper GPX</text></link><time>2019-07-12T14:20:11Z</time></metadata>
    <trk><name>GraphHopper Track</name><trkseg>
    <trkpt lat="48.197411" lon="10.102224"><time>2019-07-12T14:20:11Z</time></trkpt>
    <trkpt lat="48.294044" lon="10.076729"><time>2019-07-12T14:46:30Z</time></trkpt>
    <trkpt lat="48.396915" lon="10.021243"><time>2019-07-12T15:15:50Z</time></trkpt>
    <trkpt lat="48.397152" lon="10.020657"><time>2019-07-12T15:15:57Z</time></trkpt>
    <trkpt lat="48.39737" lon="10.019981"><time>2019-07-12T15:16:05Z</time></trkpt>
    <trkpt lat="48.405633" lon="9.831699"><time>2019-07-12T15:55:38Z</time></trkpt>
    </trkseg>
    </trk>
    </gpx>

## start web 
    set log4j.configurationFile = log4j2.yaml


    java  -Dgraphhopper.datareader.file=ulm.osm -jar target/railway_routing-0.0.1-SNAPSHOT-jar-with-dependencies.jar import config.yml

    java  -Dgraphhopper.datareader.file=ulm.osm -jar target/railway_routing-0.0.1-SNAPSHOT-jar-with-dependencies.jar serve config.yml 

Web - View Graphhopper rail:
Routing Ulm:
![](/pic/capture_22072019_113652_002.jpg))

![](/pic/capture_22072019_113038_001.jpg)
Routing Arnsberg:
![](/pic/capture_22072019_120913_003.jpg)
Routing Europa:
![](/pic/capture_22072019_171154_001.jpg)

Requerst für Map:

    http://127.0.0.1:8989/maps/?point=43.576411%2C1.417236&point=45.721522%2C4.833984&point=46.927759%2C7.294922&point=44.43378%2C11.359863&point=42.037054%2C12.579346&point=43.691708%2C10.371094&point=47.085085%2C15.402832&point=45.809658%2C15.957642&point=48.224673%2C16.391602&point=50.092393%2C14.436035&point=52.106505%2C20.588379&point=47.82422%2C18.995361&point=52.469397%2C13.359375&point=53.842805%2C10.6073&point=54.487591%2C9.817657&point=55.252512%2C9.457855&point=55.496749%2C9.461975&point=55.652798%2C12.337646&point=59.277108%2C17.097473&point=52.352119%2C9.761353&point=51.165567%2C6.394043&point=48.814099%2C2.329102&point=44.750634%2C-0.527344&point=41.51886%2C-1.465302&point=41.599013%2C0.598755&point=40.128491%2C-3.779297&locale=de&vehicle=alltracks&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale

Requerst für OSM-Map auf hq.softwareengel.de:

    http://hq.softwareengel.de:8989/maps/?point=50.945882%2C7.013526&point=51.091448%2C7.013397&point=51.167719%2C7.012711&point=51.273944%2C7.229004&locale=de&vehicle=alltracks&weighting=fastest&elevation=false&use_miles=false&layer=OpenStreetMap

    http://hq.softwareengel.de:8989/maps/?point=51.344339%2C6.833496&point=48.893615%2C2.416992&point=45.821143%2C4.866943&point=41.516804%2C2.213745&point=43.249204%2C-1.977539&point=40.722283%2C-3.180542&point=39.070379%2C-8.87146&point=38.401949%2C-0.681152&point=41.668809%2C-0.845947&point=43.560491%2C1.411743&point=44.809122%2C-0.593262&point=47.184113%2C-1.419983&point=44.658885%2C10.851402&point=44.067854%2C12.480469&point=41.934977%2C12.507935&point=46.494611%2C11.299438&point=47.085085%2C15.424805&point=48.188063%2C11.590576&point=50.071244%2C14.436035&point=53.514185%2C10.041504&point=55.66984%2C12.474976&point=59.279047%2C18.006592&point=59.377988%2C13.535156&point=59.927496%2C10.799561&point=57.715885%2C11.942139&point=50.348966%2C19.651794&point=54.597528%2C25.3125&point=55.544173%2C34.909058&point=53.388243%2C34.035645&point=52.462704%2C31.014404&point=52.295042%2C21.005859&locale=de&vehicle=alltracks&weighting=fastest&elevation=false&use_miles=false&layer=OpenStreetMap

    http://hq.softwareengel.de:8989/maps/?point=47.137425%2C15.336914&point=46.721035%2C14.364624&point=51.351201%2C4.454956&point=51.158677%2C3.251953&point=50.937662%2C1.757813&point=51.549751%2C-0.159302&point=52.516221%2C-1.801758&point=55.890716%2C-4.042969&point=48.908059%2C2.438965&point=48.118434%2C-1.532593&point=45.79817%2C4.855957&point=44.962855%2C-0.22522&point=43.258706%2C-1.978912&point=41.75902%2C-0.823975&point=39.532644%2C-0.32341&point=37.920368%2C-4.721375&point=37.492294%2C-5.932617&point=38.603993%2C-9.091187&point=41.120228%2C-8.638&point=43.329174%2C-8.44162&point=36.259778%2C-5.438232&point=40.423951%2C-3.435974&point=43.794146%2C7.380409&point=41.95132%2C12.414551&point=41.07521%2C14.205322&point=44.072787%2C15.379486&point=42.660222%2C21.084137&point=42.644898%2C23.549194&point=43.620171%2C24.675293&point=41.136262%2C28.601532&point=39.970806%2C32.541504&point=38.634036%2C35.194702&point=40.526327%2C43.005981&point=41.607228%2C44.868164&point=43.197167%2C44.615479&point=38.444985%2C38.259888&point=38.552461%2C27.03186&point=38.117272%2C23.806&point=45.371443%2C27.938232&point=47.338823%2C31.096802&point=48.904449%2C33.299561&point=47.82422%2C34.887085&point=49.435985%2C34.557495&point=51.542919%2C39.243164&point=55.606281%2C37.63504&point=59.161852%2C40.0177&point=51.648703%2C36.00769&point=50.454007%2C30.695801&point=54.669066%2C25.3125&point=52.140231%2C20.98938&point=50.014799%2C19.940186&point=51.14834%2C17.097473&point=48.283193%2C16.430054&point=45.863238%2C22.983398&point=47.480088%2C19.25354&point=44.087585%2C12.420044&point=45.479392%2C12.233276&point=45.69467%2C13.85376&point=44.427896%2C8.889313&point=52.038977%2C4.537354&point=52.328625%2C5.015259&point=50.986099%2C7.025757&point=51.495065%2C7.341614&point=52.24462%2C7.981567&point=53.041213%2C8.909912&point=51.55829%2C9.920654&point=51.349485%2C9.516907&point=50.155786%2C8.640747&point=49.477048%2C10.980835&point=48.037692%2C11.585083&point=47.802087%2C13.068237&point=48.806863%2C9.217529&point=47.393701%2C8.491058&point=52.449314%2C9.733887&point=53.555606%2C9.935074&point=54.13026%2C12.21405&point=54.77693%2C9.50592&point=55.665193%2C12.461243&point=55.583002%2C12.996826&point=56.14708%2C13.757629&point=59.850333%2C10.789948&point=60.401645%2C5.419006&point=59.293942%2C18.019638&point=62.408185%2C17.232056&point=59.380786%2C25.054321&point=60.524861%2C25.153198&point=56.98989%2C24.180908&point=52.059246%2C11.68396&point=51.013755%2C13.801575&point=51.426614%2C12.367859&point=52.566334%2C13.084717&locale=de&vehicle=alltracks&weighting=fastest&elevation=false&use_miles=false&layer=OpenStreetMap

## Web Soap UI Client mit POST und XML 

![](/pic/capture_22072019_165705_001.jpg)

### Request GH Rail Match XML (good request)

    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "POST /match?vehicle=alltracks HTTP/1.1[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "Accept-Encoding: gzip,deflate[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "Content-Type: application/xml[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "Content-Length: 988[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "Host: 127.0.0.1:8989[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "Connection: Keep-Alive[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "User-Agent: Apache-HttpClient/4.1.1 (java 1.5)[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" creator="Graphhopper version 0.11" version="1.1" xmlns:gh="https://graphhopper.com/public/schema/gpx/1.1">[\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "<metadata><copyright author="OpenStreetMap contributors"/><link href="http://graphhopper.com"><text>GraphHopper GPX</text></link><time>2019-07-12T14:20:11Z</time></metadata>[\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "<trk><name>GraphHopper Track</name><trkseg>[\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "<trkpt lat="48.197411" lon="10.102224"><time>2019-07-12T14:20:11Z</time></trkpt>[\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "<trkpt lat="48.294044" lon="10.076729"><time>2019-07-12T14:46:30Z</time></trkpt>[\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "<trkpt lat="48.396915" lon="10.021243"><time>2019-07-12T15:15:50Z</time></trkpt>[\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "<trkpt lat="48.397152" lon="10.020657"><time>2019-07-12T15:15:57Z</time></trkpt>[\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "<trkpt lat="48.39737" lon="10.019981"><time>2019-07-12T15:16:05Z</time></trkpt>[\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "<trkpt lat="48.405633" lon="9.831699"><time>2019-07-12T15:55:38Z</time></trkpt>[\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "</trkseg>[\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "</trk>[\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:>> "</gpx>"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:<< "HTTP/1.1 200 OK[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:<< "Date: Tue, 23 Jul 2019 07:46:51 GMT[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:<< "X-GH-Took: 13[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:<< "Content-Type: application/json[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:<< "Content-Length: 2789[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:<< "[\r][\n]"
    Tue Jul 23 09:46:51 CEST 2019:DEBUG:<< "{"hints":{},"info":{"copyrights":["GraphHopper","OpenStreetMap contributors"],"took":13},"paths":[{"distance":40117.718,"weight":9.223372036854775E12,"time":1442072,"transfers":0,"points_encoded":true,"bbox":[9.831646,48.197411,10.102219,48.419353],"points":"ypdeHyat|@gVx@e\\xAa}BfJqQ|@aGj@_C\\sCh@_Ez@yP~EuH|BoSrF{IjCyUnGa]xJo|@hPwh@tJoRfD_VpEwb@nHeh@|J}Bl@aDdAoHtCeF|BgGnDyNvKkT|QaBpAq|BnmB_ZbVaBtA}AnAuN|LcAdA_MlK}GvFcCfB}CpBuIzEmGpCeLhDoE`Ayc@pIeNdCgCj@iCf@sKlBsJ~A}S|DyKzBe`AzQ}|Bxb@eb@~HsA^}Ah@_Bp@qBtAgBfBiBzBeBvCyBzEaApCm@`Ca@bCi@jEMhBKxBEhFDtDH`CNvBR`BZvBj@lCt@nCz@|B|@pBp@lAdBhCtG|JlDpGvCvFnBbFpA|CnAhDpApEjAjFRzA\\tDL`EAnBE`CM~BS~B[dCq@tDOh@aAtCyE|KuI|T}@rB]n@cA`Be@n@_AzAW\\cCvCm@t@i@h@oDdCaBx@a@JgBZg@F_Qd@gIOiAFuAb@k@^gAhA_@h@i@`Ac@pAc@`Bc@bC]tCa@bFG`B?nAFxCfBrWVbDZdCd@hCvDnQXnAnAhEr@nCVfATpAfAnIJrAPpFFpHSpGsAtRg@vFm@fFoB|Nq@vDyPrhAwBxL}@rE}@zD{CdLoCtIwBbGyDnJuP`_@uS~c@oBxEy@hCeAzDa@lB{@`GUfCMzBIxBCtBA~BFxDHdBPdCb@nEp@dFxC|RbB`Mn@hGV`EFpDE`FG`B_@lFsJ`dAW~DMtECfFF`ETvE\\zDj@`Ex@|D~@nDdA|ChAjC~@hBjAlBvCxDtIxIdEnE~D|DnCxC~@jAx@nAhAvBdAzBl@|AdBzGn@xDRvAVdCLhBFvAJxFErCIhCKtBStBoAfK_Gzb@SlCQfDEjDB`CNtDRjCf@lDfAhFjA`D|@nB`CxDpA|AxCbDpL|M","instructions":[{"distance":22091.329,"heading":356.49,"sign":0,"interval":[0,52],"text":"Continue onto Illertalbahn, 5400","time":722976,"street_name":"Illertalbahn, 5400"},{"distance":2211.763,"sign":-7,"interval":[52,79],"text":"Keep left onto 5400","time":80529,"street_name":"5400"},{"distance":2136.62,"sign":0,"interval":[79,103],"text":"Continue onto 4700","time":90223,"street_name":"4700"},{"distance":27.644,"sign":0,"interval":[103,104],"text":"Continue onto 4500","time":1105,"street_name":"4500"},{"distance":49.084,"sign":-7,"interval":[104,105],"text":"Keep left","time":3212,"street_name":""},{"distance":17.639,"sign":0,"interval":[105,106],"text":"Continue onto 4500","time":705,"street_name":"4500"},{"distance":92.066,"sign":-7,"interval":[106,107],"text":"Keep left onto 4541","time":3682,"street_name":"4541"},{"distance":2279.316,"sign":-7,"interval":[107,137],"text":"Keep left onto 4541","time":91165,"street_name":"4541"},{"distance":1282.242,"sign":7,"interval":[137,150],"text":"Keep right onto 4541","time":51283,"street_name":"4541"},{"distance":7494.544,"sign":0,"interval":[150,207],"text":"Continue onto 4540","time":299775,"street_name":"4540"},{"distance":2435.471,"sign":7,"interval":[207,234],"text":"Keep right onto 4540","time":97417,"street_name":"4540"},{"distance":0.0,"sign":4,"last_heading":216.21135357056747,"interval":[234,234],"text":"Arrive at destination","time":0,"street_name":""}],"legs":[],"details":{},"ascend":0.0,"descend":0.0,"snapped_waypoints":""}],"map_matching":{"original_distance":37097.25613455281,"distance":40117.718365362096,"time":1442072,"original_time":5727000}}"

### Response 

    {
    "hints": {},
    "info":    {
        "copyrights":       [
            "GraphHopper",
            "OpenStreetMap contributors"
        ],
        "took": 13
    },
    "paths": [   {
        "distance": 40117.718,
        "weight": 9.223372036854775E12,
        "time": 1442072,
        "transfers": 0,
        "points_encoded": true,
        "bbox":       [
            9.831646,
            48.197411,
            10.102219,
            48.419353
        ],
        "points": "ypdeHyat|@gVx@e\\xAa}BfJqQ|@aGj@_C\\sCh@_Ez@yP~EuH|BoSrF{IjCyUnGa]xJo|@hPwh@tJoRfD_VpEwb@nHeh@|J}Bl@aDdAoHtCeF|BgGnDyNvKkT|QaBpAq|BnmB_ZbVaBtA}AnAuN|LcAdA_MlK}GvFcCfB}CpBuIzEmGpCeLhDoE`Ayc@pIeNdCgCj@iCf@sKlBsJ~A}S|DyKzBe`AzQ}|Bxb@eb@~HsA^}Ah@_Bp@qBtAgBfBiBzBeBvCyBzEaApCm@`Ca@bCi@jEMhBKxBEhFDtDH`CNvBR`BZvBj@lCt@nCz@|B|@pBp@lAdBhCtG|JlDpGvCvFnBbFpA|CnAhDpApEjAjFRzA\\tDL`EAnBE`CM~BS~B[dCq@tDOh@aAtCyE|KuI|T}@rB]n@cA`Be@n@_AzAW\\cCvCm@t@i@h@oDdCaBx@a@JgBZg@F_Qd@gIOiAFuAb@k@^gAhA_@h@i@`Ac@pAc@`Bc@bC]tCa@bFG`B?nAFxCfBrWVbDZdCd@hCvDnQXnAnAhEr@nCVfATpAfAnIJrAPpFFpHSpGsAtRg@vFm@fFoB|Nq@vDyPrhAwBxL}@rE}@zD{CdLoCtIwBbGyDnJuP`_@uS~c@oBxEy@hCeAzDa@lB{@`GUfCMzBIxBCtBA~BFxDHdBPdCb@nEp@dFxC|RbB`Mn@hGV`EFpDE`FG`B_@lFsJ`dAW~DMtECfFF`ETvE\\zDj@`Ex@|D~@nDdA|ChAjC~@hBjAlBvCxDtIxIdEnE~D|DnCxC~@jAx@nAhAvBdAzBl@|AdBzGn@xDRvAVdCLhBFvAJxFErCIhCKtBStBoAfK_Gzb@SlCQfDEjDB`CNtDRjCf@lDfAhFjA`D|@nB`CxDpA|AxCbDpL|M",
        "instructions":       [
                    {
                "distance": 22091.329,
                "heading": 356.49,
                "sign": 0,
                "interval":             [
                0,
                52
                ],
                "text": "Continue onto Illertalbahn, 5400",
                "time": 722976,
                "street_name": "Illertalbahn, 5400"
            },
                    {
                "distance": 2211.763,
                "sign": -7,
                "interval":             [
                52,
                79
                ],
                "text": "Keep left onto 5400",
                "time": 80529,
                "street_name": "5400"
            },
                    {
                "distance": 2136.62,
                "sign": 0,
                "interval":             [
                79,
                103
                ],
                "text": "Continue onto 4700",
                "time": 90223,
                "street_name": "4700"
            },
                    {
                "distance": 27.644,
                "sign": 0,
                "interval":             [
                103,
                104
                ],
                "text": "Continue onto 4500",
                "time": 1105,
                "street_name": "4500"
            },
                    {
                "distance": 49.084,
                "sign": -7,
                "interval":             [
                104,
                105
                ],
                "text": "Keep left",
                "time": 3212,
                "street_name": ""
            },
                    {
                "distance": 17.639,
                "sign": 0,
                "interval":             [
                105,
                106
                ],
                "text": "Continue onto 4500",
                "time": 705,
                "street_name": "4500"
            },
                    {
                "distance": 92.066,
                "sign": -7,
                "interval":             [
                106,
                107
                ],
                "text": "Keep left onto 4541",
                "time": 3682,
                "street_name": "4541"
            },
                    {
                "distance": 2279.316,
                "sign": -7,
                "interval":             [
                107,
                137
                ],
                "text": "Keep left onto 4541",
                "time": 91165,
                "street_name": "4541"
            },
                    {
                "distance": 1282.242,
                "sign": 7,
                "interval":             [
                137,
                150
                ],
                "text": "Keep right onto 4541",
                "time": 51283,
                "street_name": "4541"
            },
                    {
                "distance": 7494.544,
                "sign": 0,
                "interval":             [
                150,
                207
                ],
                "text": "Continue onto 4540",
                "time": 299775,
                "street_name": "4540"
            },
                    {
                "distance": 2435.471,
                "sign": 7,
                "interval":             [
                207,
                234
                ],
                "text": "Keep right onto 4540",
                "time": 97417,
                "street_name": "4540"
            },
                    {
                "distance": 0,
                "sign": 4,
                "last_heading": 216.21135357056747,
                "interval":             [
                234,
                234
                ],
                "text": "Arrive at destination",
                "time": 0,
                "street_name": ""
            }
        ],
        "legs": [],
        "details": {},
        "ascend": 0,
        "descend": 0,
        "snapped_waypoints": ""
    }],
    "map_matching":    {
        "original_distance": 37097.25613455281,
        "distance": 40117.718365362096,
        "time": 1442072,
        "original_time": 5727000
    }
    }
### Request GH Rail Match XML (bad request)
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "POST /match?vehicle=alltracks HTTP/1.1[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "Accept-Encoding: gzip,deflate[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "Content-Type: application/xml[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "Content-Length: 981[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "Host: 127.0.0.1:8989[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "Connection: Keep-Alive[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "User-Agent: Apache-HttpClient/4.1.1 (java 1.5)[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "<?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" creator="Graphhopper version 0.11" version="1.1" xmlns:gh="https://graphhopper.com/public/schema/gpx/1.1">[\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "<metadata><copyright author="OpenStreetMap contributors"/><link href="http://graphhopper.com"><text>GraphHopper GPX</text></link><time>2019-07-12T14:20:11Z</time></metadata>[\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "<trk><name>GraphHopper Track</name><trkseg>[\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "<trkpt lat="51.372406" lon="7.38792"><time>2019-07-12T14:20:11Z</time></trkpt>[\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "<trkpt lat="51.382957" lon="7.41997"><time>2019-07-12T14:46:30Z</time></trkpt>[\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "<trkpt lat="51.384111" lon="7.422672"><time>2019-07-12T15:15:50Z</time></trkpt>[\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "<trkpt lat="51.386874" lon="7.43009"><time>2019-07-12T15:15:57Z</time></trkpt>[\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "<trkpt lat="48.39737" lon="10.019981"><time>2019-07-12T15:16:05Z</time></trkpt>[\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "<trkpt lat="51.389138" lon="7.438345"><time>2019-07-12T15:55:38Z</time></trkpt>[\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "</trkseg>[\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "</trk>[\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:>> "</gpx>"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:<< "HTTP/1.1 400 Bad Request[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:<< "Date: Tue, 23 Jul 2019 07:45:37 GMT[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:<< "Content-Type: application/json[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:<< "Content-Length: 1756[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:<< "[\r][\n]"
    Tue Jul 23 09:45:37 CEST 2019:DEBUG:<< "{"message":"Sequence is broken for submitted track at time step 4 (6 points). Too long distance to previous measurement? 380686m, observation:48.39737,10.019981,0.0, 1562944565000, 8 candidates: [distance: 0.9967661049530568 to 48.3973616821115,10.019975966693504,NaN, distance: 0.9967661049530568 to 48.3973616821115,10.019975966693504,NaN, distance: 12.031350983351464 to 48.397475914198694,10.02001432359822,NaN, distance: 12.031350983351464 to 48.397475914198694,10.02001432359822,NaN, distance: 30.783105486733163 to 48.39744229012971,10.020383485117186,NaN, distance: 2.9987786030179095 to 48.397390694857926,10.020007044524112,NaN, distance: 2.844571066455726 to 48.39739381359322,10.019995075795576,NaN, distance: 2.844571066455726 to 48.39739381359322,10.019995075795576,NaN]. If a match is expected consider increasing max_visited_nodes.","hints":[{"message":"Sequence is broken for submitted track at time step 4 (6 points). Too long distance to previous measurement? 380686m, observation:48.39737,10.019981,0.0, 1562944565000, 8 candidates: [distance: 0.9967661049530568 to 48.3973616821115,10.019975966693504,NaN, distance: 0.9967661049530568 to 48.3973616821115,10.019975966693504,NaN, distance: 12.031350983351464 to 48.397475914198694,10.02001432359822,NaN, distance: 12.031350983351464 to 48.397475914198694,10.02001432359822,NaN, distance: 30.783105486733163 to 48.39744229012971,10.020383485117186,NaN, distance: 2.9987786030179095 to 48.397390694857926,10.020007044524112,NaN, distance: 2.844571066455726 to 48.39739381359322,10.019995075795576,NaN, distance: 2.844571066455726 to 48.39739381359322,10.019995075795576,NaN]. If a match is expected consider increasing max_visited_nodes.","details":"java.lang.IllegalArgumentException"}]}"

### Response GH Rail Match JSON
    {
    "hints": {},
    "info":    {
        "copyrights":       [
            "GraphHopper",
            "OpenStreetMap contributors"
        ],
        "took": 33
    },
    "paths": [   {
        "distance": 40117.718,
        "weight": 9.223372036854775E12,
        "time": 1442072,
        "transfers": 0,
        "points_encoded": true,
        "bbox":       [
            9.831646,
            48.197411,
            10.102219,
            48.419353
        ],
        "points": "ypdeHyat|@gVx@e\\xAa}BfJqQ|@aGj@_C\\sCh@_Ez@yP~EuH|BoSrF{IjCyUnGa]xJo|@hPwh@tJoRfD_VpEwb@nHeh@|J}Bl@aDdAoHtCeF|BgGnDyNvKkT|QaBpAq|BnmB_ZbVaBtA}AnAuN|LcAdA_MlK}GvFcCfB}CpBuIzEmGpCeLhDoE`Ayc@pIeNdCgCj@iCf@sKlBsJ~A}S|DyKzBe`AzQ}|Bxb@eb@~HsA^}Ah@_Bp@qBtAgBfBiBzBeBvCyBzEaApCm@`Ca@bCi@jEMhBKxBEhFDtDH`CNvBR`BZvBj@lCt@nCz@|B|@pBp@lAdBhCtG|JlDpGvCvFnBbFpA|CnAhDpApEjAjFRzA\\tDL`EAnBE`CM~BS~B[dCq@tDOh@aAtCyE|KuI|T}@rB]n@cA`Be@n@_AzAW\\cCvCm@t@i@h@oDdCaBx@a@JgBZg@F_Qd@gIOiAFuAb@k@^gAhA_@h@i@`Ac@pAc@`Bc@bC]tCa@bFG`B?nAFxCfBrWVbDZdCd@hCvDnQXnAnAhEr@nCVfATpAfAnIJrAPpFFpHSpGsAtRg@vFm@fFoB|Nq@vDyPrhAwBxL}@rE}@zD{CdLoCtIwBbGyDnJuP`_@uS~c@oBxEy@hCeAzDa@lB{@`GUfCMzBIxBCtBA~BFxDHdBPdCb@nEp@dFxC|RbB`Mn@hGV`EFpDE`FG`B_@lFsJ`dAW~DMtECfFF`ETvE\\zDj@`Ex@|D~@nDdA|ChAjC~@hBjAlBvCxDtIxIdEnE~D|DnCxC~@jAx@nAhAvBdAzBl@|AdBzGn@xDRvAVdCLhBFvAJxFErCIhCKtBStBoAfK_Gzb@SlCQfDEjDB`CNtDRjCf@lDfAhFjA`D|@nB`CxDpA|AxCbDpL|M",
        "instructions":       [
                    {
                "distance": 22091.329,
                "heading": 356.49,
                "sign": 0,
                "interval":             [
                0,
                52
                ],
                "text": "Continue onto Illertalbahn, 5400",
                "time": 722976,
                "street_name": "Illertalbahn, 5400"
            },
                    {
                "distance": 2211.763,
                "sign": -7,
                "interval":             [
                52,
                79
                ],
                "text": "Keep left onto 5400",
                "time": 80529,
                "street_name": "5400"
            },
                    {
                "distance": 2136.62,
                "sign": 0,
                "interval":             [
                79,
                103
                ],
                "text": "Continue onto 4700",
                "time": 90223,
                "street_name": "4700"
            },
                    {
                "distance": 27.644,
                "sign": 0,
                "interval":             [
                103,
                104
                ],
                "text": "Continue onto 4500",
                "time": 1105,
                "street_name": "4500"
            },
                    {
                "distance": 49.084,
                "sign": -7,
                "interval":             [
                104,
                105
                ],
                "text": "Keep left",
                "time": 3212,
                "street_name": ""
            },
                    {
                "distance": 17.639,
                "sign": 0,
                "interval":             [
                105,
                106
                ],
                "text": "Continue onto 4500",
                "time": 705,
                "street_name": "4500"
            },
                    {
                "distance": 92.066,
                "sign": -7,
                "interval":             [
                106,
                107
                ],
                "text": "Keep left onto 4541",
                "time": 3682,
                "street_name": "4541"
            },
                    {
                "distance": 2279.316,
                "sign": -7,
                "interval":             [
                107,
                137
                ],
                "text": "Keep left onto 4541",
                "time": 91165,
                "street_name": "4541"
            },
                    {
                "distance": 1282.242,
                "sign": 7,
                "interval":             [
                137,
                150
                ],
                "text": "Keep right onto 4541",
                "time": 51283,
                "street_name": "4541"
            },
                    {
                "distance": 7494.544,
                "sign": 0,
                "interval":             [
                150,
                207
                ],
                "text": "Continue onto 4540",
                "time": 299775,
                "street_name": "4540"
            },
                    {
                "distance": 2435.471,
                "sign": 7,
                "interval":             [
                207,
                234
                ],
                "text": "Keep right onto 4540",
                "time": 97417,
                "street_name": "4540"
            },
                    {
                "distance": 0,
                "sign": 4,
                "last_heading": 216.21135357056747,
                "interval":             [
                234,
                234
                ],
                "text": "Arrive at destination",
                "time": 0,
                "street_name": ""
            }
        ],
        "legs": [],
        "details": {},
        "ascend": 0,
        "descend": 0,
        "snapped_waypoints": ""
    }],
    "map_matching":    {
        "original_distance": 37097.25613455281,
        "distance": 40117.718365362096,
        "time": 1442072,
        "original_time": 5727000
    }
    }

## Graphhopper Routig Detail-Ansicht-Video 

[./mov/2019-07-22_12-15-32.flv.webm](./mov/2019-07-22_12-15-32.flv.webm)

## Speicher Sysinternals bei Map mit Europa 

![](/pic/capture_22072019_171453_002.jpg)



# Berechnung Ergebnis des GH Rail Map Matchings
![](/pic/capture_22072019_131603_004.jpg)

## Ulm GPX-Track 
    <?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" creator="Graphhopper version 0.11" version="1.1" xmlns:gh="https://graphhopper.com/public/schema/gpx/1.1">
    <metadata><copyright author="OpenStreetMap contributors"/><link href="http://graphhopper.com"><text>GraphHopper GPX</text></link><time>2019-07-12T14:20:11Z</time></metadata>
    <trk><name>GraphHopper Track</name><trkseg>
    <trkpt lat="48.197411" lon="10.102224"><time>2019-07-12T14:20:11Z</time></trkpt>
    <trkpt lat="48.294044" lon="10.076729"><time>2019-07-12T14:46:30Z</time></trkpt>
    <trkpt lat="48.396915" lon="10.021243"><time>2019-07-12T15:15:50Z</time></trkpt>
    <trkpt lat="48.397152" lon="10.020657"><time>2019-07-12T15:15:57Z</time></trkpt>
    <trkpt lat="48.39737" lon="10.019981"><time>2019-07-12T15:16:05Z</time></trkpt>
    <trkpt lat="48.405633" lon="9.831699"><time>2019-07-12T15:55:38Z</time></trkpt>
    </trkseg>
    </trk>
    </gpx>

## HagenTrack.gpx
    <?xml version="1.0" encoding="UTF-8" standalone="no" ?><gpx xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" creator="Graphhopper version 0.11" version="1.1" xmlns:gh="https://graphhopper.com/public/schema/gpx/1.1">
    <metadata><copyright author="OpenStreetMap contributors"/><link href="http://graphhopper.com"><text>GraphHopper GPX</text></link><time>2019-07-12T14:20:11Z</time></metadata>
    <trk><name>GraphHopper Track</name><trkseg>
    <trkpt lat="51.372406" lon="7.38792"><time>2019-07-12T14:20:11Z</time></trkpt>
    <trkpt lat="51.382957" lon="7.41997"><time>2019-07-12T14:46:30Z</time></trkpt>
    <trkpt lat="51.384111" lon="7.422672"><time>2019-07-12T15:15:50Z</time></trkpt>
    <trkpt lat="51.386874" lon="7.43009"><time>2019-07-12T15:15:57Z</time></trkpt>
    <trkpt lat="48.39737" lon="10.019981"><time>2019-07-12T15:16:05Z</time></trkpt>
    <trkpt lat="51.389138" lon="7.438345"><time>2019-07-12T15:55:38Z</time></trkpt>
    </trkseg>
    </trk>
    </gpx>
# Ergebnis GPX in Qgis 

![](/pic/capture_22072019_131852_005.jpg)


## Beispiel config.yml

Beispiel config für Rail 

    # encoder properties
    flagEncoderProperties:
    - name: tgv_all
        electrified: contact_line
        voltages: 15000;25000;1500;3000
        frequencies: 16.7;16.67;50;0
        gauges: 1435
        maxspeed: 319
        speedFactor: 11
    - name: non_tgv
        gauges: 1435
        maxspeed: 120
        speedFactor: 5
    - name: alltracks
        maxspeed: 120
        speedFactor: 5
    - name: allelectric
        maxspeed: 140
        speedFactor: 5
        electrified: contact_line,yes

    graphhopper:
    # OpenStreetMap input file
    # datareader.file: some.pbf

    ##### Vehicles #####


    # Possible options: car,foot,bike,bike2,mtb,racingbike,motorcycle (comma separated)
    # bike2 takes elevation data into account (like up-hill is slower than down-hill) and requires enabling graph.elevation.provider below
    # This property must not be set for railway routing. Use graphhopper.profiles instead
    # graph.flag_encoders: car

    profiles: alltracks,allelectric

    # Enable turn restrictions for car or motorcycle.
    # graph.flag_encoders: car|turn_costs=true


    ##### Elevation #####


    # To populate your graph with elevation data use SRTM, default is noop (no elevation)
    # graph.elevation.provider: srtm


    # default location for cache is /tmp/srtm
    # graph.elevation.cache_dir: ./srtmprovider/


    # If you have a slow disk or plenty of RAM change the default MMAP to:
    # graph.elevation.dataaccess: RAM_STORE



    #### Speed, hybrid and flexible mode ####


    # By default the speed mode with the 'fastest' weighting is used. Internally a graph preparation via
    # contraction hierarchies (CH) is done to speed routing up. This requires more RAM/disc space for holding the
    # graph but less for every request. You can also setup multiple weightings, by providing a comma separated list.
    # prepare.ch.weightings: fastest


    # Disable the speed mode. Should be used only with routing.max_visited_nodes or when the hybrid mode is enabled instead
    prepare.ch.weightings: no


    # To make CH preparation faster for multiple flagEncoders you can increase the default threads if you have enough RAM.
    # Change this setting only if you know what you are doing and if the default worked for you.
    # prepare.ch.threads: 1


    # The hybrid mode can be enabled with
    # prepare.lm.weightings: fastest

    # To tune the performance vs. memory usage for the hybrid mode use
    # prepare.lm.landmarks: 16

    # Make landmark preparation parallel if you have enough RAM. Change this only if you know what you are doing and if the default worked for you.
    # prepare.lm.threads: 1


    # avoid being stuck in a (oneway) subnetwork, see https://discuss.graphhopper.com/t/93
    #prepare.min_network_size: 200
    #prepare.min_one_way_network_size: 200



    ##### Routing #####


    # You can define the maximum visited nodes when routing. This may result in not found connections if there is no
    # connection between two points within the given visited nodes. The default is Integer.MAX_VALUE. Useful for flexibility mode
    # routing.max_visited_nodes: 1000000


    # If enabled, allows a user to run flexibility requests even if speed mode is enabled. Every request then has to include a hint routing.ch.disable=true.
    # Attention, non-CH route calculations take way more time and resources, compared to CH routing.
    # A possible attacker might exploit this to slow down your service. Only enable it if you need it and with routing.maxVisitedNodes
    # routing.ch.disabling_allowed: true


    # If enabled, allows a user to run flexible mode requests even if the hybrid mode is enabled. Every such request then has to include a hint routing.lm.disable=true.
    # routing.lm.disabling_allowed: true

    # Control how many active landmarks are picked per default, this can improve query performance
    # routing.lm.active_landmarks: 4


    # You can limit the max distance between two consecutive waypoints of flexible routing requests to be less or equal
    # the given distance in meter. Default is set to 1000km.
    routing.non_ch.max_waypoint_distance: 1000000



    ##### Web #####


    # if you want to support jsonp response type you need to add it explicitly here. By default it is disabled for stronger security.
    # web.jsonp_allowed: true



    ##### Storage #####


    # configure the memory access, use RAM_STORE for well equipped servers (default and recommended)
    #graph.dataaccess: RAM_STORE


    # will write way names in the preferred language (language code as defined in ISO 639-1 or ISO 639-2):
    # datareader.preferred_language: en


    # Sort the graph after import to make requests roughly ~10% faster. Note that this requires significantly more RAM on import.
    # graph.do_sort: true



    ##### Spatial Rules #####
    # Spatial Rules require some configuration and only work with the DataFlagEncoder.


    # Spatial Rules require you to provide Polygons in which the rules are enforced
    # The line below contains the default location for these rules
    # spatial_rules.location: core/files/spatialrules/countries.geo.json

    # You can define the maximum BBox for which spatial rules are loaded.
    # You might want to do this if you are only importing a small area and don't need rules for other countries.
    # Having less rules, might result in a smaller graph. The line below contains the world-wide bounding box, uncomment and adapt to your need.
    # spatial_rules.max_bbox: -180,180,-90,90


    # Uncomment the following to point /maps to the source directory in the filesystem instead of
    # the Java resource path. Helpful for development of the web client.
    # Assumes that the web module is the working directory.
    #
    assets:
    overrides:
    /maps: src/main/resources/assets/
    /map-matching: src/main/resources/map-matching-frontend/

    # Dropwizard server configuration
    server:
    applicationConnectors:
    - type: http
        port: 8989
        # for security reasons bind to localhost
        bindHost: localhost
    requestLog:
        appenders: []
    adminConnectors:
    - type: http
        port: 8990
        bindHost: localhost
        

# Log4j2.yaml
    Configuration:
    status: warn
    name: YAMLConfigTest
    properties:
        property:
        name: filename
        value: target/test-yaml.log
    thresholdFilter:
        level: debug
    appenders:
        Console:
        name: STDOUT
        PatternLayout:
            Pattern: "%m%n"
        File:
        name: File
        fileName: ${filename}
        PatternLayout:
            Pattern: "%d %p %C{1.} [%t] %m%n"
        Filters:
            ThresholdFilter:
            level: error
    
    Loggers:
        logger:
        -
            name: org.apache.logging.log4j.test1
            level: debug
            additivity: false
            ThreadContextMapFilter:
            KeyValuePair:
                key: test
                value: 123
            AppenderRef:
            ref: STDOUT
        -
            name: StatusLogger
            level: debug
            additivity: false
            AppenderRef:
            ref: File
        Root:
        level: error
        AppenderRef:
            ref: STDOUT


# Shell Notizen Rail 

    java -Xmx2500m -Xms50m -Dgraphhopper.datareader.file=railmap-latest-arnsberg.osm -Dgraphhopper.profiles=freight_diesel -jar .\target\railway_routing-0.0.1-SNAPSHOT-jar-with-dependencies.jar import

    java -Xmx2500m -Xms50m -Dgraphhopper.prepare.ch.weightings=no -Dgraphhopper.datareader.file=railmap-latest-arnsberg.osm -Dgraphhopper.profiles=freight_diesel -jar .\target\railway_routing-0.0.1-SNAPSHOT-jar-with-dependencies.jar

    java  -Dgraphhopper.datareader.file=ulm.osm -jar target/railway_routing-0.0.1-SNAPSHOT-jar-with-dependencies.jar match -V alltracks --gpx-location=gpx/gh_track_6TP.gpx  config.yml 

# history babun 
        1  ls -al 
        2  cd /cygdrive/c/src/WasteRoute
        3  dir
        4  cd graphhopper
        5  ./graphhopper.sh -a web -i ../osm/nordrhein-westfalen-latest.osm.pbf
        6  export JAVA_OPTS="-Xmx1g -Xms1g"
        7  ./graphhopper.sh -a web -i ../osm/nordrhein-westfalen-latest.osm.pbf
        8  exit
        9  cd /cygdrive/c/src/WasteRoute
    10  dir
    11  ls -la
    12  cd graphhopper
    13  dir
    14  ls -la
    15  ./graphhopper.sh -a web -i ../osm/out.pbf
    16  ./graphhopper.sh 
    17  ./graphhopper.sh -p car -a web -i ../osm/out.pbf
    18  ./graphhopper.sh -a build
    19  ./graphhopper.sh -p car -a web -i ../osm/out.pbf -c config.yml
    20  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml
    21  ./graphhopper.sh -a web -i ../osm/out.pbf -c config-example.yml
    22  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml
    23  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car,foot
    24  ./graphhopper.sh 
    25  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    26  cd /cygdrive/c/src
    27  cd WasteRoute/graphhopper
    28  dir
    29  ls -al 
    30  5555ls Kein   398 May 15 12:43 .project
    31  drwxr-xr-x 1 engels Kein     0 May 15 12:45 .settings
    32  -rw-r--r-- 1 engels Kein  2657 May 15 12:42 .travis.yml
    33  drwxr-xr-x 1 engels Kein     0 May 15 12:42 android
    34  -rw-r--r-- 1 engels Kein  1027 May 15 12:42 appveyor.yml
    35  drwxr-xr-x 1 engels Kein     0 May 15 12:45 client-hc
    36  -rw-r--r-- 1 engels Kein  5617 May 15 20:01 config.yml
    37  -rw-r--r-- 1 engels Kein  5498 May 15 19:10 config-example.yml
    38  -rw-r--r-- 1 engels Kein  2952 May 15 12:42 CONTRIBUTORS.md
    39  drwxr-xr-x 1 engels Kein     0 May 15 12:45 core
    40  -rw-r--r-- 1 engels Kein   396 May 15 12:42 Dockerfile
    41  drwxr-xr-x 1 engels Kein     0 May 15 12:42 docs
    42  drwxr-xr-x 1 engels Kein     0 May 15 19:23 graph-cache
    43  -rwxr-xr-x 1 engels Kein 10733 May 15 12:42 graphhopper.sh
    44  drwxr-xr-x 1 engels Kein     0 May 15 12:45 isochrone
    45  -rw-r--r-- 1 engels Kein 11562 May 15 12:42 LICENSE.txt
    46  drwxr-xr-x 1 engels Kein     0 Apr  3  2017 maven
    47  -rw-r--r-- 1 engels Kein  2602 May 15 12:42 NOTICE.md
    48  -rw-r--r-- 1 engels Kein 14765 May 15 12:42 pom.xml
    49  drwxr-xr-x 1 engels Kein     0 May 15 12:45 reader-gtfs
    50  drwxr-xr-x 1 engels Kein     0 May 15 12:45 reader-json
    51  drwxr-xr-x 1 engels Kein     0 May 15 12:45 reader-osm
    52  drwxr-xr-x 1 engels Kein     0 May 15 12:45 reader-shp
    53  -rw-r--r-- 1 engels Kein 11504 May 15 12:42 README.md
    54  dir
    55  \n
    56  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    57  exit
    58  _ifconfig
    59  ?
    60  help
    61  exit
    62  cd /cygdrive/c/src/WasteRoute/graphhopper
    63  \n\n
    64  dir
    65  \n
    66  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    67  exit
    68  cd /cygdrive/c/src/WasteRoute/graphhopper
    69  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    70  cd /cygdrive/c/src/WasteRoute/elog-uml/WS/umlGeneratorEvaluator/out
    71  dir
    72  cat
    73  cat *
    74  cat * |grep 8989
    75  cat * |grep :8989
    76  cat * |grep :8989>ghUrls.txt
    77  exit
    78  cd /cygdrive/c/src/WasteRoute/graphhopper
    79  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    80  exit
    81  cd /cygdrive/c/src/WasteRoute/graphhopper
    82  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    83  exit
    84  cd /cygdrive/c/src/WasteRoute/graphhopper
    85  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    86  exit
    87  cd /cygdrive/c/src/WasteRoute/graphhopper
    88  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    89  exit
    90  cd /cygdrive/c/src/WasteRoute/graphhopper
    91  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    92  exit
    93  cd /cygdrive/c/src/WasteRoute/
    94  cxd railway_routing
    95  cd railway_routing
    96  ./build.sh
    97  cd ..
    98  cd railservice
    99  cd hopper
    100  cd railway_routing
    101  git submodule init
    102  bash
    103  pwd
    104  bash build.sh
    105  pact
    106  pact install mvn
    107  bash build.sh
    108  mvn
    109  pact install maven
    110  exit
    111  ls
    112  ps
    113  ps-al
    114  ps -al
    115  ps -alx
    116  ps -ap
    117  ps -h
    118  ps -f
    119  top
    120  ntopp
    121  ntop
    122  dir
    123  ?
    124  help
    125  sc
    126  ?
    127  help
    128  cd railway_routing
    129  fc
    130  cd railway_routing
    131  help
    132  fc
    133  help
    134  dir
    135  ls -al
    136  more .babunrc
    137  java
    138  java -v
    139  java -version
    140  exit
    141  ls
    142  ls -al
    143  ls -l &
    144  bg
    145  fg
    146  ps
    147  ps -W
    148  ps -W|more
    149  jobs
    150  jobs --help
    151  jobs -h
    152  jobs /?
    153  edit
    154  write
    155  ps -W
    156  ps -W|grep write
    157  ps -W
    158  fg 39304
    159  exit
    160  cd /cygdrive/c/src/WasteRoute/graphhopper
    161  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    162  exit
    163  cd /cygdrive/c/src/railservice
    164  cd hopper
    165  cd railway_routing
    166  ./build.sh
    167  exit
    168  cd /cygdrive/c/src/WasteRoute/graphhopper
    169  dir
    170  chmod +x babunStartHopper.sh
    171  dir
    172  .
    173  mc
    174  ./graphhopper.sh
    175  mc
    176  ./babunStartHopper.sh
    177  exit
    178  cd /cygdrive/c/src/WasteRoute/graphhopper
    179  dire
    180  dir
    181  ls -la
    182  ./babunStartHopper.sh
    183  /cygdrive/c/src/WasteRoute/graphhopper/babunStartHopper.sh
    184  cd /cygdrive/c/src/WasteRoute/graphhopper
    185  ./babunStartHopper.sh
    186  exit
    187  cd /cygdrive/c/src
    188  cd WasteRoute/graphhopper
    189  ./babunStartHopperNRW.sh
    190  exit
    191  cd /cygdrive/c/src/WasteRoute
    192  graphhopper/babunStartHopperNRW.sh
    193  cd graphhopper
    194  ./babunStartHopperNRW.sh
    195  exit
    196  cd /cygdrive/c/src/WasteRoute/graphhopper
    197  dir
    198  ./babunStartHopperNRW.sh
    199  exit
    200  pwd
    201  cd /cygdrive/c/src/WasteRoute/graphhopper
    202  ./babunStartHopperNRW.sh
    203  ./babunStartHopper.sh
    204  ./babunStartHopperNRW.sh
    205  exit
    206  gcc
    207  fcc -?
    208  gcc /?
    209  gcc -?
    210  gcc -help
    211  gcc --help
    212  gcc -v
    213  gcc --version
    214  exit
    215  python
    216  pwd
    217  dir
    218  ls -al 
    219  python hello.py
    220  whereis python
    221  python3
    222  python
    223  python3
    224  py
    225  py --help
    226  py hello.py
    227  whereis py
    228  py hello.py
    229  dir
    230  chmod +x hello.py
    231  dir
    232  ls - al
    233  ls -l
    234  ls -la
    235  ls -l
    236  ./hello.py
    237  whereis py
    238  whereis python
    239  ./hello.py
    240  cat hello.py
    241  ./hello.py
    242  py
    243  python
    244  python3
    245  py3
    246  py
    247  exit
    248  exiz
    249  exit
    250  fg 1
    251  fg
    252  ext
    253  exit
    254  ls
    255  dir
    256  cd bin
    257  dir
    258  cd ..
    259  cat hello.py
    260  py
    261  py -?
    262  rm hello.py
    263  pwd
    264  cd /cygdrive/c/src/WasteRoute
    265  cd graphhopper
    266  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    267  exit
    268  dir
    269  ls
    270  ls -al 
    271  cd bin
    272  ls -al 
    273  top
    274  lsof -i
    275  dir
    276  cd graphhopper
    277  cd /cygdrive/c/src/WasteRoute
    278  cd graphhopper
    279  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    280  exit
    281  dir
    282  ls -al 
    283  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    284  cd graphhopper
    285  cd /cygdrive/c/src/WasteRoute
    286  cd graphhopper
    287  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    288  exit
    289  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    290  cd graphhopper
    291  cd /cygdrive/c/src/WasteRoute
    292  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    293  cd graphhopper
    294  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    295  exit
    296  cd graphhopper
    297  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    298  pwd
    299  cd /cygdrive/c/src/WasteRoute
    300  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    301  cd graphhopper
    302  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    303  exit
    304  cd graphhopper
    305  cd /cygdrive/c/src/WasteRoute
    306  cd graphhopper
    307  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    308  exit
    309  ls
    310  ls -al 
    311  cd /cygdrive/c/src/WasteRoute
    312  ls -al 
    313  cd /cygdrive/c
    314  ls -al 
    315  babun --version
    316  cd ~
    317  /
    318  exit
    319  babun --version
    320  cd /cygdrive/c/src/WasteRoute
    321  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    322  cd graphhopper
    323  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    324  exit
    325  cd /cygdrive/c/src/WasteRoute
    326  cd graphhopper
    327  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    328  exit
    329  cd /cygdrive/c/src/WasteRoute
    330  cd graphhopper
    331  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    332  exit
    333  cd /cygdrive/c/src/WasteRoute
    334  cd graphhopper
    335  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    336  ./graphhopper.sh -a web -i ../osm/nordrhein-westfalen-latest.osm.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    337  ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar
    338  xit
    339  exit
    340  pwd
    341  exit
    342  cd /cygdrive/c/src/git/barefoot/map/tools/
    343  cd..
    344  cd ..
    345  bash map/osm/import.sh
    346  exit
    347  cd /cygdrive/c/src/git/barefoot/map/tools/
    348  /cygdrive/c/src/git/OpenRailRouting
    349  dir
    350  bash build.sh
    351  ./build.sh
    352  exit
    353  history


# Log import-rail-europe.sh
    root@4fb439410119:/# bash /mnt/map/osm/import-rail-europe.sh
    Start creation and initialization of database 'europe' ...
    CREATE EXTENSION
    CREATE EXTENSION
    Done.
    Start creation of user and initialization of credentials ...
    CREATE ROLE
    GRANT
    Done.
    Start population of OSM data (osmosis) ...
    psql:/mnt/map/osm/pgsnapshot_schema_0.6.sql:4: NOTICE:  table "actions" does not exist, skipping
    DROP TABLE
    psql:/mnt/map/osm/pgsnapshot_schema_0.6.sql:5: NOTICE:  table "users" does not exist, skipping
    DROP TABLE
    psql:/mnt/map/osm/pgsnapshot_schema_0.6.sql:6: NOTICE:  table "nodes" does not exist, skipping
    DROP TABLE
    psql:/mnt/map/osm/pgsnapshot_schema_0.6.sql:7: NOTICE:  table "ways" does not exist, skipping
    DROP TABLE
    psql:/mnt/map/osm/pgsnapshot_schema_0.6.sql:8: NOTICE:  table "way_nodes" does not exist, skipping
    DROP TABLE
    psql:/mnt/map/osm/pgsnapshot_schema_0.6.sql:9: NOTICE:  table "relations" does not exist, skipping
    DROP TABLE
    psql:/mnt/map/osm/pgsnapshot_schema_0.6.sql:10: NOTICE:  table "relation_members" does not exist, skipping
    DROP TABLE
    psql:/mnt/map/osm/pgsnapshot_schema_0.6.sql:11: NOTICE:  table "schema_info" does not exist, skipping
    DROP TABLE
    psql:/mnt/map/osm/pgsnapshot_schema_0.6.sql:14: NOTICE:  function osmosisupdate() does not exist, skipping
    DROP FUNCTION
    CREATE TABLE
    CREATE TABLE
    CREATE TABLE
                addgeometrycolumn
    ------------------------------------------------
    public.nodes.geom SRID:4326 TYPE:POINT DIMS:2
    (1 row)

    CREATE TABLE
    CREATE TABLE
    CREATE TABLE
    CREATE TABLE
    INSERT 0 1
    ALTER TABLE
    ALTER TABLE
    ALTER TABLE
    ALTER TABLE
    ALTER TABLE
    ALTER TABLE
    ALTER TABLE
    CREATE INDEX
    CREATE INDEX
    CREATE INDEX
    ALTER TABLE
    ALTER TABLE
    ALTER TABLE
    CREATE FUNCTION
    CREATE FUNCTION
    ALTER TABLE
    ALTER TABLE
    ALTER TABLE
    ALTER TABLE
    ALTER TABLE
    ALTER TABLE
    ALTER TABLE
    Jul 25, 2019 11:58:16 AM org.openstreetmap.osmosis.core.Osmosis run
    INFO: Osmosis Version 0.43.1-SNAPSHOT
    Jul 25, 2019 11:58:16 AM org.openstreetmap.osmosis.core.Osmosis run
    INFO: Preparing pipeline.
    Jul 25, 2019 11:58:16 AM org.openstreetmap.osmosis.core.Osmosis run
    INFO: Launching pipeline execution.
    Jul 25, 2019 11:58:16 AM org.openstreetmap.osmosis.core.Osmosis run
    INFO: Pipeline executing, waiting for completion.
    Jul 25, 2019 2:17:37 PM org.openstreetmap.osmosis.core.Osmosis run
    INFO: Pipeline complete.
    Jul 25, 2019 2:17:37 PM org.openstreetmap.osmosis.core.Osmosis run
    INFO: Total execution time: 8361760 milliseconds.
    Done.
    Start extraction of routing data (bfmap tools) ...
    Execute in normal mode ...
    (1/5) Create intermediate table _tmp_way_nodes ...
    Done.
    Create index on intermediate table _tmp_way_nodes ...
    Done.
    (2/5) Create intermediate table _tmp_node_counts ...
    Done.
    Create index on intermediate table _tmp_node_counts ...
    Done.
    (3/5) Create intermediate table _tmp_way_counts ...
    Done.
    Drop intermediate tables _tmp_way_nodes and _tmp_node_counts.
    Done.
    Create index on intermediate table _tmp_way_counts ...
    Done.
    (4/5) Create intermediate table _tmp_way_aggs ...
    Done.
    Drop intermediate table _tmp_way_counts.
    Done.
    Create index on intermediate table _tmp_way_aggs ...
    Done.
    (5/5) Create table temp_ways ...
    Done.
    Drop intermediate table _tmp_way_aggs.
    Done.
    Finished.
    Configuration imported.
    Table 'bfmap_ways' does not exist in database 'europe'.
    Table 'bfmap_ways' has been created.
    Inserting data ...
    15376 segments from 10000 ways inserted.
    30649 segments from 20000 ways inserted.
    45955 segments from 30000 ways inserted.
    61201 segments from 40000 ways inserted.
    76559 segments from 50000 ways inserted.
    91968 segments from 60000 ways inserted.
    107304 segments from 70000 ways inserted.
    122629 segments from 80000 ways inserted.
    138092 segments from 90000 ways inserted.
    153513 segments from 100000 ways inserted.
    168541 segments from 110000 ways inserted.
    183849 segments from 120000 ways inserted.
    198796 segments from 130000 ways inserted.
    213948 segments from 140000 ways inserted.
    229666 segments from 150000 ways inserted.
    245037 segments from 160000 ways inserted.
    260517 segments from 170000 ways inserted.
    275538 segments from 180000 ways inserted.
    290709 segments from 190000 ways inserted.
    306307 segments from 200000 ways inserted.
    321250 segments from 210000 ways inserted.
    336381 segments from 220000 ways inserted.
    351521 segments from 230000 ways inserted.
    366663 segments from 240000 ways inserted.
    381783 segments from 250000 ways inserted.
    397316 segments from 260000 ways inserted.
    412728 segments from 270000 ways inserted.
    427821 segments from 280000 ways inserted.
    443212 segments from 290000 ways inserted.
    458409 segments from 300000 ways inserted.
    473993 segments from 310000 ways inserted.
    489110 segments from 320000 ways inserted.
    504483 segments from 330000 ways inserted.
    519928 segments from 340000 ways inserted.
    535105 segments from 350000 ways inserted.
    550525 segments from 360000 ways inserted.
    565823 segments from 370000 ways inserted.
    581099 segments from 380000 ways inserted.
    596301 segments from 390000 ways inserted.
    611732 segments from 400000 ways inserted.
    626835 segments from 410000 ways inserted.
    641992 segments from 420000 ways inserted.
    657484 segments from 430000 ways inserted.
    672480 segments from 440000 ways inserted.
    687725 segments from 450000 ways inserted.
    703165 segments from 460000 ways inserted.
    718248 segments from 470000 ways inserted.
    733423 segments from 480000 ways inserted.
    748551 segments from 490000 ways inserted.
    763817 segments from 500000 ways inserted.
    779067 segments from 510000 ways inserted.
    794236 segments from 520000 ways inserted.
    809583 segments from 530000 ways inserted.
    824695 segments from 540000 ways inserted.
    839873 segments from 550000 ways inserted.
    855207 segments from 560000 ways inserted.
    870420 segments from 570000 ways inserted.
    885731 segments from 580000 ways inserted.
    900723 segments from 590000 ways inserted.
    916197 segments from 600000 ways inserted.
    931534 segments from 610000 ways inserted.
    946767 segments from 620000 ways inserted.
    962012 segments from 630000 ways inserted.
    977425 segments from 640000 ways inserted.
    992880 segments from 650000 ways inserted.
    1008067 segments from 660000 ways inserted.
    1023215 segments from 670000 ways inserted.
    1038317 segments from 680000 ways inserted.
    1053589 segments from 690000 ways inserted.
    1069008 segments from 700000 ways inserted.
    1084450 segments from 710000 ways inserted.
    1099633 segments from 720000 ways inserted.
    1114935 segments from 730000 ways inserted.
    1130197 segments from 740000 ways inserted.
    1145434 segments from 750000 ways inserted.
    1160609 segments from 760000 ways inserted.
    1175955 segments from 770000 ways inserted.
    1191070 segments from 780000 ways inserted.
    1206548 segments from 790000 ways inserted.
    1221465 segments from 800000 ways inserted.
    1236697 segments from 810000 ways inserted.
    1251905 segments from 820000 ways inserted.
    1267391 segments from 830000 ways inserted.
    1282657 segments from 840000 ways inserted.
    1297842 segments from 850000 ways inserted.
    1313233 segments from 860000 ways inserted.
    1328444 segments from 870000 ways inserted.
    1343549 segments from 880000 ways inserted.
    1358922 segments from 890000 ways inserted.
    1374066 segments from 900000 ways inserted.
    1389457 segments from 910000 ways inserted.
    1404580 segments from 920000 ways inserted.
    1419832 segments from 930000 ways inserted.
    1435229 segments from 940000 ways inserted.
    1450248 segments from 950000 ways inserted.
    1465768 segments from 960000 ways inserted.
    1480924 segments from 970000 ways inserted.
    1496218 segments from 980000 ways inserted.
    1511482 segments from 990000 ways inserted.
    1515438 segments from 992544 ways inserted.
    1515438 segments from 992544 ways inserted and finished.
    Done.
    Done.


## Graphhopper startup car Wasteroute

    { ~ }  » cd /cygdrive/c/src/WasteRoute                                                                                                                                                                                               ~ 130
    { WasteRoute }  » ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar                                                                             /cygdrive/c/src/WasteRoute
    zsh: no such file or directory: ./graphhopper.sh
    { WasteRoute }  » cd graphhopper                                                                                                                                                                            /cygdrive/c/src/WasteRoute 127
    { graphhopper } master » ./graphhopper.sh -a web -i ../osm/out.pbf -c config.yml -p car --jar web/target/graphhopper-web-0.11-SNAPSHOT.jar                                                          /cygdrive/c/src/WasteRoute/graphhopper
    ## using java 1.8.0_91 (64bit) from C:\java\jdk-8u91_x64
    ./graphhopper.sh: line 131: mvn: command not found
    ## using existing osm file ../osm/out.pbf
    ## existing jar found web/target/graphhopper-web-0.11-SNAPSHOT.jar
    ## now web. JAVA_OPTS=-Xms128m -Xmx256m
    INFO  [2020-05-08 08:28:52,573] org.eclipse.jetty.util.log: Logging initialized @1443ms to org.eclipse.jetty.util.log.Slf4jLog
    INFO  [2020-05-08 08:28:52,654] io.dropwizard.server.DefaultServerFactory: Registering jersey handler with root path prefix: /
    INFO  [2020-05-08 08:28:52,656] io.dropwizard.server.DefaultServerFactory: Registering admin handler with root path prefix: /
    INFO  [2020-05-08 08:28:52,918] io.dropwizard.bundles.assets.ConfiguredAssetsBundle: Registering ConfiguredAssetBundle with name: assets for path /maps/*
    INFO  [2020-05-08 08:28:52,927] io.dropwizard.server.ServerFactory: Starting GraphHopperApplication
                            _     _
       __ _ _ __ __ _ _ __ | |__ | |__   ___  _ __  _ __   ___ _ __
      / _` | '__/ _` | '_ \| '_ \| '_ \ / _ \| '_ \| '_ \ / _ \ '__|
     | (_| | | | (_| | |_) | | | | | | | (_) | |_) | |_) |  __/ |
      \__, |_|  \__,_| .__/|_| |_|_| |_|\___/| .__/| .__/ \___|_|
      |___/          |_|                     |_|   |_|

    INFO  [2020-05-08 08:28:52,996] org.eclipse.jetty.setuid.SetUIDListener: Opened application@19382338{HTTP/1.1,[http/1.1]}{localhost:8989}
    INFO  [2020-05-08 08:28:52,996] org.eclipse.jetty.setuid.SetUIDListener: Opened admin@66420549{HTTP/1.1,[http/1.1]}{localhost:8990}
    INFO  [2020-05-08 08:28:52,998] org.eclipse.jetty.server.Server: jetty-9.4.z-SNAPSHOT
    INFO  [2020-05-08 08:28:53,158] com.graphhopper.reader.osm.GraphHopperOSM: version 0.11|2018-05-15T16:17:53Z (5,14,4,3,3,2)
    INFO  [2020-05-08 08:28:53,161] com.graphhopper.reader.osm.GraphHopperOSM: graph CH|car|RAM_STORE|2D|NoExt|5,14,4,3,3, details:edges:422▒755(13MB), nodes:334▒899(4MB), name:(2MB), geo:1▒528▒365(6MB), bounds:7.350001462176475,8.909999778345222,51.95000064261259,53.099999459832894, CHGraph|fastest|car, shortcuts:283▒144, nodesCH:(3MB)
    INFO  [2020-05-08 08:28:53,161] com.graphhopper.http.GraphHopperManaged: loaded graph at:../osm/out-gh, data_reader_file:../osm/out.pbf, flag_encoders:car, edges:422▒755(13MB), nodes:334▒899(4MB), name:(2MB), geo:1▒528▒365(6MB), bounds:7.350001462176475,8.909999778345222,51.95000064261259,53.099999459832894, CHGraph|fastest|car, shortcuts:283▒144, nodesCH:(3MB)
    INFO  [2020-05-08 08:28:53,711] io.dropwizard.jersey.DropwizardResourceConfig: The following paths were found for the configured resources:

        GET     / (com.graphhopper.http.resources.RootResource)
        GET     /i18n (com.graphhopper.http.resources.I18NResource)
        GET     /i18n/{locale} (com.graphhopper.http.resources.I18NResource)
        GET     /info (com.graphhopper.http.resources.InfoResource)
        GET     /isochrone (com.graphhopper.http.resources.IsochroneResource)
        GET     /nearest (com.graphhopper.http.resources.NearestResource)
        GET     /route (com.graphhopper.http.resources.RouteResource)

    INFO  [2020-05-08 08:28:53,713] org.eclipse.jetty.server.handler.ContextHandler: Started i.d.j.MutableServletContextHandler@7645f03e{/,null,AVAILABLE}
    INFO  [2020-05-08 08:28:53,718] io.dropwizard.setup.AdminEnvironment: tasks =

        POST    /tasks/log-level (io.dropwizard.servlets.tasks.LogConfigurationTask)
        POST    /tasks/gc (io.dropwizard.servlets.tasks.GarbageCollectionTask)

    INFO  [2020-05-08 08:28:53,724] org.eclipse.jetty.server.handler.ContextHandler: Started i.d.j.MutableServletContextHandler@1624775{/,null,AVAILABLE}
    INFO  [2020-05-08 08:28:53,750] org.eclipse.jetty.server.AbstractConnector: Started application@19382338{HTTP/1.1,[http/1.1]}{localhost:8989}
    INFO  [2020-05-08 08:28:53,751] org.eclipse.jetty.server.AbstractConnector: Started admin@66420549{HTTP/1.1,[http/1.1]}{localhost:8990}
    INFO  [2020-05-08 08:28:53,752] org.eclipse.jetty.server.Server: Started @2623ms


### Values for CAR -> Truck - Excoder - Parameter 

CarFlagEncoder.java
        
        ...
        maxPossibleSpeed = 140;

        // autobahn
        defaultSpeedMap.put("motorway", 100);
        defaultSpeedMap.put("motorway_link", 70);
        defaultSpeedMap.put("motorroad", 90);
        // bundesstraße
        defaultSpeedMap.put("trunk", 70);
        defaultSpeedMap.put("trunk_link", 65);
        // linking bigger town
        defaultSpeedMap.put("primary", 65);
        defaultSpeedMap.put("primary_link", 60);
        // linking towns + villages
        defaultSpeedMap.put("secondary", 60);
        defaultSpeedMap.put("secondary_link", 50);
        // streets without middle line separation
        defaultSpeedMap.put("tertiary", 50);
        defaultSpeedMap.put("tertiary_link", 40);
        defaultSpeedMap.put("unclassified", 30);
        defaultSpeedMap.put("residential", 30);
        // spielstraße
        defaultSpeedMap.put("living_street", 5);
        defaultSpeedMap.put("service", 20);
        // unknown road
        defaultSpeedMap.put("road", 20);
        // forestry stuff
        defaultSpeedMap.put("track", 15);
        ...

## Railflag encoder Java 

    package com.graphhopper.routing.util;

    import com.graphhopper.util.PMap;
    import com.graphhopper.reader.ReaderNode;
    import com.graphhopper.reader.ReaderRelation;
    import com.graphhopper.reader.ReaderWay;
    import com.graphhopper.routing.util.AbstractFlagEncoder;
    import com.graphhopper.routing.util.EncodedDoubleValue;

    public class RailFlagEncoder extends AbstractFlagEncoder {

	    public RailFlagEncoder(PMap properties) {
		    super(5, 5, 0);
		    this.properties = properties;
		    intendedValues.add("railway");
		    intendedValues.add("train");
	    }

	    @Override
        public long acceptWay( ReaderWay way )
        {
            String railwayValue = way.getTag("railway");
            if (railwayValue == null)
            {
        	    if(way.hasTag("route", intendedValues)) {
        		     return acceptBit | ferryBit;
        	    }
                return 0;
            }

            if (!"rail".equals(railwayValue))
            {
        	    return 0;
            }

            return acceptBit;
        }

	    @Override
        public long handleRelationTags( ReaderRelation relation, long oldRelationFlags )
        {
            return oldRelationFlags;
        }
	
        @Override
        public String toString()
        {
            return "rail";
        }
    
        protected double getSpeed( ReaderWay way )
        {
            /*String railwayValue = way.getTag("railway");
            Integer speed = 100;
            if (speed == null)
                throw new IllegalStateException("rail, no speed found for:" + railwayValue);*/
            return 100;
        }

        @Override
	    public long handleNodeTags( ReaderNode node )
        {
            return 0;
        }

        @Override
        public long handleWayTags( ReaderWay way, long allowed, long relationCode )
        {
    	    if (!isAccept(allowed))
                return 0;

    	    long flags = 0;
    	    if (!isFerry(allowed)) {
                // get assumed speed from highway type
        	    double speed = getSpeed(way);
                speed = applyMaxSpeed(way, speed);
            
                flags = setSpeed(0, speed);

                if (way.hasTag("oneway", oneways) || way.hasTag("junction", "roundabout")) {
                    if (way.hasTag("oneway", "-1"))
                        flags |= backwardBit;
                    else
                        flags |= forwardBit;
                } else
                    flags |= directionBitMask;

            } else {
        	    double ferrySpeed = getFerrySpeed(way, 20, 20, 20);
                flags = setSpeed(flags, ferrySpeed);
                flags |= directionBitMask;
            }

            return flags;
        }
    
        @Override
        public int defineWayBits( int index, int shift )
        {
            // first two bits are reserved for route handling in superclass
            shift = super.defineWayBits(index, shift);
            speedEncoder = new EncodedDoubleValue("Speed", shift, speedBits, speedFactor, 100, 100);
            return shift + speedBits;
        }

	    @Override
	    public int getVersion() {
		    return 1;
	    }    
    }


# GRaphhopper CAR URL List 

    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5837221.0,6929465.0&point=5837221.0,6929465.0&point=5837221.0,6929465.0&point=5837221.0,6929465.0&point=5835986.0,6928015.0&point=5835986.0,6928015.0&point=5834408.0,6926469.0&point=5834408.0,6926469.0&point=5834408.0,6926469.0&point=5834408.0,6926469.0&point=5834408.0,6926469.0&point=5832939.0,6925869.0&point=5832939.0,6925869.0&point=5832428.0,6925513.0&point=5832428.0,6925513.0&point=5832428.0,6925513.0&point=5830698.0,6926418.0&point=5830698.0,6926418.0&point=5830698.0,6926418.0&point=5830698.0,6926418.0&point=5828947.0,6925610.0&point=5828947.0,6925610.0&point=5832311.0,6922396.0&point=5832337.0,6919288.0&point=5832747.0,6920348.0&point=5833880.0,6920148.0&point=5834402.0,6921183.0&point=5837007.0,6921005.0&point=5840348.0,6920026.0&point=5842268.0,6919490.0&point=5843356.0,6919113.0&point=5843356.0,6919113.0&point=5848629.0,6924914.0&point=5848848.0,6926501.0&point=5848848.0,6926501.0&point=5848848.0,6926501.0&point=5847322.0,6932655.0&point=5847322.0,6932655.0&point=5847322.0,6932655.0&point=5847322.0,6932655.0&point=5847322.0,6932655.0&point=5843922.0,6932285.0&point=5843922.0,6932285.0&point=5839753.0,6934358.0&point=5839753.0,6934358.0&point=5839594.0,6934340.0&point=5839044.0,6934836.0&point=5838995.0,6948963.0&point=5837870.0,6950001.0&point=5837675.0,7002789.0&point=5883400.0,7011917.0&point=5899356.0,7035619.0&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5901217.0,7042953.0&point=5901217.0,7042953.0&point=5901217.0,7042953.0&point=5901217.0,7042953.0&point=5901217.0,7042953.0&point=5901217.0,7042953.0&point=5901217.0,7042953.0&point=5901217.0,7042953.0&point=5901217.0,7042953.0&point=5901217.0,7042953.0&point=5898274.74,7039924.87&point=5897847.78,7039827.13&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897545.19,7038886.33&point=5897408.33,7038852.73&point=5897408.33,7038852.73&point=5897211.65,7040361.48&point=5894634.47,7039572.42&point=5894699.0,7039324.0&point=5892844.0,7032115.0&point=5890067.0,6985736.0&point=5889512.0,6982318.0&point=5874372.0,6979626.0&point=5872333.0,6938631.0&point=5862305.0,6939620.0&point=5849405.0,6940789.0&point=5849405.0,6940789.0&point=5849405.0,6940789.0&point=5849405.0,6940789.0&point=5849405.0,6940789.0&point=5849405.0,6940789.0&point=5847947.0,6936278.0&point=5842732.0,6933812.0&point=5842518.0,6931578.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5833115.0,6932527.0&point=5832295.0,6932876.0&point=5831800.0,6936749.0&point=5825071.0,6936967.0&point=5825071.0,6936967.0&point=5825071.0,6936967.0&point=5825071.0,6936967.0&point=5826182.0,6935145.0&point=5826290.0,6934792.0&point=5824479.0,6934918.0&point=5824140.0,6930944.0&point=5824140.0,6930944.0&point=5824140.0,6930944.0&point=5824140.0,6930944.0&point=5824140.0,6930944.0&point=5824140.0,6930944.0&point=5824182.0,6929064.0&point=5824099.0,6927268.0&point=5822967.0,6927457.0&point=5822967.0,6927457.0&point=5822967.0,6927457.0&point=5823943.0,6927899.0&point=5825415.0,6927910.0&point=5826251.0,6925812.0&point=5826917.0,6927663.0&point=5826917.0,6927663.0&point=5826917.0,6927663.0&point=5826917.0,6927663.0&point=5826917.0,6927663.0&point=5826917.0,6927663.0&point=5826917.0,6927663.0&point=5826917.0,6927663.0&point=5826917.0,6927663.0&point=5826917.0,6927663.0&point=5826917.0,6927663.0&point=5827161.0,6928539.0&point=5829559.0,6929448.0&point=5829559.0,6929448.0&point=5830994.0,6929050.0&point=5831516.0,6929052.0&point=5836821.0,6930031.0&point=5837863.0,6932657.0&point=5837863.0,6932657.0&point=5837863.0,6932657.0&point=5838169.0,6932649.0&point=5838169.0,6932649.0&point=5838169.0,6932649.0&point=5838169.0,6932649.0&point=5836551.0,6931818.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5831351.0,6927826.0&point=5831388.0,6928205.0&point=5831572.0,6929609.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5842248.0,6937654.0&point=5842248.0,6937654.0&point=5842248.0,6937654.0&point=5842816.0,6924613.0&point=5843322.0,6924067.0&point=5844284.0,6924322.0&point=5844288.0,6924722.0&point=5848629.0,6924914.0&point=5851216.0,6931644.0&point=5851216.0,6931644.0&point=5851216.0,6931644.0&point=5848985.0,6933276.0&point=5848511.0,6933491.0&point=5848511.0,6933491.0&point=5848511.0,6933491.0&point=5848511.0,6933491.0&point=5848511.0,6933491.0&point=5848511.0,6933491.0&point=5848511.0,6933491.0&point=5848904.0,6933907.0&point=5848875.0,6934016.0&point=5849396.0,6947038.0&point=5851933.0,6971830.0&point=5852497.0,6978257.0&point=5852497.0,6978257.0&point=5853872.0,6984798.0&point=5864723.0,6985926.0&point=5883957.84,7052574.82&point=5884135.26,7052566.85&point=5884507.25,7052768.66&point=5887119.36,7053075.65&point=5887865.0,7053829.0&point=5887865.0,7053829.0&point=5888010.0,7053826.0&point=5888030.0,7053803.0&point=5888010.0,7053826.0&point=5888010.0,7053826.0&point=5890302.0,7054281.0&point=5890302.0,7054281.0&point=5890302.0,7054281.0&point=5891685.56,7053850.79&point=5891829.21,7053789.5&point=5891829.21,7053789.5&point=5893326.27,7053625.3&point=5894361.0,7052789.0&point=5895144.75,7040971.0&point=5897102.23,7040490.77&point=5897545.19,7038886.33&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5893565.0,7032992.0&point=5893399.26,7032482.86&point=5892714.84,7032020.22&point=5883400.0,7011917.0&point=5875753.77,7009883.23&point=5875753.77,7009883.23&point=5876906.0,6997545.0&point=5876906.0,6997545.0&point=5876906.0,6997545.0&point=5876906.0,6997545.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5868939.0,6978438.0&point=5868359.94,6963833.2&point=5867057.0,6963380.0&point=5849396.0,6947038.0&point=5842856.0,6940923.0&point=5841546.0,6938932.0&point=5841364.0,6937977.0&point=5840264.0,6938241.0&point=5837042.0,6935446.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5842268.0,6919490.0&point=5842268.0,6919490.0&point=5843356.0,6919113.0&point=5845076.0,6918630.0&point=5845589.0,6918488.0&point=5853879.0,6918342.0&point=5853879.0,6918342.0&point=5853879.0,6918342.0&point=5853879.0,6918342.0&point=5853879.0,6918342.0&point=5853879.0,6918342.0&point=5853879.0,6918342.0&point=5854374.0,6918320.0&point=5859660.0,6918489.0&point=5863126.0,6923561.0&point=5862073.0,6933947.0&point=5862365.0,6934194.0&point=5855856.0,6934621.0&point=5853052.0,6934864.0&point=5849396.0,6947038.0&point=5838995.0,6948963.0&point=5838995.0,6948963.0&point=5838995.0,6948963.0&point=5838995.0,6948963.0&point=5838995.0,6948963.0&point=5838995.0,6948963.0&point=5838310.0,6949133.0&point=5838310.0,6949133.0&point=5838310.0,6949133.0&point=5838310.0,6949133.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5837870.0,6950001.0&point=5843277.0,6954680.0&point=5844378.0,6979000.0&point=5844378.0,6979000.0&point=5845383.0,6979634.0&point=5846626.0,6981331.0&point=5846626.0,6981331.0&point=5846838.0,6982481.0&point=5846838.0,6982481.0&point=5848294.0,6982527.0&point=5863410.0,6984082.0&point=5864959.0,6984079.0&point=5883016.0,6995388.0&point=5883957.84,7052574.82&point=5887210.74,7053012.13&point=5892822.16,7053341.05&point=5893281.0,7038934.0&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5897108.0,7038875.0&point=5896987.09,7039336.59&point=5895828.75,7040688.75&point=5895135.5,7040971.75&point=5894682.0,7041045.0&point=5891834.0,7045583.0&point=5891834.0,7045583.0&point=5887201.55,7051911.08&point=5887201.55,7051911.08&point=5887201.55,7051911.08&point=5887201.55,7051911.08&point=5887119.36,7053075.65&point=5887251.32,7052972.23&point=5887251.32,7052972.23&point=5887251.32,7052972.23&point=5887484.0,7052805.0&point=5887676.0,7052700.0&point=5893077.58,7052969.48&point=5894481.91,7052907.38&point=5894929.75,7042102.75&point=5895144.75,7040971.0&point=5895253.88,7040040.75&point=5896023.04,7038732.29&point=5898913.0,7037169.0&point=5899356.0,7035619.0&point=5899487.0,7001688.0&point=5900286.0,6987805.0&point=5900265.0,6987777.0&point=5900264.0,6987748.0&point=5900262.0,6987720.0&point=5889431.0,6984130.0&point=5863797.0,6978907.0&point=5862564.0,6979053.0&point=5859031.0,6969968.0&point=5859008.0,6969433.0&point=5858825.0,6967452.0&point=5857186.0,6967405.0&point=5849644.0,6949808.0&point=5847821.0,6944563.0&point=5847680.0,6940053.0&point=5846927.0,6935472.0&point=5839594.0,6934340.0&point=5839042.0,6932620.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5838057.0,6922490.0&point=5836356.0,6923577.0&point=5835986.0,6928015.0&point=5836514.0,6926961.0&point=5837470.0,6927460.0&point=5837567.0,6927632.0&point=5838257.0,6931218.92&point=5839594.0,6934340.0&point=5842248.0,6937654.0&point=5846468.0,6949681.0&point=5848181.0,6963260.0&point=5848150.0,6964256.0&point=5848150.0,6964256.0&point=5847677.0,6964784.0&point=5847677.0,6964784.0&point=5847677.0,6964784.0&point=5847677.0,6964784.0&point=5847677.0,6964784.0&point=5847677.0,6964784.0&point=5847677.0,6964784.0&point=5847677.0,6964784.0&point=5848402.0,6977668.0&point=5850852.0,6984923.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5856417.0,6986259.0&point=5856417.0,6986259.0&point=5856901.0,6990087.0&point=5860987.0,6995674.11&point=5867584.0,6997742.0&point=5872957.0,6998560.0&point=5874326.0,7017131.0&point=5877898.0,7071277.0&point=5884134.46,7053852.47&point=5884134.46,7053852.47&point=5884019.87,7054625.98&point=5884019.87,7054625.98&point=5883905.27,7054425.44&point=5883905.27,7054425.44&point=5883905.27,7054425.44&point=5884793.37,7054382.46&point=5884793.37,7054382.46&point=5885149.25,7053875.25&point=5885147.89,7053769.27&point=5885147.89,7053769.27&point=5884781.0,7053618.0&point=5884818.46,7053452.48&point=5887049.5,7053081.29&point=5887049.5,7053081.29&point=5887119.36,7053075.65&point=5893125.71,7053049.7&point=5893795.0,7052212.75&point=5895012.07,7040371.12&point=5895602.5,7039310.75&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5896886.51,7039305.15&point=5895821.54,7040688.41&point=5894394.0,7052792.0&point=5893813.23,7055731.54&point=5893907.0,7056335.0&point=5893612.0,7055833.0&point=5893487.0,7055601.0&point=5893301.1,7053513.07&point=5892411.63,7053527.75&point=5886733.68,7053227.32&point=5885768.44,7051563.13&point=5885764.41,7050087.55&point=5883440.0,7012198.0&point=5874834.0,7010163.0&point=5866761.0,7009319.0&point=5864893.0,7006160.0&point=5872100.0,7005704.0&point=5899487.0,7001688.0&point=5901025.0,6982125.0&point=5903942.0,6979941.0&point=5903942.0,6979941.0&point=5903942.0,6979941.0&point=5909810.0,6975899.0&point=5909810.0,6975899.0&point=5909810.0,6975899.0&point=5909810.0,6975899.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5868670.0,6978172.0&point=5858918.0,6976335.0&point=5858918.0,6976335.0&point=5858918.0,6976335.0&point=5858918.0,6976335.0&point=5854804.0,6975302.0&point=5848721.0,6966821.0&point=5848692.0,6964872.0&point=5848440.0,6963856.0&point=5848181.0,6963260.0&point=5844848.0,6957294.0&point=5844848.0,6957294.0&point=5839791.0,6948519.0&point=5838470.0,6944538.0&point=5838289.0,6942274.0&point=5832106.0,6939260.0&point=5832174.0,6937500.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5843359.0,6924016.0&point=5847817.0,6919968.0&point=5847579.0,6918656.0&point=5850321.0,6912173.0&point=5850321.0,6912173.0&point=5850813.0,6912420.0&point=5848848.0,6926501.0&point=5848852.0,6927017.0&point=5848645.0,6934873.0&point=5843484.0,6937924.0&point=5844948.0,6957617.0&point=5846275.0,6961199.0&point=5846352.0,6961335.0&point=5846582.0,6978726.0&point=5846582.0,6978726.0&point=5847324.0,6979218.0&point=5848791.0,6980236.0&point=5857151.0,6981084.0&point=5857151.0,6981084.0&point=5857151.0,6981084.0&point=5857151.0,6981084.0&point=5857151.0,6981084.0&point=5857151.0,6981084.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5854562.0,6990702.0&point=5858851.0,6992799.0&point=5860930.33,6995686.89&point=5876906.0,6997545.0&point=5876906.0,6997545.0&point=5878102.0,7000806.0&point=5878102.0,7000806.0&point=5880820.0,7000447.0&point=5883400.0,7011917.0&point=5886771.96,7052067.41&point=5886861.0,7052216.0&point=5890565.47,7046381.27&point=5890767.0,7045134.0&point=5890670.0,7044756.0&point=5891390.0,7044955.0&point=5894754.87,7041645.89&point=5895054.25,7040453.0&point=5895762.35,7039565.34&point=5897545.19,7038886.33&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5901708.0,7028566.0&point=5900618.0,6973011.0&point=5894559.0,6959570.0&point=5888667.0,6956249.0&point=5888667.0,6956249.0&point=5888667.0,6956249.0&point=5888667.0,6956249.0&point=5888667.0,6956249.0&point=5885204.0,6957937.0&point=5878337.0,6961302.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5874372.0,6979626.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5873165.0,6978938.0&point=5868670.0,6978172.0&point=5859582.0,6969464.0&point=5855734.0,6935652.0&point=5853088.0,6934861.0&point=5852267.0,6932863.0&point=5849064.0,6933237.0&point=5844069.0,6934260.0&point=5844076.0,6934241.0&point=5843922.0,6932285.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5843922.0,6932285.0&point=5848812.0,6935272.0&point=5848980.0,6935272.0&point=5848998.0,6935270.0&point=5850634.0,6935095.0&point=5851018.0,6935079.0&point=5855397.0,6934646.0&point=5855543.0,6934651.0&point=5870069.0,6936105.0&point=5874617.0,6941385.0&point=5874610.31,6953460.05&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5877432.39,6957924.96&point=5877432.39,6957924.96&point=5877432.39,6957924.96&point=5877432.39,6957924.96&point=5877432.39,6957924.96&point=5877432.39,6957924.96&point=5877432.39,6957924.96&point=5877432.39,6957924.96&point=5877432.39,6957924.96&point=5877432.39,6957924.96&point=5877432.39,6957924.96&point=5877432.39,6957924.96&point=5889982.0,6975389.0&point=5890067.0,6985736.0&point=5895040.0,6987446.0&point=5895995.9,7037787.76&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5892714.84,7032020.22&point=5883440.0,7012198.0&point=5880820.0,7000447.0&point=5878673.0,6997597.0&point=5878673.0,6997597.0&point=5844706.0,6997700.0&point=5844664.0,6995618.0&point=5845006.0,6992518.0&point=5845006.0,6992518.0&point=5845933.0,6985502.0&point=5846399.0,6984949.0&point=5846626.0,6981331.0&point=5852008.0,6981671.0&point=5852008.0,6981671.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5857151.0,6981084.0&point=5857272.25,6979622.74&point=5862564.0,6979053.0&point=5862564.0,6979053.0&point=5858955.0,6970026.0&point=5859017.0,6969449.0&point=5860026.0,6968621.0&point=5860218.0,6967551.0&point=5862305.0,6939620.0&point=5862305.0,6939620.0&point=5862305.0,6939620.0&point=5862305.0,6939620.0&point=5862305.0,6939620.0&point=5862305.0,6939620.0&point=5862305.0,6939620.0&point=5862305.0,6939620.0&point=5862305.0,6939620.0&point=5862305.0,6939620.0&point=5862305.0,6939620.0&point=5862305.0,6939620.0&point=5857167.0,6937617.0&point=5855734.0,6935652.0&point=5850785.0,6935100.0&point=5850634.0,6935095.0&point=5849426.0,6930035.0&point=5855708.0,6844506.0&point=5845973.0,6925184.0&point=5845973.0,6925184.0&point=5845973.0,6925184.0&point=5845973.0,6925184.0&point=5845973.0,6925184.0&point=5845973.0,6925184.0&point=5845973.0,6925184.0&point=5845973.0,6925184.0&point=5845973.0,6925184.0&point=5845973.0,6925184.0&point=5845973.0,6925184.0&point=5845973.0,6925184.0&point=5845762.0,6926244.0&point=5843778.0,6927876.0&point=5843778.0,6927876.0&point=5843778.0,6927876.0&point=5843778.0,6927876.0&point=5843778.0,6927876.0&point=5843778.0,6927876.0&point=5837221.0,6929465.0&point=5836821.0,6930031.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5837380.0,6924534.0&point=5835398.0,6924811.0&point=5834515.0,6924973.0&point=5834752.0,6923385.0&point=5833891.0,6925710.0&point=5833891.0,6925710.0&point=5834408.0,6926469.0&point=5834172.0,6926961.0&point=5834159.0,6933810.0&point=5830443.0,6934727.0&point=5830443.0,6934727.0&point=5830443.0,6934727.0&point=5828446.0,6934622.0&point=5828452.0,6934641.0&point=5829970.0,6935193.0&point=5832598.0,6936546.0&point=5832598.0,6936546.0&point=5834089.0,6936115.0&point=5837309.0,6936266.0&point=5838376.0,6944931.0&point=5838768.0,6946708.0&point=5839072.0,6947332.0&point=5839301.0,6947773.0&point=5839549.0,6948091.0&point=5839951.0,6948919.0&point=5839951.0,6948919.0&point=5842988.0,6974081.0&point=5842988.0,6974081.0&point=5842988.0,6974081.0&point=5842988.0,6974081.0&point=5842988.0,6974081.0&point=5841954.0,6977025.0&point=5844762.0,6978509.0&point=5844777.0,6981411.0&point=5844329.0,6982165.0&point=5844375.0,6982564.0&point=5844664.0,6995618.0&point=5847585.8,6996102.74&point=5847585.8,6996102.74&point=5847585.8,6996102.74&point=5847585.8,6996102.74&point=5848877.0,7038714.0&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5896266.63,7038768.95&point=5893614.2,7038862.8&point=5891834.0,7045583.0&point=5890077.17,7047095.3&point=5885839.04,7051477.03&point=5885686.49,7051668.64&point=5885286.92,7052294.08&point=5883957.84,7052574.82&point=5882573.82,7053049.93&point=5882519.5,7051820.0&point=5882656.0,7051517.0&point=5848877.0,7038714.0&point=5836080.0,7039915.0&point=5836080.0,7039915.0&point=5831474.0,7032383.0&point=5836127.0,7005948.0&point=5836127.0,7005948.0&point=5841368.0,7002574.0&point=5832853.0,7000287.0&point=5832853.0,7000287.0&point=5834685.0,6998045.0&point=5847585.8,6996102.74&point=5861200.52,6995647.65&point=5862073.0,6985073.0&point=5860107.0,6968406.0&point=5860120.0,6968371.0&point=5853271.0,6968306.0&point=5848789.0,6964503.0&point=5848332.0,6963657.0&point=5846347.0,6961326.0&point=5846039.0,6960780.0&point=5844439.0,6956586.0&point=5838777.0,6948946.0&point=5837906.0,6945167.0&point=5837790.0,6944947.0&point=5835801.0,6941379.0&point=5834246.0,6938834.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5848143.0,6925582.0&point=5863752.0,6925850.0&point=5876836.0,6921112.0&point=5876836.0,6921112.0&point=5876836.0,6921112.0&point=5879485.0,6922418.0&point=5891949.0,6926323.0&point=5889280.0,6954333.0&point=5889280.0,6954333.0&point=5888667.0,6956249.0&point=5888667.0,6956249.0&point=5888667.0,6956249.0&point=5888667.0,6956249.0&point=5885341.0,6958075.0&point=5884527.0,6994068.0&point=5884765.75,7052504.25&point=5884818.46,7053452.48&point=5884781.0,7053618.0&point=5884793.37,7054382.46&point=5884019.87,7054625.98&point=5883905.27,7054425.44&point=5882642.0,7051532.0&point=5882592.0,7051489.0&point=5869415.0,7013346.0&point=5836127.0,7005948.0&point=5836127.0,7005948.0&point=5836127.0,7005948.0&point=5836127.0,7005948.0&point=5837675.0,7002789.0&point=5837675.0,7002789.0&point=5832853.0,7000287.0&point=5817883.0,6987852.0&point=5816562.0,6988365.0&point=5816799.0,6987179.0&point=5817183.0,6986223.0&point=5816698.0,6986610.0&point=5816698.0,6986610.0&point=5815821.0,6986541.0&point=5815665.0,6987460.0&point=5812959.0,6981420.0&point=5811282.0,6976652.0&point=5811368.0,6976832.0&point=5822272.0,6980841.0&point=5822400.0,6980815.0&point=5839443.0,6975464.0&point=5833732.0,6972604.0&point=5833732.0,6972604.0&point=5830757.0,6970652.0&point=5831529.0,6943646.0&point=5831529.0,6943646.0&point=5831575.0,6935959.0&point=5832053.0,6934854.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5833385.0,6927859.0&point=5832939.0,6925869.0&point=5832428.0,6925513.0&point=5832561.0,6924030.0&point=5832133.0,6923644.0&point=5830407.0,6924660.0&point=5830145.0,6924672.0&point=5828893.0,6927497.0&point=5829038.0,6930539.0&point=5829038.0,6930539.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5838984.0,6920362.0&point=5836332.0,6920673.0&point=5836259.0,6921215.0&point=5836027.0,6921265.0&point=5836074.0,6919766.0&point=5834560.0,6920191.0&point=5833942.0,6918688.0&point=5833249.0,6918761.0&point=5832747.0,6920348.0&point=5822338.0,6927748.0&point=5819619.0,6928858.0&point=5815432.0,6933820.0&point=5812483.0,6934253.0&point=5815077.0,6939687.0&point=5815082.0,6940126.0&point=5815081.0,6940100.0&point=5815472.0,6938634.0&point=5815472.0,6938634.0&point=5824949.0,6936714.0&point=5826809.0,6935026.0&point=5827030.0,6934969.0&point=5829038.0,6930539.0&point=5834340.0,6928927.0&point=5843778.0,6927876.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5845453.0,6921353.0&point=5844507.0,6918854.0&point=5844492.0,6918792.0&point=5842980.0,6839623.0&point=5842779.09,6844024.39&point=5855708.0,6844506.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5857685.0,6916847.0&point=5853879.0,6918342.0&point=5853879.0,6918342.0&point=5858826.0,6925804.0&point=5862305.0,6939620.0&point=5879277.0,6947749.0&point=5898913.0,7037169.0&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5898913.0,7037169.0&point=5888153.0,6985104.0&point=5873165.0,6978938.0&point=5868460.0,6975962.0&point=5859031.0,6969968.0&point=5859031.0,6969968.0&point=5856521.0,6969886.0&point=5855382.0,6969534.0&point=5855410.0,6969515.0&point=5849989.0,6966665.0&point=5849101.61,6965094.35&point=5848331.0,6964170.0&point=5845799.0,6955146.0&point=5837263.0,6952244.0&point=5837530.0,6950011.0&point=5837273.0,6943898.0&point=5833846.0,6942062.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5831541.0,6925703.0&point=5831541.0,6925703.0&point=5831420.0,6926009.0&point=5830029.0,6924115.0&point=5830029.0,6924115.0&point=5829253.0,6924749.0&point=5828947.0,6925610.0&point=5827704.0,6924763.0&point=5826835.0,6925752.0&point=5824600.0,6928313.0&point=5827971.0,6926116.0&point=5827971.0,6926116.0&point=5830507.0,6927268.0&point=5830521.0,6927288.0&point=5831015.0,6929079.0&point=5853170.0,6929899.0&point=5853447.0,6930123.0&point=5853377.0,6930405.0&point=5856194.0,6930302.0&point=5853019.0,6941785.0&point=5849097.0,6945484.0&point=5849396.0,6947038.0&point=5849396.0,6947038.0&point=5849030.0,6949929.0&point=5847609.0,6946165.0&point=5846162.0,6941675.0&point=5847660.0,6940000.0&point=5847660.0,6940000.0&point=5848511.0,6933491.0&point=5849055.0,6933278.0&point=5849258.0,6934701.0&point=5851791.0,6935004.0&point=5852144.0,6934957.0&point=5853170.0,6929899.0&point=5855319.0,6914017.0&point=5863494.4,6908869.75&point=5863494.4,6908869.75&point=5863494.4,6908869.75&point=5859879.0,6906048.0&point=5852005.0,6904723.0&point=5852005.0,6904723.0&point=5851847.0,6899819.0&point=5852219.0,6896858.0&point=5852164.0,6896384.0&point=5852802.0,6872911.0&point=5870929.0,6858363.0&point=5875590.0,6856995.0&point=5895024.0,6857008.0&point=5906590.0,6992108.0&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5900281.0,6987717.0&point=5892182.0,6987620.0&point=5889512.0,6982318.0&point=5874372.0,6979626.0&point=5863797.0,6978907.0&point=5859979.0,6968765.0&point=5857186.0,6967405.0&point=5848150.0,6964256.0&point=5848014.0,6962957.0&point=5846461.0,6961528.0&point=5846352.0,6961336.0&point=5843277.0,6954680.0&point=5837370.0,6951456.0&point=5837024.0,6951374.0&point=5837024.0,6951374.0&point=5836538.0,6945230.0&point=5835485.88,6942392.45&point=5833846.0,6942062.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5827952.0,6927452.0&point=5824600.0,6928313.0&point=5816453.0,6929077.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5823559.0,6928305.0&point=5824099.0,6927268.0&point=5826008.0,6887357.0&point=5828567.75,6884588.8&point=5828707.31,6884392.08&point=5828707.31,6884392.08&point=5828707.31,6884392.08&point=5828707.31,6884392.08&point=5828707.31,6884392.08&point=5828707.31,6884392.08&point=5828707.31,6884392.08&point=5828707.31,6884392.08&point=5828707.31,6884392.08&point=5830969.2,6881968.27&point=5845167.0,6881251.0&point=5844712.0,6882426.0&point=5843616.8,6894056.23&point=5843616.8,6894056.23&point=5843616.8,6894056.23&point=5843616.8,6894056.23&point=5846454.0,6897228.0&point=5851138.0,6900209.0&point=5851377.0,6900169.0&point=5851377.0,6900169.0&point=5852005.0,6904723.0&point=5852005.0,6904723.0&point=5852219.0,6896858.0&point=5853204.0,6889961.0&point=5853204.0,6889961.0&point=5887948.0,6884567.0&point=5895024.0,6857008.0&point=5898870.0,6847130.0&point=5907933.0,6843530.0&point=5907933.0,6843530.0&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5897344.0,6981226.0&point=5894471.0,6981192.0&point=5885875.0,6966213.0&point=5885875.0,6966213.0&point=5886607.0,6955051.0&point=5886267.0,6954695.0&point=5885136.0,6957779.0&point=5877432.39,6957924.96&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5875615.0,6959011.0&point=5872100.0,6961461.0&point=5872091.0,6961509.0&point=5872091.0,6961509.0&point=5860141.0,6968257.0&point=5856484.0,6968300.0&point=5853352.0,6968333.0&point=5848678.0,6964857.0&point=5847677.0,6964784.0&point=5847529.0,6964470.0&point=5847529.0,6964470.0&point=5840795.0,6964270.0&point=5813074.0,6962366.0&point=5809779.0,6961653.0&point=5809779.0,6961653.0&point=5806416.85,6959863.53&point=5813528.0,6960756.0&point=5813896.0,6959688.0&point=5816130.0,6955624.0&point=5812745.0,6943976.0&point=5811255.52,6939820.34&point=5808120.0,6940828.0&point=5805994.0,6934417.0&point=5805994.0,6934417.0&point=5812483.0,6934253.0&point=5812483.0,6934253.0&point=5815432.0,6933820.0&point=5820880.0,6932222.0&point=5824140.0,6930944.0&point=5827086.0,6930620.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5841213.0,6930273.0&point=5840264.0,6938241.0&point=5838289.0,6942274.0&point=5828100.0,6942980.0&point=5828100.0,6942980.0&point=5831594.0,6943315.0&point=5832531.0,6936817.0&point=5847069.0,6936165.0&point=5847116.0,6935611.0&point=5848998.0,6935270.0&point=5853088.0,6934861.0&point=5853943.0,6934783.0&point=5862013.0,6934242.0&point=5862365.0,6934194.0&point=5871853.0,6930883.0&point=5868048.0,6932415.0&point=5867901.0,6932482.0&point=5867708.0,6929026.0&point=5867066.0,6928307.0&point=5867078.0,6928305.0&point=5878632.0,6924395.0&point=5860580.0,6882668.0&point=5860580.0,6882668.0&point=5887324.0,6875725.0&point=5887324.0,6875725.0&point=5898713.0,6848983.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5901787.0,6845459.0&point=5901787.0,6845459.0&point=5907933.0,6843530.0&point=5871318.0,6844059.0&point=5871318.0,6844059.0&point=5872695.0,6850120.0&point=5872695.0,6850120.0&point=5872695.0,6850120.0&point=5872695.0,6850120.0&point=5872695.0,6850120.0&point=5863501.0,6863554.0&point=5853366.19,6863868.73&point=5839935.0,6866254.0&point=5833664.33,6869107.83&point=5836694.0,6880577.0&point=5836474.0,6922047.0&point=5835829.0,6921765.0&point=5835575.0,6924209.0&point=5835002.0,6930177.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5832030.0,6929149.0&point=5831635.0,6928343.0&point=5831635.0,6928343.0&point=5820497.0,6928516.0&point=5818027.0,6929557.0&point=5816453.0,6929077.0&point=5816759.0,6929648.0&point=5820161.0,6931571.0&point=5820161.0,6931571.0&point=5822398.0,6932077.0&point=5822693.0,6935704.0&point=5824643.0,6935992.0&point=5825071.0,6936967.0&point=5826547.0,6939107.0&point=5827182.0,6941131.0&point=5827182.0,6941131.0&point=5827401.0,6941317.0&point=5828100.0,6942980.0&point=5828100.0,6942980.0&point=5828452.0,6934641.0&point=5828774.0,6934503.0&point=5828931.0,6934468.0&point=5831261.0,6932906.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5823559.0,6928305.0&point=5828567.75,6884588.8&point=5828707.31,6884392.08&point=5820291.0,6872314.0&point=5820291.0,6872314.0&point=5820291.0,6872314.0&point=5820291.0,6872314.0&point=5820291.0,6872314.0&point=5819844.0,6871652.0&point=5819103.0,6871210.0&point=5818506.0,6870327.0&point=5818506.0,6870327.0&point=5818506.0,6870327.0&point=5818506.0,6870327.0&point=5818506.0,6870327.0&point=5818506.0,6870327.0&point=5818506.0,6870327.0&point=5818506.0,6870327.0&point=5818506.0,6870327.0&point=5818506.0,6870327.0&point=5819546.0,6870728.0&point=5819017.0,6869504.0&point=5823250.0,6857617.0&point=5827537.0,6855715.0&point=5835655.0,6848832.0&point=5836147.0,6848427.0&point=5837025.0,6847676.0&point=5838219.0,6846672.0&point=5838219.0,6846672.0&point=5838219.0,6846672.0&point=5838289.0,6846587.0&point=5842030.0,6846978.0&point=5835296.24,6848654.53&point=5835201.0,6844728.0&point=5833389.0,6844876.0&point=5833389.0,6844876.0&point=5837490.0,6846207.0&point=5837490.0,6846207.0&point=5837877.0,6845267.0&point=5837574.0,6843195.0&point=5837413.0,6843226.0&point=5840923.0,6843500.0&point=5840882.0,6843044.0&point=5840794.0,6842771.0&point=5842311.0,6841825.0&point=5871417.0,6841903.0&point=5871417.0,6841903.0&point=5871417.0,6841903.0&point=5871417.0,6841903.0&point=5871417.0,6841903.0&point=5907932.0,6843549.0&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5901112.0,6988076.0&point=5900657.0,6988071.0&point=5895212.0,6987423.0&point=5886002.0,6959857.0&point=5885564.0,6958788.0&point=5885564.0,6958788.0&point=5885410.4,6958673.92&point=5883849.0,6954382.0&point=5877251.67,6945767.54&point=5871097.0,6947266.0&point=5854647.0,6955101.0&point=5843722.0,6955455.0&point=5831731.0,6955244.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5816429.0,6955024.0&point=5816429.0,6955024.0&point=5816429.0,6955024.0&point=5816429.0,6955024.0&point=5816429.0,6955024.0&point=5816429.0,6955024.0&point=5816429.0,6955024.0&point=5817499.0,6932874.0&point=5828502.0,6931912.0&point=5829915.0,6931864.0&point=5829665.0,6931482.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5827604.0,6927229.0&point=5824651.0,6928288.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814869.0,6931687.0&point=5814749.0,6931797.0&point=5812483.0,6934253.0&point=5812483.0,6934253.0&point=5812483.0,6934253.0&point=5812483.0,6934253.0&point=5812483.0,6934253.0&point=5812483.0,6934253.0&point=5812483.0,6934253.0&point=5812483.0,6934253.0&point=5812483.0,6934253.0&point=5804743.74,6935272.08&point=5804743.74,6935272.08&point=5804743.74,6935272.08&point=5804743.74,6935272.08&point=5804743.74,6935272.08&point=5814603.0,6939283.0&point=5815077.0,6939687.0&point=5822234.0,6935703.0&point=5832939.0,6925869.0&point=5842268.0,6919490.0&point=5871433.0,6910410.0&point=5880365.0,6881087.0&point=5878975.0,6875085.0&point=5877629.0,6856123.0&point=5877629.0,6856123.0&point=5898711.0,6841430.0&point=5898711.0,6841430.0&point=5897263.0,6877265.0&point=5897263.0,6877265.0&point=5897263.0,6877265.0&point=5894075.0,6873728.0&point=5882720.0,6871776.0&point=5883453.0,6868862.0&point=5883746.0,6868380.0&point=5887948.0,6884567.0&point=5887948.0,6884567.0&point=5887948.0,6884567.0&point=5893374.0,6888866.0&point=5882181.0,6919004.0&point=5881757.0,6919356.0&point=5881757.0,6919356.0&point=5881757.0,6919356.0&point=5877623.0,6913409.0&point=5876720.74,6915826.43&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5831261.0,6932906.0&point=5831122.0,6935244.0&point=5829426.0,6937698.0&point=5813704.0,6939629.0&point=5813704.0,6939629.0&point=5815077.0,6939687.0&point=5815069.0,6939892.0&point=5815154.0,6941142.0&point=5815173.0,6941477.0&point=5815945.0,6946388.0&point=5817827.0,6948474.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5821399.0,6952702.0&point=5823616.0,6956803.0&point=5823616.0,6956803.0&point=5819860.0,6945313.0&point=5819893.0,6941301.0&point=5826567.0,6941188.0&point=5827432.0,6930985.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5843930.0,6923853.0&point=5849861.16,6848389.66&point=5852210.0,6843378.0&point=5855708.0,6844506.0&point=5855708.0,6844506.0&point=5853266.82,6847973.86&point=5872695.0,6850120.0&point=5872117.0,6849781.0&point=5872117.0,6849781.0&point=5871318.0,6844059.0&point=5871208.0,6843069.0&point=5871417.0,6841903.0&point=5898711.0,6841430.0&point=5856453.0,6829486.0&point=5853960.0,6838244.0&point=5847546.0,6839182.0&point=5842777.0,6840180.0&point=5839262.0,6838631.0&point=5839190.0,6837854.0&point=5838983.0,6836220.0&point=5837084.0,6837906.0&point=5833209.0,6836207.0&point=5832263.0,6835698.0&point=5828463.0,6840061.0&point=5828474.0,6840314.0&point=5828457.0,6840367.0&point=5826035.0,6845402.0&point=5825772.0,6845428.0&point=5819870.0,6848116.0&point=5816329.0,6845810.0&point=5816532.0,6851391.0&point=5816745.0,6851790.0&point=5816745.0,6851790.0&point=5816745.0,6851790.0&point=5819866.67,6852231.22&point=5819866.67,6852231.22&point=5819866.67,6852231.22&point=5819866.67,6852231.22&point=5819866.67,6852231.22&point=5819866.67,6852231.22&point=5819866.67,6852231.22&point=5819866.67,6852231.22&point=5819866.67,6852231.22&point=5822414.0,6855708.0&point=5822278.0,6856106.0&point=5827537.0,6855715.0&point=5827537.0,6855715.0&point=5827537.0,6855715.0&point=5833664.33,6869107.83&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5834340.0,6928927.0&point=5841292.0,6927929.0&point=5843248.0,6927825.0&point=5843368.0,6920247.0&point=5844238.0,6918860.0&point=5847404.0,6918048.0&point=5850321.0,6912173.0&point=5850358.0,6911890.0&point=5850632.0,6910092.0&point=5849107.0,6903972.0&point=5849107.0,6903972.0&point=5849107.0,6903972.0&point=5849107.0,6903972.0&point=5849107.0,6903972.0&point=5848471.0,6903344.0&point=5848602.0,6902957.0&point=5850229.0,6902724.0&point=5853587.0,6902758.0&point=5852501.7,6904942.47&point=5852501.7,6904942.47&point=5851309.0,6906643.0&point=5851449.0,6908057.0&point=5850632.0,6910092.0&point=5850632.0,6910092.0&point=5854994.0,6913621.0&point=5853879.0,6918342.0&point=5857289.0,6916712.0&point=5862571.0,6922864.0&point=5863126.0,6923561.0&point=5862305.0,6939620.0&point=5849709.0,6948720.0&point=5849030.0,6949929.0&point=5837870.0,6950001.0&point=5837328.0,6950082.0&point=5810738.0,6946704.0&point=5810738.0,6946704.0&point=5812745.0,6943976.0&point=5813533.0,6942972.0&point=5808594.0,6940123.0&point=5808594.0,6940123.0&point=5807473.0,6935816.0&point=5804743.74,6935272.08&point=5804743.74,6935272.08&point=5805068.01,6935080.85&point=5805441.0,6932581.0&point=5814869.0,6931687.0&point=5822051.0,6931495.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5831529.0,6922533.0&point=5829721.0,6921959.0&point=5820291.0,6872314.0&point=5817350.0,6868324.0&point=5817206.0,6867566.0&point=5817193.0,6867581.0&point=5817891.0,6867242.0&point=5816221.83,6866569.31&point=5815989.0,6866796.0&point=5815959.0,6866783.0&point=5814567.0,6869770.0&point=5813351.0,6867727.0&point=5812613.35,6864602.94&point=5808846.0,6859724.0&point=5808846.0,6859724.0&point=5806951.0,6858429.0&point=5806951.0,6858429.0&point=5806951.0,6858429.0&point=5806951.0,6858429.0&point=5806951.0,6858429.0&point=5806951.0,6858429.0&point=5806951.0,6858429.0&point=5806951.0,6858429.0&point=5807522.0,6855783.0&point=5809796.0,6854304.0&point=5811713.0,6857336.0&point=5811713.0,6857336.0&point=5816745.0,6851790.0&point=5816532.0,6851391.0&point=5816329.0,6845810.0&point=5828457.0,6840367.0&point=5871047.0,6840107.0&point=5872590.0,6837914.0&point=5872590.0,6837916.0&point=5872695.0,6850120.0&point=5886545.0,6841034.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898870.0,6847130.0&point=5898593.0,6847230.0&point=5898409.0,6847304.0&point=5898167.0,6847402.0&point=5898174.0,6847421.0&point=5898713.0,6848983.0&point=5898713.0,6848983.0&point=5895024.0,6857008.0&point=5823363.0,6857777.0&point=5822158.0,6860227.0&point=5820910.0,6859990.0&point=5820711.0,6861417.0&point=5819706.0,6866709.0&point=5831012.0,6923201.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5814358.0,6853221.0&point=5814358.0,6853221.0&point=5812145.0,6855013.0&point=5809796.0,6854304.0&point=5806888.0,6854078.0&point=5806623.0,6854707.0&point=5807522.0,6855783.0&point=5803174.51,6857240.44&point=5802839.0,6851283.0&point=5802839.0,6851283.0&point=5802839.0,6851283.0&point=5803014.0,6850925.0&point=5803014.0,6850925.0&point=5803785.0,6848416.0&point=5807539.0,6850657.0&point=5807539.0,6850657.0&point=5808939.0,6850524.0&point=5808891.0,6850053.0&point=5808778.0,6849125.0&point=5808778.0,6849125.0&point=5808778.0,6849125.0&point=5808778.0,6849125.0&point=5808586.0,6848057.0&point=5808521.0,6847685.0&point=5809318.0,6846712.0&point=5810148.0,6845817.0&point=5810148.0,6845817.0&point=5810451.0,6843319.0&point=5811334.0,6845393.0&point=5811103.0,6848951.0&point=5811103.0,6848951.0&point=5814419.0,6846813.0&point=5814419.0,6846813.0&point=5812435.0,6845182.0&point=5812373.0,6843018.0&point=5812373.0,6843018.0&point=5812373.0,6843018.0&point=5812373.0,6843018.0&point=5812373.0,6843018.0&point=5812373.0,6843018.0&point=5812373.0,6843018.0&point=5812369.0,6842923.0&point=5815780.0,6842736.0&point=5815780.0,6842736.0&point=5816022.0,6844593.0&point=5816010.0,6844601.0&point=5816004.0,6844605.0&point=5816017.0,6844669.0&point=5816684.0,6843960.0&point=5820232.0,6841486.0&point=5820232.0,6841486.0&point=5820267.0,6842665.0&point=5820246.0,6845010.0&point=5821126.0,6844223.0&point=5823550.0,6845177.0&point=5828474.0,6840314.0&point=5828475.0,6840328.0&point=5828462.0,6840478.0&point=5852600.28,6878051.43&point=5868623.0,6934149.0&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5803785.0,6848416.0&point=5802864.0,6848659.0&point=5795283.0,6856968.0&point=5810101.0,6938640.0&point=5815084.0,6940152.0&point=5818545.0,6969575.0&point=5848294.0,6982527.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5853872.0,6984798.0&point=5801548.45,6980697.21&point=5800813.0,6980848.0&point=5800338.0,6980947.0&point=5800574.0,6977913.0&point=5809058.0,6973216.0&point=5808962.0,6964058.0&point=5779387.82,6953732.42&point=5791665.0,6949003.0&point=5797366.0,6855960.0&point=5799047.0,6858988.0&point=5799602.0,6859014.0&point=5801071.0,6859234.0&point=5801165.0,6859912.0&point=5801834.0,6856458.0&point=5803174.51,6857240.44&point=5802978.0,6851751.0&point=5802842.0,6851276.0&point=5803014.0,6850925.0&point=5800821.0,6849569.0&point=5803613.0,6849962.0&point=5805030.0,6853439.0&point=5805922.0,6854694.0&point=5805965.0,6854690.0&point=5805869.0,6854727.0&point=5805869.0,6854727.0&point=5805725.0,6855109.0&point=5806829.0,6855520.0&point=5806951.0,6858429.0&point=5808846.0,6859724.0&point=5808846.0,6859724.0&point=5813285.0,6867678.0&point=5820291.0,6872314.0&point=5820291.0,6872314.0&point=5831534.0,6929880.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5833046.0,6925356.0&point=5832982.0,6924017.0&point=5834174.0,6923991.0&point=5834582.0,6921954.0&point=5834636.0,6924150.0&point=5834636.0,6924150.0&point=5833778.0,6930620.0&point=5833778.0,6930620.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
    http://127.0.0.1:8989/maps/?point=5842368.0,6925753.0&point=5832293.0,6935383.0&point=5832294.0,6935386.0&point=5829852.0,6935309.0&point=5827950.0,6935917.0&point=5824949.0,6936714.0&point=5817102.0,6937790.0&point=5815876.0,6946573.0&point=5815660.0,6946873.0&point=5815439.0,6946981.0&point=5813044.0,6962877.0&point=5813044.0,6962877.0&point=5812838.0,6962963.0&point=5808962.0,6964058.0&point=5810839.0,6970326.0&point=5811393.0,6962284.0&point=5814377.0,6947156.0&point=5814802.0,6941902.0&point=5816985.0,6937674.0&point=5819741.0,6935686.0&point=5819764.0,6928154.0&point=5820291.0,6872314.0&point=5822104.0,6873336.0&point=5822104.0,6873336.0&point=5822104.0,6873336.0&point=5823250.0,6857617.0&point=5828445.0,6840063.0&point=5831873.0,6835375.0&point=5831873.0,6835375.0&point=5832046.0,6835562.0&point=5832108.0,6835601.0&point=5832159.0,6835633.0&point=5831805.0,6887148.0&point=5834241.0,6888404.0&point=5848889.0,6902618.0&point=5849690.0,6902625.0&point=5849937.0,6902678.0&point=5851880.0,6904428.0&point=5852501.7,6904942.47&point=5852498.0,6904925.0&point=5855539.0,6906211.0&point=5854671.0,6900000.0&point=5887948.0,6884567.0&point=5887948.0,6884567.0&point=5900841.0,6921551.0&point=5904908.0,6992962.0&point=5906897.0,6991872.0&point=5907658.0,7038354.0&point=5907658.0,7038354.0&point=5842368.0,6925753.0&locale=de&vehicle=car&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale
