# Rappad_Lyrics_Scraper

This Python-based project taims to scrape specific elements from a webpage on Rappad.co. The script navigates to a specified URL, waits for all JavaScript to execute, and then scrapes the words highlighted in yellow. This project utilizes web scraping with Python, BeautifulSoup, and Selenium, and the scraped data for analysis of the lyrics.

## 🔧 Installation and Setup
To run this project, you need to install a few Python libraries and tools. Run the following command in your terminal:

### 1. Install Selenium
```pip install selenium```

### 2. Install BeautifulSoup
```pip install beautifulsoup4```

### 3. Install webdriver_manager
```pip install webdriver_manager```

### 4. Download and Set Up ChromeDriver
Selenium requires a driver to interface with choosen browser. Download the correct version of ChromeDriver from the [official site](https://sites.google.com/a/chromium.org/chromedriver/downloads). Place the extracted 'chromedriver' file in the same directory as your Python script, and Selenium will be able to access it directly.
