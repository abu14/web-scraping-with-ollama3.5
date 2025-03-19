from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import os   
import requests

# Function to scrape the website
def scrape_website(url):
    print("Launcing Chrome browser....") 
    # Launch Chrome browser
    chrome_driver_path = "./chromedriver.exe"
    #chrome options allows us to add arguments and customize the browser
    options = webdriver.ChromeOptions()
    ##options.add_argument('--headless') # headless makes for a faster scraping 
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    try:
        driver.get(url)
        print("Getting the website to load...")
        html = driver.page_source
        time.sleep(3)

        return html 
    except Exception as e:
        print(e)
    
    finally:
        driver.quit()

def exract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body = soup.body
    if body:
        return str(body)
    return "No body content found"


def clean_body_content(body_content):
    # remove html tages
    soup = BeautifulSoup(body_content, 'html.parser')

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(separator="\n")
    # get rid of extra newlines and characters 
    cleaned_content = '\n'.join(line.strip() for line in cleaned_content.splitlines() if line.strip()) # remove empty lines

    return cleaned_content


#we need to reduce the content for smaller batch for our LLM model
def split_dom_content(dom_content, max_length=1000):
    #iterate through the content and split it into smaller chunks using the max lenght parameter
    return [dom_content[i:i+max_length] for i in range(0, len(dom_content), max_length)]