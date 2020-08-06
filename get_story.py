from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
import os

class get_story:
    """ Download Storys """
    
    def __init__(self, browser, account):
        # Setzt Variablen
        
        self.browser = browser
        self.account = account
        
        try:
            # Name des Accounts kann entweder in h2 oder h1 Tag stehen
            
            # Der Name des Accounts wird gespeichert
            self.name = self.browser.find_element_by_xpath("(//h2[@class='_7UhW9       fKFbl yUEEX   KV-D4            fDxYl     '])").get_attribute('innerHTML')
        
        except:
        
            # Der Name des Accounts wird gespeichert
            self.name = self.browser.find_element_by_xpath("(//h1[@class='_7UhW9       fKFbl yUEEX   KV-D4            fDxYl     '])").get_attribute('innerHTML')
    
    
    
    
    def get_story(self):
        # Main function
        
        # In self.erg_storys werden alle src von img/video Tags gespeichert
        self.erg_storys = []
        # Ruft Seite von Account auf
        self.browser.get(self.account)
        
        #ToDO: Nötig..?
        sleep(3)
        
        try:
            # Wenn Storys vorhanden sind, existiert div@class...
            
            # Storys werden beim Klick geladen und angezeigt
            self.browser.find_element_by_xpath("(//div[@class='RR-M- h5uC0'])[1]").click()
        except:
            # Wenn keine Storys vorhanden sind
            print("Keine Storys vorhanden")
            quit()
        
        #ToDo: Kommentar hinzufügen
        self.browser.find_element_by_xpath("(//img[@class='_6q-tv'])[1]").click()
        
        # Funktion load_story()
        # Wartet bis Story geladen hat
        self.load_story()
        
        # stop beendet while Schleife
        stop = 0
        # Zählt Story Crawls mit
        count = 1
        
        while stop == 0:
            
            # Speichert in self.erg_storys[] die src von img/video Tag
            self.try_get_story()
            
            try:
                # Versucht, Story weiterzuklicken
                # Wenn Button nicht existiert, ist der Crawl abgeschlossen
                
                # Klickt "weiter" Button
                self.browser.find_element_by_xpath("(//div[@class='coreSpriteRightChevron'])[1]").click()
                
                print("# Crawl Story: ",count,"                             #")
                
                count += 1
                
                # Zeit für Animation, die die Story benötigt
                sleep(1)
            
            except:
                # Beendet die Schleife
                stop = 1
        
        # Downloaded die in self.erg_storys[] gespeicherten src
        # count-1 für Konsolen Ausgabe
        self.download_storys(count-1)
    
    
    
    
    
    def download_storys(self, count):
        # Downloaded src, die in self.erg_storys[] gespeichert sind
        
        print("#                                             #")
        
        # Da auch beim Beenden der Story ein "weiter" Button existiert, wird ein unnützes Bild gespeichert
        # Dies wird gelöscht...
        del self.erg_storys[-1]
        
        # Story Ordner wird erstellt
        os.mkdir(self.name + "/" + self.name + "_Storys")
        
        # Story Download Counter
        i = 1
        
        # Downloaded alle src
        for aC in self.erg_storys:
            # Holt im Array aC den 0 Index
            # 0 -> Link
            # 1 -> Typ (jpg/mp4)
            print("# Download Story: [",i,"/",count,"]                   #")
            r = requests.get(aC[0])
            # In des wird der Name des src gespeichert
            des = self.name + "/" + self.name + "_Storys/" + str(i) + "." + aC[1]
            
            # Bild wird gespeichert
            with open(des, 'wb') as f:
                f.write(r.content)
            
            i += 1
    
        print("###############################################")
    
    def load_story(self):
        # Wartet.bis Story geladen ist
        
        while 0 == 0:
            
            try:
            
                # Prüft, ob span Tag existiert
                self.browser.find_element_by_xpath("(//span[@class='Szr5J'])[1]")
                return 0
            except:
                # Wenn nicht, warte
                sleep(1)
    
    
    
    
    def try_get_story(self):
        # Speichert Storys in self.erg_storys[]
        
        while 0 == 0:
            
            found = self.story_video()
            
            if found == 1:
                break;
                
            found = self.story_img()

            if found == 1:
                break
    
    
    
    def story_video(self):
        
        try:
            self.erg_storys.append([self.browser.find_element_by_xpath("(//source)[1]").get_attribute('src'), 'mp4'])
            return 1
        except:
            return 0
    
    
    
    
    def story_img(self):
    
        try:
            self.erg_storys.append([self.browser.find_element_by_xpath("(//img)[2]").get_attribute('src'), 'jpg'])
            return 1
        except:
            return 0