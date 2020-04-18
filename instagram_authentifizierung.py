from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from win32com.client import Dispatch
import requests
import os

class crawl:
    """ Get every Post from a Instagram Account """

    def __init__(self, username, password, account):
        # Speichert Benutezrdaten
        
        self.username = username
        self.password = password
        self.account = account




    def get_post(self):
        # "Run" Function
        
        # Erstellt eine Chrome Session
        self.create_chrome_session()
        self.login()
        self.get_site()
        self.get_posts()
    
    
    
    
    def get_version_via_com(self, filename):
        # Holt die Google Chrome Version
        
        parser = Dispatch("Scripting.FileSystemObject")
        try:
            version = parser.GetFileVersion(filename)
        except Exception:
            return None
        return version
    
    
    
    
    def get_chrome_version(self):
        # Filtert die Google Chrome Version
        
        if __name__ == "__main__":
            paths = [r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                     r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
            version = list(filter(None, [c.get_version_via_com(p) for p in paths]))[0]
        return version
    
    
    
    
    def create_chrome_session(self):
        # Erstellt Chrome Session
        
        # Window ist disabled
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("disable-gpu")
        options.add_argument("--log-level=3")
        
        try:
            # Versucht, Chrome Session zu erstellen
            print("Chrome Sitzung wird geöffnet...")
            self.browser = webdriver.Chrome('chromedriver.exe', options=options)
            self.browser_sec = webdriver.Chrome('chromedriver.exe', options=options)
        except:
            # Wenn dies fehlschlägt, gib Info aus
            version = self.get_chrome_version()
            print("\n######################################################")
            print("#")
            print("# Der Google Chrome Treiber wurde nicht gefunden...\n# Downloade den passenden Treiber und verschiebe ihn mit dem Namen 'chromedriver.exe' in das aktuelle Verzeichnis")
            print("#")
            print("# Google Chrome Version: ", version)
            print("# Link: https://chromedriver.chromium.org/downloads")
            print("#")
            print("######################################################")
            quit()
    
    
    
    
    def login(self):
        # Login Versuch
        
        print('Login wird versucht...')
        
        # Holt Anmeldeformular
        self.browser.get('https://www.instagram.com/accounts/login/')
        
        sleep(1)
        
        # Füllt Felder aus
        self.browser.find_element_by_name('username').send_keys(self.username)
        self.browser.find_element_by_name('password').send_keys(self.password)
        self.browser.find_element_by_name('password').send_keys(Keys.ENTER)
        
        # Solange kein Ergebnis da ist
        erg = 0
        
        while erg == 0:
            # Prüfe, ob Fehler angezeigt wird
            erg = self.get_login_error()
            if erg == 0:
                # Wenn nein, prüfe ob Benutzer eingeloggt wurde
                erg = self.get_login_succ()
        
        # Wenn erg auf 1 gesetzt wurde, war der Anmeldevorgang fehlerhaft
        if erg == 1:
            print('Benutzername oder Passwort waren falsch...')
            quit()
            
        print("Anmeldung erfolgreich")
    
    
    
    
    def get_login_error(self):
        # Prüft, ob Fehler beim Anmelden angezeigt wird
    
        try:
            self.browser.find_element_by_xpath("(//p[@id='slfErrorAlert'])")
            # Wenn ja, gib 1 zurück
            return 1
        except:
            return 0
    
    
    
    
    def get_login_succ(self):
        # Prüft, ob Homescreen gezeigt wird
        
        try:
            self.browser.find_element_by_xpath("(//div[@class='_47KiJ'])")
            # Wenn ja, gib 2 zurück
            return 2
        except:
            return 0
    
    
    
    
    def get_site(self):
        # Prüft, ob angeforderte Seite existiert
    
        try:
            print("'", self.account, "' wird gesucht...")
            self.browser.get(self.account)
            self.browser.find_element_by_xpath("(//span[@class='g47SY '])").get_attribute('innerHTML')
        except:
            print("\nEs scheint so, als ob '", self.account, "' keine gültige Instagram-Adresse sei\nBitte verwende folgenden Pattern: https://instagram.com/USERNAME")




    def get_posts(self):
        # Downloaded alle Posts
        
        # Der Name des Accounts wird gespeichert
        self.name = self.browser.find_element_by_xpath("(//h2[@class='_7UhW9       fKFbl yUEEX   KV-D4            fDxYl     '])").get_attribute('innerHTML')
        
        # Die Anzahl der Artikel
        self.articels = self.get_articels()

        # In found[] werden alle src gespeichert
        found = []
        
        # iterat sucht alle img Tags
        iterat = 1
        # i ist der Zähler
        i = 1
        
        # Ordner wird erstellt
        os.mkdir(self.name)
        
        print("\nDownload Files...\n")
       
        # Solange nicht alle Posts gedownloaded wurden
        while i != self.articels:
            
            try:
                
                # Versuche, nächsten img Tag in tag zu speichern
                tag = self.browser.find_element_by_xpath("(//div[@class='v1Nh3 kIKUG  _bz0w'])[" + str(iterat) + "]").find_element_by_tag_name("a").get_attribute('href')
                
                # Wenn dieser Tag noch nicht in found ist
                if tag not in found:
                    
                    # Speichere tag in found
                    found.append(tag)
                    
                    # Downloade Bild
                    img = self.get_def_post(self.browser.find_element_by_xpath("(//div[@class='v1Nh3 kIKUG  _bz0w'])[" + str(iterat) + "]").find_element_by_tag_name("a").get_attribute('href'))
                    
                    c = 1
                    for aC in img:
                        r = requests.get(aC[0])
                        des = self.name + "/" + str(i) + "_" + str(c) + "." + aC[1]
                        c = c + 1
                        with open(des, 'wb') as f:
                            f.write(r.content)
                    
                    # Gib Meldung aus
                    print("[", i, "/", self.articels - 1, "]")
                    
                else:
                    # Wenn tag schon in found ist soll i nicht erhöht werden, da kein img tag gefunden wurde
                    i = i - 1
                
            except:
                # Wenn kein img Tag mehr gefunden werden kann
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
        self.erg = []
        
        i = 1
        while 0 == 0:
            self.browser_sec.get(link)
            
            sleep(1)
            
            self.try_post('video')
            
            self.browser_sec.get(link)
            
            self.try_post('img')
            
            return self.erg
            break;
            
    def try_post(self, ver):
        
        iterat = 1
        if ver == 'video':
        
            while 0 == 0:
                
                try_b = 0
                try:
                    
                    # Versuche, nächsten img Tag in tag zu speichern
                    tag = self.browser_sec.find_element_by_xpath("(//video[@class='tWeCl'])[" + str(iterat) + "]").get_attribute('src')
                    
                    # Wenn dieser Tag noch nicht in found ist
                    if not any(tag in sublist for sublist in self.erg):
                        
                        # Speichere tag in found
                        self.erg.append([tag, 'mp4'])
                    
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
        
        else:
            
            while 0 == 0:
                
                try_b = 0
                try:
                    
                    # Versuche, nächsten img Tag in tag zu speichern
                    tag = self.browser_sec.find_element_by_xpath("(//img[@class='FFVAD'])[" + str(iterat) + "]").get_attribute('src')
                    
                    # Wenn dieser Tag noch nicht in found ist
                    if not any(tag in sublist for sublist in self.erg):
                        # Speichere tag in found
                        
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
        
c = crawl('USERNAME', 'PASSWORD', 'https://www.instagram.com/ACCOUNTNAME')
c.get_post()