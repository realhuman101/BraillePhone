from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def WebBrowsing(text : str):
    # Create a new Chrome browser instance
    url = "https://www.google.com/?safe=active&ssui=on"
    browser = webdriver.Chrome() # Browser might change 
    browser.get(url)

    # Find the search input element and enter the search query
    search_input = browser.find_element_by_name("q")
    search_input.send_keys(text)
    search_input.submit()

    # Wait for the search results page to load
    time.sleep(3)

    # Get the search results
    search_results = browser.find_elements_by_css_selector("div.g")

    # Print the search results
    for result in search_results:
        title = result.find_element_by_tag_name("h3").text
        link = result.find_element_by_tag_name("a").get_attribute("href")
        print(f"Title: {title}")
        print(f"Link: {link}")
        print()

    # Close the browser
    browser.quit()