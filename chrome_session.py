from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class session:
    
    def new_session(self):
    
        # Erstellt Chrome Session
        
        # Window ist disabled
        options = webdriver.ChromeOptions()
        #options.add_argument('headless')
        #options.add_argument("disable-gpu")
        #options.add_argument("--log-level=3")
        
        try:
            # Versucht, Chrome Session zu erstellen
            self.browser = webdriver.Chrome('chromedriver.exe', options=options)
            return self.browser
            
        except:
            # Wenn dies fehlschlägt, gib Info aus
           
            print("\n######################################################")
            print("#")
            print("# Der Google Chrome Treiber wurde nicht gefunden...\n# Downloade den passenden Treiber und verschiebe ihn mit dem Namen 'chromedriver.exe' in das aktuelle Verzeichnis")
            print("#")
            print("# Link: https://chromedriver.chromium.org/downloads")
            print("#")
            print("######################################################")
            return 1