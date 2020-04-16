from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument("disable-gpu")
options.add_argument("--log-level=3")
print('Chrome Sitzung wird geöffnet...')
browser = webdriver.Chrome('chromedriver.exe', options=options)

# browser = webdriver.Chrome('chromedriver.exe')
# browser.set_window_position(-10000,0)

print('Angeforderte Seite wird geladen...')
browser.get('https://www.instagram.com/accounts/login/')

sleep(1)

browser.find_element_by_name('username').send_keys('Username')
browser.find_element_by_name('password').send_keys('Password')
browser.find_element_by_name('password').send_keys(Keys.ENTER)

print('Login abgeschlossen...')
sleep(5)

browser.get('https://www.instagram.com/best_joudlerz_')

# articels = browser.find_elements_by_xpath("(//span[@class='g47SY '])").get_attribute('innerHTML')
articels = browser.find_element_by_xpath("(//span[@class='g47SY '])").get_attribute('innerHTML')
num_articels = ""

for i in articels:
    if i != ".":
        num_articels = num_articels + i

articels = int(num_articels)

found = []

for i in range(articels):
    
    try:
        found.append(browser.find_element_by_xpath("(//img[@class='FFVAD'])[" + str(i+1) + "]"))
        print(i+1, " from", articels)
        
    except:
        print("Scroll...")
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)
    
for k in found:
    print(k.get_attribute('src'))
    print("\n")