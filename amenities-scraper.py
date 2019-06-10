from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# =============================================================================
# Defines a header to pass along get command.  This mimics a "more human" 
# behavior that doesn't overload site with several requests per second.  
# You will get blocked if you scrape too agressively and so, this is a nie feature.
# =============================================================================

headers = ({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})

# =============================================================================
# Copy and paste the apartments.com url of specific property below within "quotations"
# =============================================================================
corazon = "https://www.apartments.com/corazon-austin-tx/v59cl5f/"
response = get(corazon, headers=headers)

print(response)
print(response.text[:1000])

html_soup = BeautifulSoup(response.text, 'html.parser')

property_container = html_soup.find_all('div', class_="propertyNameRow clearfix")
theProperty = property_container[0]
var_1 = theProperty.find_all('h1', class_="propertyName")[0].text
print(var_1)

amenities_containers = html_soup.find_all('div', class_="js-viewAnalyticsSection")
amenities = amenities_containers[0]
for link in amenities.find_all('li'):
    print(link.get_text().replace('•',''))
