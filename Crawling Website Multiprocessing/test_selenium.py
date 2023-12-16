from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from bs4 import BeautifulSoup
import pdfkit
from random import randint


# webpage1 = 'https://www.geeksforgeeks.org/generate-all-possible-sorted-arrays-from-alternate-elements-of-two-given-arrays/'
# webpage2 = 'https://hudoc.echr.coe.int/#{%22documentcollectionid2%22:[%22GRANDCHAMBER%22,%22CHAMBER%22],%22itemid%22:[%22001-226390%22]}'
# webpage3 = 'https://hudoc.echr.coe.int/#{%22documentcollectionid2%22:[%22GRANDCHAMBER%22,%22CHAMBER%22],%22itemid%22:[%22001-225882%22]}'
# webpage4 = 'https://hudoc.echr.coe.int/#{%22documentcollectionid2%22:[%22GRANDCHAMBER%22,%22CHAMBER%22],%22itemid%22:[%22001-225807%22]}'


def test_selenium(website_url):
    current_directory = os.getcwd()
    driver = webdriver.Chrome()
    driver.get(website_url)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    html_content = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_content, 'html.parser')
    file_name = f'example_{randint(0, 10000)}.pdf'
    output_file_path = os.path.join(current_directory, file_name)
    pdf_options = {'page-size': 'A4', 'margin-top': '5mm', 'margin-right': '5mm', 'margin-bottom': '5mm', 'margin-left': '5mm'}
    pdfkit.from_string(soup.prettify(), output_file_path, options=pdf_options, verbose=True)
