from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from bs4 import BeautifulSoup
import pdfkit
import multiprocessing


def test_multiprocessing(website_url):
    current_directory = os.getcwd()
    driver = webdriver.Chrome()
    driver.get(website_url)
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    html_content = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_content, 'html.parser')
    file_name = f'example_{website_url.split("/")[-1]}.pdf'
    output_file_path = os.path.join(current_directory, file_name)
    pdf_options = {'page-size': 'A4', 'margin-top': '5mm', 'margin-right': '5mm', 'margin-bottom': '5mm',
                   'margin-left': '5mm'}
    pdfkit.from_string(soup.prettify(), output_file_path, options=pdf_options, verbose=True)


# question_links = []
# for i in range(1, 101):
#     question_links.append("https://justice.gov.az/articles/" + str(i))
#
# chunk_size = 10
# page_chunks = [question_links[i:i + chunk_size] for i in range(0, len(question_links), chunk_size)]
# num_processes = 10
#
# with multiprocessing.Pool(processes=num_processes) as pool:
#     for chunk in page_chunks:
#         pool.map(test_multiprocessing, chunk)
