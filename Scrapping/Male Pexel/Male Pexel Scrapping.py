from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import requests

USER_AGENT = 'Chrome/89.0.4389.128'
path = r"C:\Users\Faizal\Documents\Pemrograman\Python\Projek1\Scrapping Selenium\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.pexels.com/id-id/pencarian/fashion%20pria/")

i = 1
for fashion in driver.find_elements_by_class_name("hide-favorite-badge"):        
    for img in fashion.find_elements_by_xpath(".//a//img[contains(@class,'img')]"):
        print(img.get_attribute("src"))
        r = requests.get(img.get_attribute("src"), stream = True, headers={'User-Agent': USER_AGENT})
        with open("Male " + str(i)+ ".jpg",'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        i = i+1
    if(i >= 5):
        break;

driver.quit()
