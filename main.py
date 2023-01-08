from scraper.pmc import ScrapePMC

url = r'https://www.ncbi.nlm.nih.gov/pmc?term=(%22gastrointestinal+microbiome%22%5BMeSH+Terms%5D+OR+(%22gastrointestinal%22%5BAll+Fields%5D+AND+%22microbiome%22%5BAll+Fields%5D)+OR+%22gastrointestinal+microbiome%22%5BAll+Fields%5D+OR+(%22gut%22%5BAll+Fields%5D+AND+%22microbiome%22%5BAll+Fields%5D)+OR+%22gut+microbiome%22%5BAll+Fields%5D)+AND+%22open+access%22%5Bfilter%5D+AND+(%22open+access%22%5Bfilter%5D)&cmd=DetailsSearch&log$=activity'
pmc = ScrapePMC()
current_page = 435
pmc.scrape_links(url=url)
