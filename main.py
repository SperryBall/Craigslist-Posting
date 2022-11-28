from craigslist import CraigslistHousing
import yaml


with open('config.yaml', 'r') as f:
    CONFIG = yaml.safe_load(f)


cl_h = CraigslistHousing(
    site=CONFIG['site'],
    area=CONFIG['area'],
    category=CONFIG['category'],
    filters=CONFIG['filters']
)


print(cl_h.get_results_approx_count())
