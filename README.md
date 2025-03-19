## 🍀 **Web Scraping with Ollama 3.5**

![GitHub contributors](https://img.shields.io/github/contributors/abu14/web-scraping-with-ollama3.5)
![GitHub forks](https://img.shields.io/github/forks/abu14/web-scraping-with-ollama3.5)
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

#### **Sample Output**


### 🔧 **Code Snippets**

#### **Scraping Website Content**
> The ```scrape_website``` function uses Selenium to load the webpage and extract its HTML content.
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


#### **Cleaning DOM Content**
> The ```clean_body_content``` function removes unnecessary tags and formats the text for readability.

  ```python
  from bs4 import BeautifulSoup
  
  def clean_body_content(body_content):
      soup = BeautifulSoup(body_content, 'html.parser')
      for script_or_style in soup(["script", "style"]):
          script_or_style.extract()
      cleaned_content = soup.get_text(separator="\n")
      cleaned_content = '\n'.join(line.strip() for line in cleaned_content.splitlines() if line.strip())
      return cleaned_content
   ```

#### **Parsing with Ollama**
> The ```parse_with_ollama``` function uses Ollama 3.5 to extract specific information from the DOM content.

```python
 from langchain_ollama import OllamaLLM
 from langchain_core.prompts import ChatPromptTemplate

 #instruction to the llm model to follow when answering the prompt frm user
 template = (
    "You are tasked with extracting specific information from the following text content: {dom_content}. "
    "Please follow these instructions carefully: \n\n"
    "1. **Extract Information:** Only extract the information that directly matches the provided description: {parse_description}. "
    "2. **No Extra Content:** Do not include any additional text, comments, or explanations in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string ('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text."
 )
 
 model = OllamaLLM(model='llama3')
 
 def parse_with_ollama(dom_chunks, parse_description):
     prompt = ChatPromptTemplate.from_template(template)
     chain = prompt | model
     parse_content = []
     for chunk in dom_chunks:
         response = chain.invoke({'dom_content': chunk, 'parse_description': parse_description})
         parse_content.append(response)
     return "\n".join(parse_content)

```



### 📝 **License**

This project is licensed under the MIT License.  See [LICENSE](./LICENSE) file for more details.
  
<br>

<!-- CONTACT -->
### 💬 **Contact**

##### Abenezer Tesfaye

⭐️ Email - tesfayeabenezer64@gmail.com
 
Project Link: [Github Repo](https://github.com/abu14/web-scraping-with-ollama3.5)
