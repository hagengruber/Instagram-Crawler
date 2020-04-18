# Instagram-Crawler
Liest nach Anmeldung Benutzerkonten aus
<br><a href="https://implod3.github.io/Instagram-Crawler" target="_blank"> View Github Page </a>

## Voraussetzungen

Der Crawler benötigt...
<p> einen normalen Instagram Account </p>
<p> Google Chrome </p>
<p> den dazu passenden <a href="https://chromedriver.chromium.org/downloads" target="_blank">Google Chrome Treiber</a> </p>
<p> das Python Paket Selemium <p>
				
## Installation und Verwendung 

<p> Die Verwendung des Instagram-Crawler ist ziemlich simpel: </p>
				
<p> Kopiere die Datei 'instagram-crawler.py' und den passenden <a href="https://chromedriver.chromium.org/downloads" target="_blank">Google Chrome Treiber</a> in ein beliebiges Verzeichnis </p>
<p> Erstelle wie folgt ein Objekt und rufe danach die Funktion 'get_post()' auf </p>
					
<code> c = crawl('USERNAME', 'PASSWORD', 'https://www.instagram.com/ACCOUNTNAME') </code> <br>
<code> c.get_post() </code>
					
<p> Danach werden alle Beiträge und Storys in ein mit dem Usernamen erstelltes Verzeichnis kopiert </p>
