# Instagram-Crawler
Liest nach Anmeldung Benutzerkonten aus
<br><a href="https://implod3.github.io/Instagram-Crawler" target="_blank"> View Github Page </a>

## Voraussetzungen

Der Crawler benötigt...
<ul>
				
				<li> einen normalen Instagram Account </li>
				<li> Google Chrome </li>
				<li> den dazu passenden <a href="https://chromedriver.chromium.org/downloads" target="_blank">Google Chrome Treiber</a> </li>
				<li> das Python Paket Selemium </li>
				
			</ul>

## Installation und Verwendung 

<p> Die Verwendung des Instagram-Crawler ist ziemlich simpel: </p>
				
				<ul>
					
					<li> Kopiere die Datei 'instagram-crawler.py' und den passenden <a href="https://chromedriver.chromium.org/downloads" target="_blank">Google Chrome Treiber</a> in ein beliebiges Verzeichnis </li>
					<li> Erstelle wie folgt ein Objekt und rufe danach die Funktion 'get_post()' auf </li>
					
				</ul>
				
					<code> c = crawl('USERNAME', 'PASSWORD', 'https://www.instagram.com/ACCOUNTNAME') </code>
					<code> c.get_post() </code>
					
				<p> Danach werden alle Beiträge und Storys in ein mit dem Usernamen erstelltes Verzeichnis kopiert </p>