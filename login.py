from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class login:
    
    def login(self, browser, username, password):
        # Login Versuch
        
        self.browser = browser
        # Holt Anmeldeformular
        self.browser.get('https://www.instagram.com/accounts/login/')
        
        sleep(1)
        
        # Füllt Felder aus
        self.browser.find_element_by_name('username').send_keys(username)
        self.browser.find_element_by_name('password').send_keys(password)
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
            return 1
            
        return self.browser
        
    
    
    
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