from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from sql.sql import SQL

class ScrapePMC():

    def __init__(self):
        self.driver = webdriver.Edge()
        self.sql = SQL()

    def scrape_links(self, url):
        # get the url
        self.driver.get(url)
        time.sleep(10)

        # iterate over the search results
        for i in range(871):
            # wait for the search results to load
            search_results = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".rprt"))
            )

            for index, result in enumerate(search_results, start=1):
                # get the title
                title = result.find_element(By.CSS_SELECTOR, ".title")
                # get the link to the paper
                link = title.find_element(By.TAG_NAME, 'a').get_attribute('href')

                # print the title and link
                sql = 'INSERT INTO article_links (title, link) VALUES (%s, %s)'
                self.sql.cursor.execute(sql, (title.text, link,))
                self.sql.mydb.commit()

            self.driver.find_element(By.CLASS_NAME, 'next').click()
            time.sleep(5)

        # close the browser
        self.driver.quit()

    def scrape_pubs_from_db(self):
        paragraphs = self.driver.find_elements(By.CLASS_NAME, 'p')
        for index, paragraph in enumerate(paragraphs):
            print(paragraph.text, index)

