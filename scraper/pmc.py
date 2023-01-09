from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from sql.sql import SQL
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

class ScrapePMC():

    def __init__(self):
        self.driver = webdriver.Edge()
        self.sql = SQL()
        load_dotenv()

    def scrape_links(self, url):
        # get the url
        self.driver.get(url)
        time.sleep(20)

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
        exc = 'SELECT title, link FROM article_links WHERE mined = 0 LIMIT 20000'
        self.sql.cursor.execute(exc)
        result = self.sql.cursor.fetchall()  # fetch links and titles from db

        for index, (title, url) in enumerate(result):
            start = datetime.now()
            self.driver.get(url)
            paragraphs = [paragraph.text for paragraph in self.driver.find_elements(By.CLASS_NAME, 'p')]
            if len(paragraphs) == 0:
                return
            with open(rf'{os.getenv("PUB_TXT_PATH")}/pub{index}.txt', mode='w', encoding='utf-8') as f:
                f.write(f'{title}\n\n')
                for paragraph in paragraphs:
                    f.write(f'{paragraph}\n\n')
                exc = 'UPDATE article_links SET mined = 1 WHERE link = %s'
                self.sql.cursor.execute(exc, (url,))
                self.sql.mydb.commit()

            end = datetime.now()
            print(f'number of paragraphs: {len(paragraphs)}')
            print(f'Elapsed time: {end - start}')
            print(f'publication {index} out of 20,000 has been mined.')
            print(f' Remaining time in seconds is: {(end - start) * (20000 - index)}')
            print('-------------------------------------------------------------------')
            time.sleep(3)

