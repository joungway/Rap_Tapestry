import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Setup ChromeDriver
webdriver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=webdriver_service)

# specify the url
url = "https://www.rappad.co/blueprints/314836"

# make the browser navigate to the url
driver.get(url)

# get the HTML of the webpage after all JavaScript has been executed
html = driver.page_source

# create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# find all tags with the specific CSS class
yellow_words_elements = soup.select(".word.has-rhymes")

# extract and print out the words
yellow_words = [element.text for element in yellow_words_elements]
cleaned_words = [''.join(c for c in word if c not in string.punctuation) for word in yellow_words]

# open a file in write mode
with open('output.txt', 'w') as file:
    for word in cleaned_words:
        # write each word on a new line
        file.write(word + '\n')

# close the browser
driver.quit()
