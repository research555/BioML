from scraper.pmc import ScrapePMC

try:
    pmc = ScrapePMC()
    pmc.scrape_pubs_from_db()
except Exception as e:
    print(e)
    pass



