# Research 

## Literature 

### Skripte 

http://www.netzmafia.de/skripten/index.html

### Paper Search 

https://sci-hub.se/

https://scholar.google.de/

## IT - Books 

http://www.allitebooks.org/

https://b-ok.cc/

## Books 

https://www.pdfdrive.com/ 

https://librarygenesis.net/ 

http://en.bookfi.net/ 

https://dlfeb.com/ (interneál server err ?!)

https://libgen.pw/ 
    
https://en.booksee.org/ 

# audiobooks 

http://www.audiobookreviews.com/

Key: !cHzM6YY3JU3b65OzxecnmA!P3R21Yba


# Share Logins 

http://bugmenot.com/

# Web IDE 

https://repl.it/

https://www.onlinegdb.com/

https://www.onlinegdb.com/online_java_compiler 



# Interesting web technologies 


Message your customers,
they'll love you for it.
Monitor and chat with the visitors on your website, mobile app or from a free customizable page.

<https://www.tawk.to/>





# Internet Live Stats 
https://www.internetlivestats.com/ 

![Internet Live Stats](pic/internetLiveStats.png)

# statische sites generatoren stats 

https://www.staticgen.com/

# Web UI 

http://madebyevan.com/

# Web Mapping 



## overpass API mit grafischem Ergebnis

https://overpass-turbo.eu/ 

![2019 12 09 Overpas Api Map](pic/2019_12_09_overpas_api_map.png)

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
  
             // Art des Gesch�ftes und Name
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
         
             // �ffnungszeiten 
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
         
             // Informationen zur Zug�nglichkeit mit Rollst�hlen 
             wheelchair,
             "wheelchair:toilets",
             "wheelchair:description",
  
             // Meta-Informationen von OSM
             // Knoten, Weg oder Relation
             // Individueller OSM-Schl�ssel
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


![2019 12 09 Overpass Beispiel Laden Daten Csv Export](pic/2019-12-09-overpass-beispiel-laden-daten-csv-export.png)