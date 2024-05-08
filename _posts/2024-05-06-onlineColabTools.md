---
layout: post
title: Online-Colaborations-Tools
categories: 
tags: [ Colab, Web, Webflow, Tools, WebUI]
lastupdate: 
date: 2024-05-06
---

![](../pics/2024-05-06-onlineColabTools_image_1.png)
- [Online Colaboration Tools](#online-colaboration-tools)
  - [Chat](#chat)
    - [Libra Chat (ohne Anmeldung)](#libra-chat-ohne-anmeldung)
  - [Web App Design und Run](#web-app-design-und-run)
    - [Flutter Flow](#flutter-flow)
  - [Draw Editor - Whiteborad](#draw-editor---whiteborad)
    - [Multiuser Draw Editor Excalidraw (OSS)  ohne Anmeldung](#multiuser-draw-editor-excalidraw-oss--ohne-anmeldung)
    - [draw.io Online Zeichen - Editor (OSS) / ohne Anmeldung](#drawio-online-zeichen---editor-oss--ohne-anmeldung)
    - [bpmn.io (ohne Anmeldung ) - von camunda](#bpmnio-ohne-anmeldung----von-camunda)
      - [Token Simulation](#token-simulation)
    - [GenMyModel](#genmymodel)
      - [Generators](#generators)
      - [Projekt Type Selection](#projekt-type-selection)
      - [UML - Diagram Typen](#uml---diagram-typen)
    - [Miro Board](#miro-board)
    - [PlantUML - Generator](#plantuml---generator)
      - [Liste der Modellierungs-Diagramm-Sprachen](#liste-der-modellierungs-diagramm-sprachen)
      - [Beispiel Usecase Diagram](#beispiel-usecase-diagram)
      - [Beispiel Class Diagram](#beispiel-class-diagram)
  - [BPMN Suites](#bpmn-suites)
    - [Signavio - Academic](#signavio---academic)
    - [Camunda](#camunda)
    - [Camunda Formular Builder](#camunda-formular-builder)
  - [Multiuser Text Editor](#multiuser-text-editor)
    - [Etherpad - OSS](#etherpad---oss)
  - [Office - Word - Excel - Powerpoint](#office---word---excel---powerpoint)
    - [Google Documents](#google-documents)
    - [MS Teams](#ms-teams)
    - [CryptPad (ohne Anmeldung)](#cryptpad-ohne-anmeldung)
  - [Online Feedback](#online-feedback)
    - [Mentimeter](#mentimeter)
    - [Padlet -](#padlet--)
  - [Projekt-Management](#projekt-management)
    - [Jira - Confluence](#jira---confluence)


# Online Colaboration Tools 

## Chat 
### Libra Chat (ohne Anmeldung)

![](../pics/2024-05-06-onlineColabTools_image_2.png)

![](../pics/2024-05-06-onlineColabTools_image_3.png)

<https://web.libera.chat/#IIT2023>

## Web App Design und Run 

### Flutter Flow 

![](../pics/2024-05-06-onlineColabTools_image_4.png)

![](../pics/2024-05-06-onlineColabTools_image_5.png)

![](../pics/2024-05-06-onlineColabTools_image_6.png)

##  Draw Editor - Whiteborad 
### Multiuser Draw Editor Excalidraw (OSS)  ohne Anmeldung 

![](../pics/2024-05-06-onlineColabTools_image_7.png)

<https://excalidraw.com/>

<https://github.com/excalidraw/excalidraw>

### draw.io Online Zeichen - Editor (OSS) / ohne Anmeldung 

![](../pics/2024-05-06-onlineColabTools_image_8.png)

![](../pics/2024-05-06-onlineColabTools_image_9.png)

<https://app.diagrams.net/>

<https://github.com/jgraph/drawio>
### bpmn.io (ohne Anmeldung ) - von camunda 

![](../pics/2024-05-06-onlineColabTools_image_10.png)

![](../pics/2024-05-06-onlineColabTools_image_11.png)

![](../pics/2024-05-06-onlineColabTools_image_12.png)

https://demo.bpmn.io/
#### Token Simulation 

https://github.com/bpmn-io/bpmn-js-token-simulation

### GenMyModel 

![](../pics/2024-05-06-onlineColabTools_image_13.png)
#### Generators 

![](../pics/2024-05-06-onlineColabTools_image_14.png)
#### Projekt Type Selection 

![](../pics/2024-05-06-onlineColabTools_image_15.png)
#### UML - Diagram Typen 

![](../pics/2024-05-06-onlineColabTools_image_16.png)


### Miro Board 

![](../pics/2024-05-06-onlineColabTools_image_17.png)


![](../pics/2024-05-06-onlineColabTools_image_18.png)


![](../pics/2024-05-06-onlineColabTools_image_19.png)


### PlantUML - Generator 
#### Liste der Modellierungs-Diagramm-Sprachen

![](../pics/2024-05-06-onlineColabTools_image_20.png)

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

![](../pics/2024-05-06-onlineColabTools_image_21.png)
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

![](../pics/2024-05-06-onlineColabTools_image_22.png)

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

![](../pics/2024-05-06-onlineColabTools_image_23.png)

<https://www.plantuml.com/plantuml/uml/XP5FIZGn4CNtTOgYDz-dq8FYhd4nRaPtWYvSIjAfwGxaZoGLNAYtcJDuWRcOIIRJ3eAugJn-nNjvdLv75e6JDM1eoyWUWvvcHgK3ZQozWt_iNmgNdjdRayLeH8nu9rB4Dq1y5KuDJtd01xJTWqWsxpAegk_xJaXBCIOtTNXpb5Ug6KvHYJJxdPleURG3Af-aeSna8Cq_sBp_d2jgP2bGwjHoMn4a3RWf1vOK2ZJEZkwpsEPhnfd-dmsu-Aknk-p-R5mJwnLEM1hmaODs4o06EGse7N-NsP2BJ07XA7uDRuPRaljTKeG0Yxn-x_lov536eM6VZzNglAlF3MKqtd3z9sKSyKN5IvssAh2QkiD7mPgSIjPy0G00>

## BPMN Suites

### Signavio - Academic  
![](../pics/2024-05-06-onlineColabTools_image_24.png)

![](../pics/2024-05-06-onlineColabTools_image_25.png)

![](../pics/2024-05-06-onlineColabTools_image_26.png)

![](../pics/2024-05-06-onlineColabTools_image_27.png)

![](../pics/2024-05-06-onlineColabTools_image_28.png)

<https://academic.signavio.com/p/explorer>

### Camunda 
![](../pics/2024-05-06-onlineColabTools_image_29.png)

### Camunda Formular Builder

![](../pics/2024-05-06-onlineColabTools_image_30.png)

<https://demo.bpmn.io/form/new>

## Multiuser Text Editor 

### Etherpad - OSS 

![](../pics/2024-05-06-onlineColabTools_image_31.png)

![](../pics/2024-05-06-onlineColabTools_image_32.png)

![](../pics/2024-05-06-onlineColabTools_image_33.png)


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

![](../pics/2024-05-06-onlineColabTools_image_34.png)

![](../pics/2024-05-06-onlineColabTools_image_35.png)

![](../pics/2024-05-06-onlineColabTools_image_36.png)

![](../pics/2024-05-06-onlineColabTools_image_37.png)

![](../pics/2024-05-06-onlineColabTools_image_38.png)

## Online Feedback 

### Mentimeter 


### Padlet - 
![](../pics/2024-05-06-onlineColabTools_image_30.png)

![](../pics/2024-05-06-onlineColabTools_image_39.png)

<https://padlet.com/dashboard/gallery/all>

## Projekt-Management 

### Jira - Confluence 

![](../pics/2024-05-06-onlineColabTools_image_40.png)

![](../pics/2024-05-06-onlineColabTools_image_41.png)


![](../pics/tmp1715176390104_2024-05-06-onlineColabTools_image_39.png)