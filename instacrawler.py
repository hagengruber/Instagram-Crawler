from time import sleep
from win32com.client import Dispatch
import os

# Import eigene Module

from chrome_session import session
from login import login
from get_site import get_site
from get_post import get_post
from get_story import get_story

class crawl:
    """ Get every Post from a Instagram Account """

    def __init__(self, username, password, account):
        # Speichert Benutezrdaten
        
        self.username = username
        self.password = password
        self.account = account

    



    def get_post(self):
        # "Run" Function
        
        # Erzeuge Session Objekte
        self.create_session()
        
        # Logt beide Sessions ein
        self.login()
        
        # Lädt Seite
        self.get_site()
        
        # Downloaded Posts
        self.get_posts()
        
        # Downloaded Storys
        self.get_story()
    
    


    
    def create_session(self):
        # Erzeugt Chrome Sessions
        
        print("Session wird vorbereitet...")
        
        # Erzeuge ein Session Objekt
        b = session()
        # Die Funktion new_session() gibt ein Session Objekt zurück
        self.browser = b.new_session()
        
        # Wenn Session nicht erzeugt wurde, gibt die Funktion new_session() 1 zurück
        # Fehlermeldung wurde bereits ausgegeben, deshalb soll nur das Script abgebrochen werden
        if self.browser == 1:
            quit()
        
        # Zweites Session Objekt wird erzeugt
        self.browser_sec = b.new_session()
    
    
    
    
    
    def login(self):
        # Logt Benutzer ein
        
        print("Login wird versucht...")
        
        # Erzeugt Login Objekt
        l = login()
        # login(...) gibt die Startseite bei erfolgreichem Login zurück
        # So übernimmt self.browser die Login-Session von Instagram
        self.browser = l.login(self.browser, self.username, self.password)
        
        # Wenn Login nicht erfolgreich war, gibt login(...) 1 zurück
        if self.browser == 1:
            quit()
        
        # Erzeugt zweites Login Objekt
        # Wenn erster Login erfolgreich war, ist keine Prüfung mehr nötig
        self.browser_sec = l.login(self.browser_sec, self.username, self.password)
        
        print("Anmeldung war erfolgreich")
    
    
    
    
    
    def get_site(self):
        # Prüft, ob Benutzer existiert und leitet Chrome Sessions weiter
        
        print(self.account, "wird gesucht...")
        
        # Site Objekt wird erzeugt
        g = get_site()
        # Wenn Benutzer nicht existiert, beinhaltet control 1
        control = g.get_site(self.browser, self.account)
        
        # Beende das Script
        if control == 1:
            quit()





    def get_posts(self):
        # Downlaoded Posts
        
        print("Download der Beiträge wird vorbereitet...")
        
        # Erzeugt Post Objekt
        g = get_post(self.browser, self.browser_sec)
        # Rufe Funktion get_post() auf
        g.get_posts()
    



    
    def get_story(self):
        # Downloaded Storys
        
        # Erzeugt Story Objekt
        g = get_story(self.browser, self.account)
        # Ruft Funktion get_story auf
        g.get_story()