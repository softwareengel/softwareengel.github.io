---
layout: post
title: Online-Colaborations-Tools
categories: 
tags: [ Colab, Web, Webflow, Tools, WebUI]
lastupdate: 
date: 2024-05-06
---

![](../pics/2024-05-06-onlineColabTools_image_1_20240517094136.png)


# Online Colaboration Tools 



## Chat 
### Libra Chat (ohne Anmeldung)

![](../pics/2024-05-06-onlineColabTools_image_2_20240517094136.png)

![](../pics/2024-05-06-onlineColabTools_image_3_20240517094136.png)

<https://web.libera.chat/#IIT2023>

## Web App Design und Run 

### Flutter Flow 

![](../pics/2024-05-06-onlineColabTools_image_4_20240517094136.png)

![](../pics/2024-05-06-onlineColabTools_image_5_20240517094136.png)

![](../pics/2024-05-06-onlineColabTools_image_6_20240517094136.png)

##  Draw Editor - Whiteborad 
### Multiuser Draw Editor Excalidraw (OSS)  ohne Anmeldung 

![](../pics/2024-05-06-onlineColabTools_image_7_20240517094136.png)

<https://excalidraw.com/>

<https://github.com/excalidraw/excalidraw>

### draw.io Online Zeichen - Editor (OSS) / ohne Anmeldung 
<https://app.diagrams.net/>

<https://github.com/jgraph/drawio>

#### UML KD

![](../pics/2024-05-06-onlineColabTools_image_8_20240517094136.png)
#### Auswahl Vorlagen 
![](../pics/2024-05-06-onlineColabTools_image_9_20240517094136.png)
#### EPK 


![](../pics/Pasted%20image%2020240603190728.png)


### bpmn.io (ohne Anmeldung ) - von camunda 

![](../pics/2024-05-06-onlineColabTools_image_10_20240517094136.png)

![](../pics/2024-05-06-onlineColabTools_image_11_20240517094136.png)

![](../pics/2024-05-06-onlineColabTools_image_12_20240517094136.png)

https://demo.bpmn.io/
#### Token Simulation 

https://github.com/bpmn-io/bpmn-js-token-simulation

### GenMyModel 

![](../pics/2024-05-06-onlineColabTools_image_13_20240517094136.png)
#### Generators 

![](../pics/2024-05-06-onlineColabTools_image_14_20240517094136.png)
#### Projekt Type Selection 

![](../pics/2024-05-06-onlineColabTools_image_15_20240517094136.png)
#### UML - Diagram Typen 

![](../pics/2024-05-06-onlineColabTools_image_16_20240517094136.png)

#### Beispiel BPMN mit Animation 
![](../pics/2024-05-06-onlineColabTools_image_17_20240517094136.png)
#### Beispiel UML Klassendiagramm
![](../pics/2024-05-06-onlineColabTools_image_18_20240517094136.png)

![](../pics/2024-05-06-onlineColabTools_image_19_20240517094136.png)
![](../pics/2024-05-06-onlineColabTools_image_20_20240517094136.png)
#### Beispiel Komponenten Diagramm 
![](../pics/2024-05-06-onlineColabTools_image_21_20240517094136.png)

#### Beispiel UML Usecase 
![](../pics/2024-05-06-onlineColabTools_image_22_20240517094136.png)
![](../pics/2024-05-06-onlineColabTools_image_23_20240517094136.png)
### Miro Board 

![](../pics/2024-05-06-onlineColabTools_image_24_20240517094136.png)


![](../pics/2024-05-06-onlineColabTools_image_25_20240517094136.png)


![](../pics/2024-05-06-onlineColabTools_image_26_20240517094136.png)


### PlantUML - Generator 
#### Liste der Modellierungs-Diagramm-Sprachen

![](../pics/2024-05-06-onlineColabTools_image_27_20240517094136.png)

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

![](../pics/2024-05-06-onlineColabTools_image_28_20240517094136.png)
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

![](../pics/2024-05-06-onlineColabTools_image_29_20240517094136.png)

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

![](../pics/2024-05-06-onlineColabTools_image_30_20240517094136.png)

<https://www.plantuml.com/plantuml/uml/XP5FIZGn4CNtTOgYDz-dq8FYhd4nRaPtWYvSIjAfwGxaZoGLNAYtcJDuWRcOIIRJ3eAugJn-nNjvdLv75e6JDM1eoyWUWvvcHgK3ZQozWt_iNmgNdjdRayLeH8nu9rB4Dq1y5KuDJtd01xJTWqWsxpAegk_xJaXBCIOtTNXpb5Ug6KvHYJJxdPleURG3Af-aeSna8Cq_sBp_d2jgP2bGwjHoMn4a3RWf1vOK2ZJEZkwpsEPhnfd-dmsu-Aknk-p-R5mJwnLEM1hmaODs4o06EGse7N-NsP2BJ07XA7uDRuPRaljTKeG0Yxn-x_lov536eM6VZzNglAlF3MKqtd3z9sKSyKN5IvssAh2QkiD7mPgSIjPy0G00>

## BPMN Suites

### Signavio - Academic  

![](../pics/2024-05-06-onlineColabTools_image_31_20240517094136.png)


#### Beispiel BPMN Token 
![](../pics/2024-05-06-onlineColabTools_image_32_20240517094136.png)


#### Beispiel EPK
![](../pics/2024-05-06-onlineColabTools_image_33_20240517094136.png)

#### Beispiel UML Klassendiagramm 

![](../pics/2024-05-06-onlineColabTools_image_34_20240517094136.png)

#### Beispiel UML Usecase Diagramm 

![](../pics/2024-05-06-onlineColabTools_image_35_20240517094136.png)

<https://academic.signavio.com/p/explorer>

### Camunda 
![](../pics/2024-05-06-onlineColabTools_image_36_20240517094136.png)

### Camunda Formular Builder

![](../pics/2024-05-06-onlineColabTools_image_37_20240517094136.png)

<https://demo.bpmn.io/form/new>

## Multiuser Text Editor 

### Etherpad - OSS 

![](../pics/2024-05-06-onlineColabTools_image_38_20240517094136.png)

![](../pics/2024-05-06-onlineColabTools_image_39_20240517094136.png)


![](../pics/2024-05-06-onlineColabTools_image_40_20240517094136.png)


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

![](../pics/2024-05-06-onlineColabTools_image_41_20240517094136.png)

![](../pics/2024-05-06-onlineColabTools_image_42_20240517094136.png)
#### Beispiel Multiuser - Whiteboard 

![](../pics/2024-05-06-onlineColabTools_image_43_20240517094136.png)



![](../pics/2024-05-06-onlineColabTools_image_44_20240517094136.png)

![](../pics/2024-05-06-onlineColabTools_image_45_20240517094136.png)

## Online Feedback 

### Mentimeter 


### Padlet - 
![](../pics/2024-05-06-onlineColabTools_image_37_20240517094136.png)

![](../pics/2024-05-06-onlineColabTools_image_46_20240517094136.png)

<https://padlet.com/dashboard/gallery/all>

## Projekt-Management 

### Jira - Confluence 

#### Beispiel Zeitleiste Gantt 

![](../pics/2024-05-06-onlineColabTools_image_47_20240517094136.png)

#### Beispiel Kanban Board 
![](../pics/2024-05-06-onlineColabTools_image_48_20240517094136.png)


![](../pics/tmp1715176390104_2024-05-06-onlineColabTools_image_39.png)

![](../pics/2024-05-06-onlineColabTools_image_49_20240517094136.png)