from bs4 import BeautifulSoup
import selenium
import requests

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "html.parser")
# LIST OF ALL THE PRICES IN SAN-FRANSISCO
prices = soup.find_all(name='span', class_="PropertyCardWrapper__StyledPriceLine")
cleaned_prices = [price.getText().replace('+/mo', '').replace('/mo', '').replace(' 1bd', '') for price in prices]
print(cleaned_prices)
# LIST OF ALL THE ADDRESS
address = soup.find_all(name='a', class_='StyledPropertyCardDataArea-anchor')
all_adders = [addrs.getText().replace('\n\n', '').replace('\n','').strip() for addrs in address]
print(all_adders)
#LIST OF THE LINKS FOR THE PROPERTIES
links = soup.find_all('a', class_='StyledPropertyCardDataArea-anchor')

# Extract href attribute from each <a> tag
hrefs = [link.get('href') for link in links]



