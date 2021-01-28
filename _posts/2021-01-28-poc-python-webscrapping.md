---
layout: post
title: Pyhon Selenium Data scapping from complex website (Arcgis + iframe+ emberjs)
categories: [Python, Web, Scapping ]
tags: [Python, Web, Scapping, Selenium ]
--- 
Pyhon Selenium Data scapping from complex website (Arcgis + iframe+ emberjs)
<figure class="video_container">
  <video width="320" height="240" controls="true" allowfullscreen="true" poster="/pic/2021-01-28-screenshot-scapping-live-sendkeys.png">
    <source src="/mov/2021-01-28 13-24-07-python-selenium-WebScrapping.mp4" type="video/mp4">
  </video>
</figure>
# Python Web Scapping 

Pyhon Selenium Data scapping from complex website (Arcgis + iframe+ emberjs)


<!-- blank line -->
<figure class="video_container">
  <video width="640" controls="true" allowfullscreen="true" poster="/pic/2021-01-28-screenshot-scapping-live-sendkeys.png"> 
    <source src="/mov/2021-01-28 13-24-07-python-selenium-WebScrapping.mp4" type="video/mp4">
  </video>
</figure>
<!-- blank line -->


```python 
# pip install selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec



# Driver initialisieren und mit Dashboard-Link füttern
# driver = webdriver.Chrome("C:/Pfad/Zum/Chrome/Webdriver /chromedriver.exe")
driver = webdriver.Chrome(r"C:\down\chromedriver88_win32\chromedriver.exe")
dashboard_link = "https://experience.arcgis.com/experience/478220a4c454480e823b17327b2bf1d4"
driver.get(dashboard_link)

# Zu iFrame wechseln
WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.ID, "ifrSafe")))
driver.switch_to.frame(driver.find_element_by_id("ifrSafe"))

# Inzidenzwert für Deutschlan holen
WebDriverWait(driver, 20).until(ec.text_to_be_present_in_element((By.CSS_SELECTOR, "text"), "7-Tage-Inzidenz"))
text_elemente = driver.find_elements_by_tag_name("text")

text_werte = []
for x in range(len(text_elemente)):
    text_werte.append(text_elemente[x].text)

sieben_tage_inzidenz_de_index = text_werte.index("7-Tage-Inzidenz")
sieben_tage_inzidenz_de = text_werte[sieben_tage_inzidenz_de_index + 1]

# Werte für die Region Hannover holen
'''
<div role="button" title="Suchen" class="searchBtn searchSubmit" tabindex="0" data-dojo-attach-point="submitNode">
      <span aria-hidden="true" role="presentation" class="searchIcon esri-icon-search"></span>
      <span class="searchButtonText">Suchen</span>
    </div>
'''
WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[class='searchBtn searchSubmit']")))
driver.find_element_by_css_selector("div[class='searchBtn searchSubmit']").click()
region = "Region Hannover"
region = "Dortmund"

# driver.find_element_by_css_selector("input[title='Landkreis suchen']").send_keys("Region Hannover")
'''
<input maxlength="128" autocomplete="off" type="text" tabindex="0" 
class="searchInput" value="" aria-haspopup="true" id="esri_dijit_Search_0_input" 
data-dojo-attach-point="inputNode" role="textbox" placeholder="Landkreis suchen" 
title="Landkreis suchen">
'''
driver.find_element_by_css_selector("input[title='Landkreis suchen']").send_keys(region)

WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[class='searchMenu suggestionsMenu'] > div > ul > li")))
driver.find_element_by_css_selector("div[class='searchMenu suggestionsMenu'] > div >  ul > li").click()

WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div[class='feature-description ember-view'] > table")))
hannover_elemente = driver.find_element_by_css_selector("div[class='feature-description ember-view'] > table").find_elements_by_tag_name("td")

# Hannover Werte in Liste und Dictionary formatieren
liste_hannover_werte = []
for x in range(len(hannover_elemente)):
    liste_hannover_werte.append(hannover_elemente[x].text)
liste_hannover_werte = [einträge.replace("EW", "Einwohner") for einträge in liste_hannover_werte]

dict_hannover_werte = dict(zip(liste_hannover_werte[::2], liste_hannover_werte[1::2]))

einträge_löschen_liste = ["Einwohnerzahl", "Bundesland"]
for k in einträge_löschen_liste:
    dict_hannover_werte.pop(k, None)

# Landkreise nach Fallzahl
WebDriverWait(driver, 20).until(ec.presence_of_element_located((By.CSS_SELECTOR, "nav[class='feature-list'] > span")))
landkreise_nach_inzidenz_elemente = driver.find_elements_by_css_selector("nav[class='feature-list'] > span")

erste_fünf_landkreise_nach_inzidenz_liste = []
for x in range(5):
    erste_fünf_landkreise_nach_inzidenz_liste.append(landkreise_nach_inzidenz_elemente[x].text)

# Ausgabe
print("=======Daten für Deutschland=======\n")
print("7-Tage-Inzidenz: " + sieben_tage_inzidenz_de + "\n")
print("Die Landkreise mit der höchsten Inzidenz:\n"
      "7-Tage-Inzidenz | 7-Tage-Fallzahl | Landkreis")
for x in range(5):
    print(erste_fünf_landkreise_nach_inzidenz_liste[x])
print("\n===Daten für ", region, "===\n")
for x, y in dict_hannover_werte.items():
    print(x + ": " + y)

driver.close()




```

# Links:

Selenium Dokumentation

<https://www.selenium.dev/documentation/en/>

Heise Artikel 

<https://www.heise.de/ratgeber/Mit-Python-und-Selenium-Corona-Daten-vom-RKI-Dashboard-scrapen-5032291.html>

Beispiel Selenium 

<https://www.guru99.com/selenium-python.html>

WebDriver Links 

<https://www.selenium.dev/documentation/en/webdriver/driver_requirements/>