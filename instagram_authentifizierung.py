from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class crawl:
    def __init__(self, username, password, account):
        self.username = username
        self.password = password
        self.account = account

    def get_post(self):
        self.create_chrome_session()
        self.login()
        self.get_site()
        self.get_posts()
        
    def create_chrome_session(self):
        print("Chrome Sitzung wird vorbereitet...")
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument("disable-gpu")
        options.add_argument("--log-level=3")
        
        try:
            print("Chrome Sitzung wird geöffnet...")
            self.browser = webdriver.Chrome('chromedriver.exe', options=options)
        except:
            print("\nDer Google Chrome Treiber wurde nicht gefunden...\nDownloade den zu passenden Treiber und verschiebe ihn mit dem Namen 'chromedriver.exe' in das aktuelle Verzeichnis")
            quit()
            
    def login(self):
        print('Login wird versucht...')
        self.browser.get('https://www.instagram.com/accounts/login/')
        sleep(1)
        self.browser.find_element_by_name('username').send_keys(self.username)
        self.browser.find_element_by_name('password').send_keys(self.password)
        self.browser.find_element_by_name('password').send_keys(Keys.ENTER)
        sleep(6)
        
        try:
            self.browser.find_element_by_xpath("(//div[@class='_47KiJ'])")
        except:
            print("\nBenutzername oder Passwort waren nicht korrekt...")
            quit()
            
        print('Login erfolgreich')
            
    def get_site(self):
        try:
            print("'", self.account, "' wird gesucht...")
            self.browser.get(self.account)
        except:
            print("\nEs scheint so, als ob '", self.account, "' keine gültige Instagram-Adresse sei\nBitte verwende folgenden Pattern: https://instagram.com/USERNAME")

    def get_posts(self):
        try:
            articels = self.browser.find_element_by_xpath("(//span[@class='g47SY '])").get_attribute('innerHTML')
        except:
            print("\nBenutzer wurde nicht gefunden...")
            quit()
        
        num_articels = ""

        for i in articels:
            if i != ".":
                num_articels = num_articels + i

        articels = int(num_articels) + 1

        found = []
        iterat = 1
        i = 1
        
        while i != articels:
            
            try:
                
                tag = self.browser.find_element_by_xpath("(//img[@class='FFVAD'])[" + str(iterat) + "]").get_attribute('src')
                if tag not in found:
                    
                    found.append(tag)
                    print("[", i, " /", articels - 1, "]")
                    
                else:
                    i = i - 1
                
            except:
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(3)
                iterat = 0
                i = i - 1
                
            iterat = iterat + 1
            i = i + 1
            
        counter = 0
        for k in found:
            counter = counter + 1
            print(counter, k)
            print("\n")

c = crawl('USERNAME', 'PASSWORD', 'https://instagram.com/ACCOUNTNAME')
c.get_post()
quit()