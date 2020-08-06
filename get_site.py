from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class get_site:
    # Holt angeforderte Seite
    
    def get_site(self, browser, account):
        # Prüft, ob angeforderte Seite existiert
    
        try:
            
            # Holt Account
            browser.get(account)
            browser.find_element_by_xpath("(//span[@class='g47SY '])").get_attribute('innerHTML')
            return 0
        
        except:
            print("\nEs scheint so, als ob '", account, "' keine gültige Instagram-Adresse sei\nBitte verwende folgenden Pattern: https://instagram.com/USERNAME")
            return 1