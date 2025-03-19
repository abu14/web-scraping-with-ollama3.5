## 🍀 **Web Scraping with Ollama 3.5**

![GitHub contributors](https://img.shields.io/github/contributors/abu14/web-scraping-with-ollama3.5)
![GitHub forks](https://img.shields.io/github/forks/abu14/web-scraping-with-ollama3.5)
![GitHub stars](https://img.shields.io/github/stars/abu14/wweb-scraping-with-ollama3.5)
![GitHub issues](https://img.shields.io/github/issues/abu14/web-scraping-with-ollama3.5)
![GitHub license](https://img.shields.io/github/license/abu14/web-scraping-with-ollama3.5)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/abenezer-tesfaye-191579214/)

🌟I built a web scraping tool powered by ***Selenium , BeautifulSoup , and Ollama 3.5*** . The tool extracts structured data from websites and uses an AI language model to parse and extract specific information based on user input.

> Please Note: This project is designed for educational purposes only. Web scraping might be against the terms of service agreement for some websites. Thus, ensure compliance with website terms of service when scraping.

### ✨ **Features**
  * Extracts raw HTML content from any website using ***Selenium***.
  * Cleans and processes the DOM content into a readable format.
  * Splits large DOM content into smaller chunks for efficient processing.
  * Integrates ***Ollama 3.5*** to extract specific information from the parsed content. Link [here](https://ollama.com/)
  * Built with ***Streamlit*** for an interactive user interface.


### 📦 **Requirements**
  ```
  * Python → 3.12.3
  * Streamlit → 1.28.0
  * Selenium → 4.16.0
  * BeautifulSoup4 → 4.13.3
  * Requests → 2.32.3
  * Langchain-Ollama → 0.1.0
  ```

> Additionally, download the appropriate version of [ChromeDriver](https://sites.google.com/chromium.org/driver/?spm=a2ty_o01.29997173.0.0.27d85171qiSiOl) for your system and place it in the project folder.

### ⚙️ **Usage**
Follow these steps to set up and run the project:

1. Clone the repository:
    ```bash
      git clone https://github.com/abu14/web-scraping-with-ollama3.5.git
      cd web-scraping-with-ollama3.5
    ```

2. Install dependencies:
   ```bash
    pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
    streamlit run main.py
   ```
4. Provide inputs when prompted:

    * Enter the URL of the website you want to scrape.
    * Describe what information you want to extract (e.g., product names, prices, etc.)
  
5. Results:
The app will display the extracted DOM content and parsed results based on your description.

### 🔧 **Code Snippet**
Here are some key parts of the code to help you understand how the project works:

    ```python
      from selenium import webdriver
      from selenium.webdriver.chrome.service import Service
      
      def scrape_website(url):
          print("Launching Chrome browser...")
          chrome_driver_path = "./chromedriver.exe"
          options = webdriver.ChromeOptions()
          driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
          try:
              driver.get(url)
              print("Loading the website...")
              time.sleep(3)  # Wait for the page to load
              return driver.page_source
          finally:
              driver.quit()
  
    ```




