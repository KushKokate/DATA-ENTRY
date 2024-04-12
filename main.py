from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7,fr;q=0.6'
}

response = requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=headers)
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
print(hrefs)
# USING SELENIUM TO AUTOMATE THE GOOGLE FORM FILLING PROCESS
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options = chrome_options)

for i in range(len(all_adders)):
    # Navigate to the Google Form link for each property
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfnwM7g5vA-dCBLU_-Wfg57Oc03gz-uuokkTKrLpPjIkKOzuA/viewform?usp=sf_link")

    # Find the address input field and fill it with the current address
    filling_address = driver.find_element(By.CSS_SELECTOR, 'div.AgroKb input.whsOnd')
    filling_address.send_keys(all_adders[i])

    # Find the price input field and fill it with the current price
    filling_prices = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    filling_prices.send_keys(cleaned_prices[i])

    # Find the link input field and fill it with the current link
    filling_hrefs = driver.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.o3Dpx > div:nth-child(3) > div > div > div.AgroKb > div > div.aCsJod.oJeWuf > div > div.Xb9hP > input')
    filling_hrefs.send_keys(hrefs[i])

    # Submit the form
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()


