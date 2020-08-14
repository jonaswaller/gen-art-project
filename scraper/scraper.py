import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os

def downloadImg(imageURL, directory):
    startTime = time.time()
    print(f"Downloading image {imageURL}")
    if not os.path.isfile(f"{directory}/{imageURL}.replay"):
        img = requests.get(imageURL)
        with open(f"{directory}/{imageURL.split('/')[-1]}","wb") as file:
            file.write(img.content)
        print(f"Downloading image {imageURL} took {time.time() - startTime} seconds")
    else:
        print(f"Image {imageURL} already exists, skipping")

driver = webdriver.Chrome() # Firefox() | Chrome()

perPage = 80 # 20 | 40 | 80
pages = 12 # any

driver.get(f"https://www.metmuseum.org/art/collection/search#!?showOnly=openAccess&material=Canvas&perPage={perPage}&offset=0&pageSize=0&sortBy=Relevance&sortOrder=asc&searchField=All") # canvas filter | perPage = 80
for i in range(pages):
    
    time.sleep(5)
    for img in driver.find_elements_by_class_name("result-card__image--art"):
        print(img.get_attribute("src"))
        downloadImg(img.get_attribute("src"),"MET960") # MET960 = Desktop folder

    driver.find_element_by_class_name("pagenav-numeric__next").click()
    time.sleep(5)

