---
layout: post
title: Online-Colaborations-Tools
categories: []
tags:
  - Colab
  - Web
  - Webflow
  - Tools
  - WebUI
date: 2024-05-06
---

![](../pics/2024-05-06-onlineColabTools_image_1.webp)


# Online Collaboration Tools 



## Chat 
### Libra Chat (ohne Anmeldung)

![](../pics/2024-05-06-onlineColabTools_image_2.webp)

![](../pics/2024-05-06-onlineColabTools_image_3.webp)

<https://web.libera.chat/#IIT2023>

## Web App Design und Run 

### Flutter Flow 

![](../pics/2024-05-06-onlineColabTools_image_4.webp)

![](../pics/2024-05-06-onlineColabTools_image_5.webp)

![](../pics/2024-05-06-onlineColabTools_image_6.webp)

##  Draw Editor - Whiteborad 
### Multiuser Draw Editor Excalidraw (OSS)  ohne Anmeldung 

![](../pics/2024-05-06-onlineColabTools_image_7.webp)

<https://excalidraw.com/>

<https://github.com/excalidraw/excalidraw>

### draw.io Online Zeichen - Editor (OSS) / ohne Anmeldung 
<https://app.diagrams.net/>

<https://github.com/jgraph/drawio>

#### UML KD

![](../pics/2024-05-06-onlineColabTools_image_8.webp)
#### Auswahl Vorlagen 
![](../pics/2024-05-06-onlineColabTools_image_9.webp)
#### EPK 


![](../pics/2024-05-06-onlineColabTools_image_10.webp)


### bpmn.io (ohne Anmeldung ) - von camunda 

![](../pics/2024-05-06-onlineColabTools_image_11.webp)

![](../pics/2024-05-06-onlineColabTools_image_12.webp)

![](../pics/2024-05-06-onlineColabTools_image_13.webp)

https://demo.bpmn.io/
#### Token Simulation 

https://github.com/bpmn-io/bpmn-js-token-simulation

### GenMyModel 

![](../pics/2024-05-06-onlineColabTools_image_14.webp)
#### Generators 

![](../pics/2024-05-06-onlineColabTools_image_15.webp)
#### Projekt Type Selection 

![](../pics/2024-05-06-onlineColabTools_image_16.webp)
#### UML - Diagram Typen 

![](../pics/2024-05-06-onlineColabTools_image_17.webp)

#### Beispiel BPMN mit Animation 
![](../pics/2024-05-06-onlineColabTools_image_18.webp)
#### Beispiel UML Klassendiagramm
![](../pics/2024-05-06-onlineColabTools_image_19.webp)

![](../pics/2024-05-06-onlineColabTools_image_20.webp)
![](../pics/2024-05-06-onlineColabTools_image_21.webp)
#### Beispiel Komponenten Diagramm 
![](../pics/2024-05-06-onlineColabTools_image_22.webp)

#### Beispiel UML Usecase 
![](../pics/2024-05-06-onlineColabTools_image_23.webp)
![](../pics/2024-05-06-onlineColabTools_image_24.webp)
### Miro Board 

![](../pics/2024-05-06-onlineColabTools_image_25.webp)


![](../pics/2024-05-06-onlineColabTools_image_26.webp)


![](../pics/2024-05-06-onlineColabTools_image_27.webp)


### PlantUML - Generator 
#### Liste der Modellierungs-Diagramm-Sprachen

![](../pics/2024-05-06-onlineColabTools_image_28.webp)

<https://plantuml.com/sitemap-language-specification>

<https://crashedmind.github.io/PlantUMLHitchhikersGuide/layout/layout.html>

<https://plantuml.com/guide>

#### Beispiel Usecase Diagram
```
@startuml
left to right direction
skinparam packageStyle rectangle
actor customer
actor clerk

rectangle checkout {
  customer -- (payment)
  (payment) -- clerk
}
@enduml
```

![](../pics/2024-05-06-onlineColabTools_image_29.webp)
```
@startuml
' left to right direction
skinparam packageStyle rectangle
actor customer
actor clerk

rectangle checkout {
  customer -- (payment)
  (payment) - clerk
  (payment) ..>(identification) : <<include>>
  (help) .> (payment) : <<extends>>
}
@enduml

```

![](../pics/2024-05-06-onlineColabTools_image_30.webp)

