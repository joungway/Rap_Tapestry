# Rap_Tapestry

# RapTapestry

This Python-based project taims to scrape specific elements from a webpage on Rappad.co. The script navigates to a specified URL, waits for all JavaScript to execute, and then scrapes the words highlighted in yellow. This project utilizes web scraping with Python, BeautifulSoup, and Selenium, and the scraped data for analysis of the lyrics.

## Installation and Setup
To run this project, you need to install a few Python libraries and tools. Run the following command in your terminal:

### Install Selenium
```pip install selenium```

### Install BeautifulSoup
```pip install beautifulsoup4```

### Install webdriver_manager
```pip install webdriver_manager```

### Download and Set Up ChromeDriver
Selenium requires a driver to interface with choosen browser. Download the correct version of ChromeDriver from the [official site](https://sites.google.com/a/chromium.org/chromedriver/downloads). Place the extracted 'chromedriver' file in the same directory as your Python script, and Selenium will be able to access it directly.
