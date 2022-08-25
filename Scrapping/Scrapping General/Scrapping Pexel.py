from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import requests

USER_AGENT = 'Chrome/89.0.4389.128'
path = r"C:\Users\Faizal\Documents\Pemrograman\Python\Projek1\Scrapping Selenium\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.pexels.com/search/fashion%20model/")

# looping kedua di setiap jenis karena di lopping pertama
# hanya bisa mengambil 30 gambar

#===========Female===========
# Female
i = 0
for fashion in driver.find_elements_by_class_name("hide-favorite-badge"):        
    for img in fashion.find_elements_by_xpath(".//a//img[contains(@class,'img')]"):
        print(img.get_attribute("src"))
        r = requests.get(img.get_attribute("src"), stream = True, headers={'User-Agent': USER_AGENT})
        with open("Female " + str(i+1)+ ".jpg",'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        i = i+1
    if(i >= 50):
        break;

# Female 2
driver.get("https://www.pexels.com/id-id/pencarian/women%20fashion/")
for fashion in driver.find_elements_by_class_name("hide-favorite-badge"):        
    for img in fashion.find_elements_by_xpath(".//a//img[contains(@class,'img')]"):
        print(img.get_attribute("src"))
        r = requests.get(img.get_attribute("src"), stream = True, headers={'User-Agent': USER_AGENT})
        with open("Female " + str(i+1)+ ".jpg",'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        i = i+1
    if(i >= 60):
        break;

#===========MALE===========

# Male
driver.get("https://www.pexels.com/id-id/pencarian/fashion%20pria/")
i = 0
for fashion in driver.find_elements_by_class_name("hide-favorite-badge"):        
    for img in fashion.find_elements_by_xpath(".//a//img[contains(@class,'img')]"):
        print(img.get_attribute("src"))
        r = requests.get(img.get_attribute("src"), stream = True, headers={'User-Agent': USER_AGENT})
        with open("Male " + str(i+1)+ ".jpg",'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        i = i+1
    if(i >= 60):
        break;

# Male 2
driver.get("https://www.pexels.com/id-id/pencarian/men%20fashion/")
for fashion in driver.find_elements_by_class_name("hide-favorite-badge"):        
    for img in fashion.find_elements_by_xpath(".//a//img[contains(@class,'img')]"):
        print(img.get_attribute("src"))
        r = requests.get(img.get_attribute("src"), stream = True, headers={'User-Agent': USER_AGENT})
        with open("Male " + str(i+1)+ ".jpg",'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        i = i+1
    if(i >= 60):
        break;

#===========KIDS===========

# Kids
driver.get("https://www.pexels.com/search/kids%20fashion/")
i = 0
for fashion in driver.find_elements_by_class_name("hide-favorite-badge"):        
    for img in fashion.find_elements_by_xpath(".//a//img[contains(@class,'img')]"):
        print(img.get_attribute("src"))
        r = requests.get(img.get_attribute("src"), stream = True, headers={'User-Agent': USER_AGENT})
        with open("Kids " + str(i+1)+ ".jpg",'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        i = i+1
    if(i >= 60):
        break;

## Kids 2
driver.get("https://www.pexels.com/search/kids%20clothes/")
for fashion in driver.find_elements_by_class_name("hide-favorite-badge"):        
    for img in fashion.find_elements_by_xpath(".//a//img[contains(@class,'img')]"):
        print(img.get_attribute("src"))
        r = requests.get(img.get_attribute("src"), stream = True, headers={'User-Agent': USER_AGENT})
        with open("Kids " + str(i+1)+ ".jpg",'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        i = i+1
    if(i >= 60):
        break;

driver.quit()