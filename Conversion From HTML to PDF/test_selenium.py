from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from bs4 import BeautifulSoup
import pdfkit
from random import randint


def test_selenium(website_url):
    current_directory = os.getcwd()

    # Create a Selenium WebDriver
    driver = webdriver.Chrome()  # You will need to install the Chrome WebDriver

    # Open the website in the browser
    driver.get(website_url)

    # Wait for content to load (you can adjust the timeout as needed)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

    # Capture the content of the final page
    html_content = driver.page_source

    # Close the browser
    driver.quit()

    # html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    file_name = f'example_{randint(0, 10000)}.pdf'
    output_file_path = os.path.join(current_directory, file_name)
    pdf_options = {'page-size': 'A4', 'margin-top': '5mm', 'margin-right': '5mm', 'margin-bottom': '5mm',
                   'margin-left': '5mm', 'orientation': 'Landscape', 'dpi': 300, 'image-quality': 100}
    pdfkit.from_string(soup.prettify(), output_file_path, options=pdf_options, verbose=True)
