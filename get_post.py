from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
import os

class get_post:
    
    
    
    
    def __init__(self, browser, browser_sec):
        self.browser = browser
        self.browser_sec = browser_sec
    
    
    
    
    def get_posts(self):
        # Downloaded alle Posts
        # ToDo: Warten, bis h2 verfügbar ist
        sleep(3)
        
        try:
            
            # Der Name des Accounts wird gespeichert
            self.name = self.browser.find_element_by_xpath("(//h2[@class='_7UhW9       fKFbl yUEEX   KV-D4            fDxYl     '])").get_attribute('innerHTML')
        
        except:
        
            # Der Name des Accounts wird gespeichert
            self.name = self.browser.find_element_by_xpath("(//h1[@class='_7UhW9       fKFbl yUEEX   KV-D4            fDxYl     '])").get_attribute('innerHTML')
        
        # Die Anzahl der Abonnenten werden gespeichert
        self.follower = self.browser.find_element_by_xpath("(//span[@class='g47SY '])[2]").get_attribute('innerHTML')
        
        # Die Anzahl der Abonnierten wird gespeichert
        self.following = self.browser.find_element_by_xpath("(//span[@class='g47SY '])[3]").get_attribute('innerHTML')
        
        # Die Anzahl der Beiträge wird gespeichert
        self.articels = self.get_articels()
        
        # In found[] werden alle Links gespeichert:
        # Die Links der Bilder werden in einer zweiten Chrome Session gecrawlt
        # Um zu prüfen, ob ein Bild schon bearbeitet worden ist, werden alle Links der Bilder
        # in found gespeichert
        found = []
        
        # iterat sucht alle a Tags
        iterat = 1
        
        # i ist der Zähler
        i = 1
        
        try:
            # Ordner wird erstellt
            os.mkdir(self.name)
        except FileExistsError:
            # Wenn Ordner schon existiert
            print("Der Ordner '" + self.name + "' existiert schon...")
            answer = input("Sollen Daten gelöscht werden [J/N]? ")
            if not answer == "J":
                quit()
        
        # Solange nicht alle Posts gedownloaded wurden
        while i != self.articels:
            
            try:
                
                # Versuche, nächsten a Tag in tag zu speichern
                # Dazu hole erst div Tag und anschließend den a Tag im div Tag
                tag = self.browser.find_element_by_xpath("(//div[@class='v1Nh3 kIKUG  _bz0w'])[" + str(iterat) + "]").find_element_by_tag_name("a").get_attribute('href')
                
                # Wenn dieser Tag noch nicht in found ist
                if tag not in found:
                    
                    # Speichere tag in found
                    found.append(tag)
                    
                    # Hole alle Bilder (wenn Serienbilder)
                    # img ist ein mehrdimensionaler Array
                    img = self.get_def_post(self.browser.find_element_by_xpath("(//div[@class='v1Nh3 kIKUG  _bz0w'])[" + str(iterat) + "]").find_element_by_tag_name("a").get_attribute('href'))
                    
                    # c ist der Counter, der das Bild benennt
                    c = 1
                    # Downloaded alle Bikder
                    for aC in img:
                        # Holt im Array aC den 0 Index
                        # 0 -> Link
                        # 1 -> Typ (jpg/mp4)
                        r = requests.get(aC[0])
                        # In des wird der Name des Bildes gespeichert
                        des = self.name + "/" + str(i) + "_" + str(c) + "." + aC[1]
                        c = c + 1
                        # Bild wird gespeichert
                        with open(des, 'wb') as f:
                            f.write(r.content)
                    
                    # Consolenausgabe wird gelöscht
                    os.system("cls")
                    
                    # Gib Meldung aus
                    print("###############################################")
                    print("#                                             #")
                    print(self.p_header(self.name))
                    print("#                                             #")
                    print("# Beiträge:", self.articels-1, " " + self.follower + " Abonnenten " + self.following + " Abonniert")
                    print("#                                             #")
                    print("###############################################")
                    print("#                                             #")
                    print("# Download Success: [", i, "/", self.articels - 1, "]               #")
                    print("#                                             #")
                    
                else:
                    # Wenn tag schon in found ist soll i nicht erhöht werden, da kein div/a tag gefunden wurde
                    i = i - 1
                
            except:
                # Wenn kein div/a Tag mehr gefunden werden kann
                # Script scrollt bis bottom, da Instagram so die älteren Bilder per Ajax lädt
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(3)
                #iterat wird auf 0 gesetzt, da die Bilder von oben verschwinden können
                # So wird also wieder die erste Klasse des img Tags ermittelt
                # Wenn diese schon gefunden ist... (siehe if tag not in found)
                iterat = 0
                # i soll nicht erhöht werden, da kein img tag gefunden wurde
                i = i - 1
                
            #iterat wird erhöht
            iterat = iterat + 1
            #i wird erhöht
            i = i + 1
    
    
    
    
    def get_def_post(self, link):
    # Gibt alle Serienbilder in einem mehrdimensionalem Array zurück
    
        # Ergebnis wird in self.erg gespeichert
        self.erg = []
        
        # Serienbild wird aufgerufen
        self.browser_sec.get(link)
        
        sleep(1)
        
        # Prüft, ob Videos im Serienpost existiert
        # Wenn ja, werden dieses in self.erg gespeichert
        self.try_post('video')
        
        # Beitrag wird erneut aufgerufen
        self.browser_sec.get(link)
        
        # Prüft, ob Bilder im Serienpost existiert
        # Wenn ja, wird dieses in self.erg gespeichert
        self.try_post('img')
        
        return self.erg
    
    
    
    
    def try_post(self, ver):
    # Speichert Bilder und Videos in self.erg
        
        iterat = 1
        # Wenn nach Videos gesucht wird
        if ver == 'video':
        
            # Unendlich Schleife
            # Wird abgebrochen, sobald alle Beiträge gespeichert worden sind
            while 0 == 0:
                
                # try_b beinhaltet 1, wenn kein Beitrag mehr gefunden werden kann
                try_b = 0
                try:
                    
                    # Versuche, nächsten video Tag in tag zu speichern
                    tag = self.browser_sec.find_element_by_xpath("(//video[@class='tWeCl'])[" + str(iterat) + "]").get_attribute('src')
                    
                    # Wenn dieser Tag noch nicht in self.erg ist
                    if not any(tag in sublist for sublist in self.erg):
                        
                        # Speichere tag in self.erg
                        self.erg.append([tag, 'mp4'])
                    
                except:
                    # Wenn kein Video Tag mehr gefunden werden kann
                    try_b = 1
                    iterat = 1
                
                # Wenn kein Video Tag mehr gefunden werden kann
                if try_b == 1:
                
                    try:
                        # Verusche, Button für nächstes Bild zu klicken
                        self.browser_sec.find_element_by_xpath("(//div[@class='    coreSpriteRightChevron  '])[1]").click()
                    except:
                        # Wenn Button nicht mehr existiert, ist die Suche beendet
                        # self.erg wird zurückgegeben
                        return self.erg
                        break
                
                iterat = iterat + 1
        
        else:
            
            # Gleiches Prinzip wie oben
            self.browser_sec.execute_script('document.getElementsByClassName("Z666a")[0].innerHTML=""')
            while 0 == 0:
                
                try_b = 0
                try:
                    
                    # Versuche, nächsten img Tag in tag zu speichern
                    tag = self.browser_sec.find_element_by_xpath("(//img[@class='FFVAD'])[" + str(iterat) + "]").get_attribute('src')
                    
                    # Wenn dieser Tag noch nicht in self.erg ist
                    if not any(tag in sublist for sublist in self.erg):
                        
                        # Speichere tag in self.erg
                        self.erg.append([tag, 'jpg'])
                    
                except:
                    try_b = 1
                    iterat = 1
                
                if try_b == 1:
                    try:
                        self.browser_sec.find_element_by_xpath("(//div[@class='    coreSpriteRightChevron  '])[1]").click()
                        
                    except:
                        return self.erg
                        break
                
                iterat = iterat + 1
    
    
    
    
    def get_articels(self):
        # Die Anzahl der Artikel wird ermittelt 
        
        # In diesem Tag steht die Anzahl der Artikel
        articels = self.browser.find_element_by_xpath("(//span[@class='g47SY '])").get_attribute('innerHTML')
        
        # Wenn der User jedoch mehr als 999 Postst hat, wird folgendes zurückgegeben: 1.234
        # Der Punkt muss entfernt werden, da das Script sonst nichts mit dem String anfangen kann
        num_articels = ""

        # Entfernt . in articels
        for i in articels:
            if i != ".":
                num_articels = num_articels + i

        # Gibt Anzahl zurück
        # Anzahl wird für while schleife um 1 erhöht
        return int(num_articels) + 1
    
    
    def p_header(self, name):
        # Formatierte Ausgabe
       
        lenWidth = 29 - len(name)
        
        header = "#"
        for i in range(14):
            header = header + " "
        
        header = header + " " + name + " "
        
        for i in range(lenWidth):
            header = header + " "
        
        return header + "#"