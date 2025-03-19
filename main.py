import streamlit as st
from scrape import (scrape_website, split_dom_content, clean_body_content, exract_body_content)
# from parse import parse_with_ollama

# Title for our website
st.title("Web Scraping AI🍀")



# Sidebar enhancements
with st.sidebar:
    st.title("About")
    st.write("This simple web app is a demonstration of web scraping using Streamlit, Selenium & BeautifulSoup.💪")
    
    # Components Section
    st.subheader("Components")
    st.write("Tech stacks and tools used:")
    # List with emojis as icons
    st.write("- :rocket: Streamlit - The framework powering this app")
    st.write("- :spider_web: Selenium - For browser automation and scraping")
    st.write("- :bowl_with_spoon: BeautifulSoup - For parsing HTML content")
    st.write("- :chains: Langchain - For language model integration")
    st.write("- :llama: Ollama 3.1 - The AI model assisting with parsing")


# Creates a text input box
url = st.text_input("Please enter the URL of the website you want to scrape")

if st.button('Scrape Site'):
    st.write("Scraping the site...")

    # Opens the website
    result = scrape_website(url)
    # Extracts the body content
    body_content = exract_body_content(result)
    # Cleans the body content
    cleaned_content = clean_body_content(body_content)
    # Stores the cleaned content in session state
    st.session_state.dom_content = cleaned_content

    with st.expander("Show DOM content"):
        st.text_area("DOM Content", cleaned_content, height=300)

if 'dom_content' in st.session_state:
    parse_description = st.text_area("Describe what you want out of the parse website")
    
    if st.button('Parse Content'):
        if parse_description:
            st.write("Parsing the content!🚀 Please wait...")

            # Parse the content
            dom_chunks = split_dom_content(st.session_state.dom_content)
            # result = parse_with_ollama(dom_chunks, parse_description)
            # st.write(result)
        else:
            st.warning("Please provide a description for parsing the content.")



