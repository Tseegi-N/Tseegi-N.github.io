import requests

url = "https://www.bricklink.com/v2/search.page?q=star%20wars#T=M"
response = requests.get(url)
print(response)
html_content = response.content

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'your-table-class'})

data = []
headers = [th.text.strip() for th in table.find_all('th')]
data.append(headers) # Extract Headers if available

for row in table.find_all('tr')[1:]: # skip header row if available
    row_data = [td.text.strip() for td in row.find_all('td')]
    data.append(row_data)

import pandas as pd

df = pd.DataFrame(data[1:], columns=data[0]) #Create a DataFrame using the extracted data and headers
print(df)