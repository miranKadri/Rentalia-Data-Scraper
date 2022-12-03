from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import csv


options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--no-sandbox')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("user-data-dir=selenium")
options.add_argument("--remote-debugging-port=9222")
options.add_argument('--disable-dev-shm-usage')

url = "https://es.rentalia.com/" 
driver = webdriver.Chrome(executable_path = "driver/chromedriver.exe", options = options)

driver.implicitly_wait(15)
driver.get(url) 

cookies = driver.find_element('xpath', '//*[@id="didomi-host"]/div/div/div/div//div[2]/button[2]')
cookies.click()

locations = ["Costa Brava", "Alicante", "Barcelona", "Madrid", "Castelldefels", "Gavà"]  

def render():
    for i in range(1,22):
        ActionChains(driver).send_keys(Keys.SPACE).perform()
    for i in range(1,192):
        ActionChains(driver).send_keys(Keys.UP).perform()

for loc in locations:
    try:
        input_field = driver.find_element('class', 'locationInput ng-pristine ng-valid ng-scope ng-isolate-scope ng-empty ng-touched')   
    except:    
        input_field = driver.find_element('xpath', '//*[@id="masterContainer"]/div/div[1]/div/form/div/div[1]/span/input')
    
    # inputing the locations from the given list 
    input_field.send_keys(loc)
    ActionChains(driver).send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
    time.sleep(3)
    # locating search button on the webpage 
    try:
        f = driver.find_element_by_xpath('//*[@id="masterContainer"]/div/div[1]/div/form/div/div[5]/button')
        print(f)
        a = ActionChains(driver)
        h = a.move_to_element(f)
        h.perform()
        h.send_keys(Keys.ENTER).perform()
    except:  
        f = ''    
    
    # desde 25€ por noche
    print(f"reached page {url}")   

    with open('data/rentalia.csv','w', encoding = 'utf-8') as f:
        wr = csv.writer(f, dialect = 'excel')
        wr.writerow(['Title','Location', 'Price per night', 'Link', 'Contact number'])
        
        while(True):
        # now extract the data from the page we reached on that website     
    
            render()

            props = driver.find_elements_by_class_name('itemContent')
            
            for a in range(0,len(props)):  
                
                prop = driver.find_elements_by_class_name('itemContent')[a] 
                # //*[@id="239697"]/div/div[2]/a/h3
                try:
                    title = prop.find_element_by_class_name('title').find_element_by_tag_name('a').find_element_by_tag_name('h3').text
                    print("title",title)
                    print('guess it worked')
                except:  
                    title = ''    
                

                try:  
                    lctn = prop.find_element_by_class_name('title').find_element_by_tag_name('a').find_element_by_tag_name('h4').text
                    print(lctn)
                except:
                    lctn = ""    

                try:
                    link = prop.find_element_by_class_name('title').find_element_by_tag_name('a').get_attribute('href')
                    print('link')
                    print(link)
                except:  
                    link = ''   

                try:
                    ppn = prop.find_element_by_class_name('price').find_element_by_tag_name('span').find_element_by_tag_name('span').text.split(' p')[0]

                except:  
                    ppn = ''    
                # prop = prop
                
                driver.get(link)
                render()
                try:
                    phn = driver.find_element_by_class_name('owner').find_element_by_class_name('editButtons').find_elements_by_tag_name('a')[0].text.split(" ")[1]
                    print(phn)
                except:
                    phn = ''    
                bklnk = driver.find_element_by_class_name('navigation').find_element_by_tag_name('a')
                bklnk.click()
                render()
                
                

                wr.writerow([title, lctn, ppn,  link, phn])

            lnk = driver.find_element_by_xpath('//*[@id="houseList"]/div[3]/div[2]/ul/li[6]/a').get_attribute('href')
            print(lnk)
            driver.get(lnk)      

                
            
                # wr.writerow([n, title, location, price, phone, link ])  
                
                # #backbutton to itemContainerPage
                # bckbtn = driver.find_element('xpath', '//*[@id="masterContainer"]/div/div[1]/div[1]/div/a').get_attribute('href')
                # driver.get(bckbtn)
                
                
            
            #  nxtpg_lnk = driver.find_element('css selector', 'button.')
            #nxtpg_lnk.click()
            
