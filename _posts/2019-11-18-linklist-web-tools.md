---
layout: post
title: LinkList - 
categories: [Links]
tags: [Links]
---

# Research

## Literature

### Skript

<http://www.netzmafia.de/skripten/index.html>

### Paper Search

"Schattenbibliotheken" wie Sci-Hub, LibGen, UbuWeb und AAARG  

<https://sci-hub.se/>

<https://scholar.google.de/>

## IT - Books

~~<https://b-ok.cc/>~~

~~<https://z-lib.org/>~~

~~<https://www.ebooks777.net/>~~

~~<https://dlfeb.com/>~~

~~<http://www.allitebooks.org/>~~

## Books

<https://www.pdfdrive.com/> 

<https://librarygenesis.net/> 

~~<http://en.bookfi.net/>~~

~~<https://dlfeb.com/>~~

~~<https://libgen.pw/>~~

<https://en.booksee.org/>

## Audio / Video 

<https://uu.canna.to/>

## Rheinwerk open books

<https://www.rheinwerk-verlag.de/openbook/>

<http://openbook.rheinwerk-verlag.de/it_handbuch/index.html>

<http://openbook.rheinwerk-verlag.de/python/>

## audiobooks

<http://www.audiobookreviews.com/>

Key: !cHzM6YY3JU3b65OzxecnmA!P3R21Yba

## Share Logins 

<http://bugmenot.com/>

## Web IDE 

<https://repl.it/>

<https://www.onlinegdb.com/>

<https://www.onlinegdb.com/online_java_compiler>

## Interesting web technologies

Message your customers, they'll love you for it.
Monitor and chat with the visitors on your website, mobile app or from a free customizable page.

<https://www.tawk.to/>

## Internet Live Stats

<https://www.internetlivestats.com/>

![Internet Live Stats](../pics/2019-11-18-linklist-web-tools_image_1.png)

## statische sites generatoren stats 

<https://www.staticgen.com/>

## Web UI

<http://madebyevan.com/>

## Web Tools owasp Phoenix/Tools
he free and open software security community

<https://wiki.owasp.org/index.php/Phoenix>

## Explore Git

https://resources.oreilly.com/public

## Web Mapping 

### Overpass API mit grafischem Ergebnis

<https://overpass-turbo.eu/> 

![2019 12 09 Overpas Api Map](../pics/2019-11-18-linklist-web-tools_image_2.png)

### Beispiele

---

<code>

    {{Suchbereich="Bochum-Mitte"}}
    //[out:xml];
    // Ausgabeformat der CSV-Datei
    [out:csv(
  
             // Art des Geschäftes und Name
             shop,
             name,
  
             // Informationen zur Adresse  
             "addr:street",
             "addr:housenumber",
  
         
             // öffnungszeiten 
             opening_hours,
  
             // Infos zur Kontaktaufnahme
             // traditionelles Tagging
             website,
         
             // Infos zur Kontaktaufnahme
             // alternatives Tagging
             "contact:website"
  
             ;
             yes;
             "|"
            )
    ];

    area[name={{Suchbereich}}]->.searchArea;



    (

      node[shop]
          (area.searchArea);
  
      way[shop]
         (area.searchArea);
  
      relation[shop]
              (area.searchArea);
  
    );


    out meta center;

    /*
    >;
    out meta qt;
    */
</code>

---

<code>

    {{Suchbereich="Bochum-Mitte"}}

    //[out:xml];


    // Ausgabeformat der CSV-Datei

    [out:csv(
  
             // Art des Geschäftes und Name
             shop,
             name,
  
             // Bei Ladenketten den Betreiber und die Marke
             operator,
             brand,
  
             // Informationen zur Adresse 
             "addr:country", 
             "addr:city",
             "addr:postcode",
             "addr:street",
             "addr:housenumber",
  
             // In welcher Etage liegt der Laden
             level,
         
             // Öffnungszeiten 
             opening_hours,
  
             // Infos zur Kontaktaufnahme
             // traditionelles Tagging
             phone,
             fax,
             email,
             website,
         
             // Infos zur Kontaktaufnahme
             // alternatives Tagging
             "contact:phone",
             "contact:fax",
             "contact:email",
             "contact:website",
         
             // Informationen zur Zugänglichkeit mit Rollstühlen 
             wheelchair,
             "wheelchair:toilets",
             "wheelchair:description",
  
             // Meta-Informationen von OSM
             // Knoten, Weg oder Relation
             // Individueller OSM-Schlüssel
             // Wer hat wann zuletzt daran gearbeitet
             // Geokoordinaten
             ::type,
             ::id,
             ::version,
             ::timestamp,
             ::uid,
             ::user,
             ::lat,
             ::lon
  
             ;
             yes;
             "|"
            )
    ];

    area[name={{Suchbereich}}]->.searchArea;



    (

      node[shop]
          (area.searchArea);
  
      way[shop]
         (area.searchArea);
  
      relation[shop]
              (area.searchArea);
  
    );


    out meta center;

    /*
    >;
    out meta qt;
    */
</code>

---

![2019 12 09 Overpass Beispiel Laden Daten Csv Export](../pics/2019-11-18-linklist-web-tools_image_3.png)
