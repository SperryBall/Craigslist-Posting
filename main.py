from craigslist import CraigslistHousing
import yaml
import webbrowser
import time
from pprint import pprint


with open('config.yaml', 'r') as f:
    CONFIG = yaml.safe_load(f)


cl_houses = CraigslistHousing(
    site=CONFIG['site'],
    # area=CONFIG['area'],
    category=CONFIG['category'],
    filters=CONFIG['filters']
)

url = site=CONFIG['url']

for url in url:
        webbrowser.open(url, new=0)

else:
    pass



current_house_postings = cl_houses.get_results(sort_by='newest', geotagged=True)

for house_listing in current_house_postings:
    pprint(house_listing)
