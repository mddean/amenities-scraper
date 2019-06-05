from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
headers = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
apartments = "https://www.apartments.com/corazon-austin-tx/v59cl5f/"
response = get(apartments, headers=headers)
html_soup = BeautifulSoup(response.text, 'html.parser')
house_containers = html_soup.find_all('div', class_="js-viewAnalyticsSection")
