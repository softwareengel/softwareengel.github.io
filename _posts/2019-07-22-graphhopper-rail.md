# Graphhopper Rail 

https://github.com/geofabrik/OpenRailRouting 

## start MapMatch 
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
![](./pic/capture_22072019_113652_002.jpg))

![](./pic/capture_22072019_113038_001.jpg)
Routing Arnsberg:
![](./pic/capture_22072019_120913_003.jpg)
Routing Europa:
![](./pic/capture_22072019_171154_001.jpg)

Requerst für Map:

    http://127.0.0.1:8989/maps/?point=43.576411%2C1.417236&point=45.721522%2C4.833984&point=46.927759%2C7.294922&point=44.43378%2C11.359863&point=42.037054%2C12.579346&point=43.691708%2C10.371094&point=47.085085%2C15.402832&point=45.809658%2C15.957642&point=48.224673%2C16.391602&point=50.092393%2C14.436035&point=52.106505%2C20.588379&point=47.82422%2C18.995361&point=52.469397%2C13.359375&point=53.842805%2C10.6073&point=54.487591%2C9.817657&point=55.252512%2C9.457855&point=55.496749%2C9.461975&point=55.652798%2C12.337646&point=59.277108%2C17.097473&point=52.352119%2C9.761353&point=51.165567%2C6.394043&point=48.814099%2C2.329102&point=44.750634%2C-0.527344&point=41.51886%2C-1.465302&point=41.599013%2C0.598755&point=40.128491%2C-3.779297&locale=de&vehicle=alltracks&weighting=fastest&elevation=false&use_miles=false&layer=Omniscale

Requerst für OSM-Map auf hq.softwareengel.de:
    http://hq.softwareengel.de:8989/maps/?point=50.945882%2C7.013526&point=51.091448%2C7.013397&point=51.167719%2C7.012711&point=51.273944%2C7.229004&locale=de&vehicle=alltracks&weighting=fastest&elevation=false&use_miles=false&layer=OpenStreetMap

    http://hq.softwareengel.de:8989/maps/?point=51.344339%2C6.833496&point=48.893615%2C2.416992&point=45.821143%2C4.866943&point=41.516804%2C2.213745&point=43.249204%2C-1.977539&point=40.722283%2C-3.180542&point=39.070379%2C-8.87146&point=38.401949%2C-0.681152&point=41.668809%2C-0.845947&point=43.560491%2C1.411743&point=44.809122%2C-0.593262&point=47.184113%2C-1.419983&point=44.658885%2C10.851402&point=44.067854%2C12.480469&point=41.934977%2C12.507935&point=46.494611%2C11.299438&point=47.085085%2C15.424805&point=48.188063%2C11.590576&point=50.071244%2C14.436035&point=53.514185%2C10.041504&point=55.66984%2C12.474976&point=59.279047%2C18.006592&point=59.377988%2C13.535156&point=59.927496%2C10.799561&point=57.715885%2C11.942139&point=50.348966%2C19.651794&point=54.597528%2C25.3125&point=55.544173%2C34.909058&point=53.388243%2C34.035645&point=52.462704%2C31.014404&point=52.295042%2C21.005859&locale=de&vehicle=alltracks&weighting=fastest&elevation=false&use_miles=false&layer=OpenStreetMap

    http://hq.softwareengel.de:8989/maps/?point=47.137425%2C15.336914&point=46.721035%2C14.364624&point=51.351201%2C4.454956&point=51.158677%2C3.251953&point=50.937662%2C1.757813&point=51.549751%2C-0.159302&point=52.516221%2C-1.801758&point=55.890716%2C-4.042969&point=48.908059%2C2.438965&point=48.118434%2C-1.532593&point=45.79817%2C4.855957&point=44.962855%2C-0.22522&point=43.258706%2C-1.978912&point=41.75902%2C-0.823975&point=39.532644%2C-0.32341&point=37.920368%2C-4.721375&point=37.492294%2C-5.932617&point=38.603993%2C-9.091187&point=41.120228%2C-8.638&point=43.329174%2C-8.44162&point=36.259778%2C-5.438232&point=40.423951%2C-3.435974&point=43.794146%2C7.380409&point=41.95132%2C12.414551&point=41.07521%2C14.205322&point=44.072787%2C15.379486&point=42.660222%2C21.084137&point=42.644898%2C23.549194&point=43.620171%2C24.675293&point=41.136262%2C28.601532&point=39.970806%2C32.541504&point=38.634036%2C35.194702&point=40.526327%2C43.005981&point=41.607228%2C44.868164&point=43.197167%2C44.615479&point=38.444985%2C38.259888&point=38.552461%2C27.03186&point=38.117272%2C23.806&point=45.371443%2C27.938232&point=47.338823%2C31.096802&point=48.904449%2C33.299561&point=47.82422%2C34.887085&point=49.435985%2C34.557495&point=51.542919%2C39.243164&point=55.606281%2C37.63504&point=59.161852%2C40.0177&point=51.648703%2C36.00769&point=50.454007%2C30.695801&point=54.669066%2C25.3125&point=52.140231%2C20.98938&point=50.014799%2C19.940186&point=51.14834%2C17.097473&point=48.283193%2C16.430054&point=45.863238%2C22.983398&point=47.480088%2C19.25354&point=44.087585%2C12.420044&point=45.479392%2C12.233276&point=45.69467%2C13.85376&point=44.427896%2C8.889313&point=52.038977%2C4.537354&point=52.328625%2C5.015259&point=50.986099%2C7.025757&point=51.495065%2C7.341614&point=52.24462%2C7.981567&point=53.041213%2C8.909912&point=51.55829%2C9.920654&point=51.349485%2C9.516907&point=50.155786%2C8.640747&point=49.477048%2C10.980835&point=48.037692%2C11.585083&point=47.802087%2C13.068237&point=48.806863%2C9.217529&point=47.393701%2C8.491058&point=52.449314%2C9.733887&point=53.555606%2C9.935074&point=54.13026%2C12.21405&point=54.77693%2C9.50592&point=55.665193%2C12.461243&point=55.583002%2C12.996826&point=56.14708%2C13.757629&point=59.850333%2C10.789948&point=60.401645%2C5.419006&point=59.293942%2C18.019638&point=62.408185%2C17.232056&point=59.380786%2C25.054321&point=60.524861%2C25.153198&point=56.98989%2C24.180908&point=52.059246%2C11.68396&point=51.013755%2C13.801575&point=51.426614%2C12.367859&point=52.566334%2C13.084717&locale=de&vehicle=alltracks&weighting=fastest&elevation=false&use_miles=false&layer=OpenStreetMap

## Web Soap UI Client mit POST und XML 
![](./pic/capture_22072019_165705_001.jpg)

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
![](./pic/capture_22072019_171453_002.jpg)



# Berechnung Ergebnis des GH Rail Map Matchings
![](./pic/capture_22072019_131603_004.jpg)

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

![](./pic/capture_22072019_131852_005.jpg)


## Beispiel config.yml
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


# Shell Notizen 

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
