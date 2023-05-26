# Tapestry_of_Rap

## Fetch_Data
Coming soon.

## Rappad_Lyrics_Scraper: 
This Python-based project taims to scrape specific elements from a webpage on Rappad.co. The script navigates to a specified URL, waits for all JavaScript to execute, and then scrapes the words highlighted in yellow. 
- 🎯 Goal: analysis of the lyrics with the use of web scraping in Python, BeautifulSoup, and Selenium, and the scraped data.
- 📋 Output: it will create a file named 'output.txt' in the same directory

### 1. Install Selenium
```pip install selenium```

### 2. Install BeautifulSoup
```pip install beautifulsoup4```

### 3. Install webdriver_manager
```pip install webdriver_manager```

### 4. Download and Set Up ChromeDriver
Selenium requires a driver to interface with choosen browser. Download the correct version of ChromeDriver from the [official site](https://sites.google.com/a/chromium.org/chromedriver/downloads). Place the extracted 'chromedriver' file in the same directory as your Python script, and Selenium will be able to access it directly.