#### Beispiel Class Diagram 
``` code 
@startuml
left to right direction
'top to bottom direction
class Haus {
  wand:Wand
}
Haus --- "abmessung" Abmessung3d
class Raum {
  raumnummer: String
}
Raum ---"abmessung" Abmessung3d

class Abmessung3d{
  länge_cm: double
  breite_cm: double
  höhe_cm: double
}

class Wand {
  berechneOberfläche(): double
}

Wand "1"--"abmessung" Abmessung3d

class Farbe {
  name: String
  rbg: int
}

class Tür
Tür --"abmessung" Abmessung3d
Tür "1"--"0..*" Fenster 
class Fenster 
Fenster --"abmessung" Abmessung3d
class Gebäude 
Wand "1"--"0..*" Tür
Gebäude <|--Haus
Haus "1"*--- "1..*" Raum
Raum "1"---"1..*" Wand
Wand "1"---"0..*" Fenster 
Wand "1..*"---"farbe" Farbe


@enduml
```

![](../pics/2024-05-06-onlineColabTools_image_31.webp)

<https://www.plantuml.com/plantuml/uml/XP5FIZGn4CNtTOgYDz-dq8FYhd4nRaPtWYvSIjAfwGxaZoGLNAYtcJDuWRcOIIRJ3eAugJn-nNjvdLv75e6JDM1eoyWUWvvcHgK3ZQozWt_iNmgNdjdRayLeH8nu9rB4Dq1y5KuDJtd01xJTWqWsxpAegk_xJaXBCIOtTNXpb5Ug6KvHYJJxdPleURG3Af-aeSna8Cq_sBp_d2jgP2bGwjHoMn4a3RWf1vOK2ZJEZkwpsEPhnfd-dmsu-Aknk-p-R5mJwnLEM1hmaODs4o06EGse7N-NsP2BJ07XA7uDRuPRaljTKeG0Yxn-x_lov536eM6VZzNglAlF3MKqtd3z9sKSyKN5IvssAh2QkiD7mPgSIjPy0G00>

## BPMN Suites

### Signavio - Academic  

![](../pics/2024-05-06-onlineColabTools_image_32.webp)


#### Beispiel BPMN Token 
![](../pics/2024-05-06-onlineColabTools_image_33.webp)


#### Beispiel EPK
![](../pics/2024-05-06-onlineColabTools_image_34.webp)

#### Beispiel UML Klassendiagramm 

![](../pics/2024-05-06-onlineColabTools_image_35.webp)

#### Beispiel UML Usecase Diagramm 

![](../pics/2024-05-06-onlineColabTools_image_36.webp)

<https://academic.signavio.com/p/explorer>

### Camunda 
![](../pics/2024-05-06-onlineColabTools_image_37.webp)

### Camunda Formular Builder

![](../pics/2024-05-06-onlineColabTools_image_38.webp)

<https://demo.bpmn.io/form/new>

## Multiuser Text Editor 

### Etherpad - OSS 

![](../pics/2024-05-06-onlineColabTools_image_39.webp)

![](../pics/2024-05-06-onlineColabTools_image_40.webp)


![](../pics/2024-05-06-onlineColabTools_image_41.webp)


Testinstanz: 
<https://etherpad.wikimedia.org/>

Sites That Run Etherpad:

<https://github.com/ether/etherpad-lite/wiki/Sites-That-Run-Etherpad#sites-that-run-etherpad>

<https://etherpad.org/#/#download>
<https://github.com/ether/etherpad-lite>

<https://de.m.wikipedia.org/wiki/Etherpad>

## Office - Word - Excel - Powerpoint 

### Google Documents 

### MS Teams 

### CryptPad (ohne Anmeldung) 

![](../pics/2024-05-06-onlineColabTools_image_42.webp)

![](../pics/2024-05-06-onlineColabTools_image_43.webp)
#### Beispiel Multiuser - Whiteboard 

![](../pics/2024-05-06-onlineColabTools_image_44.webp)



![](../pics/2024-05-06-onlineColabTools_image_45.webp)

![](../pics/2024-05-06-onlineColabTools_image_46.webp)

## Online Feedback 

### Mentimeter 


### Padlet - 
![](../pics/2024-05-06-onlineColabTools_image_38.webp)

![](../pics/2024-05-06-onlineColabTools_image_47.webp)

<https://padlet.com/dashboard/gallery/all>

## Projekt-Management 

### Jira - Confluence 

#### Beispiel Zeitleiste Gantt 

![](../pics/2024-05-06-onlineColabTools_image_48.webp)

#### Beispiel Kanban Board 
![](../pics/2024-05-06-onlineColabTools_image_49.webp)


![](../pics/tmp1715176390104_2024-05-06-onlineColabTools_image_39.png)

![](../pics/2024-05-06-onlineColabTools_image_50.webp)