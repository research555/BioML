from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# specify the url
url = r'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4838018/'
# create a new Chrome browser
driver = webdriver.Edge()

# get the url
driver.get(url)

paragraphs = driver.find_elements(By.CLASS_NAME, 'p')
for index, paragraph in enumerate(paragraphs):
    print(paragraph.text, index)