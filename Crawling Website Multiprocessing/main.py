import os
import pdfkit
import multiprocessing
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def convert_from_html_to_pdf(website_url):
    current_directory = os.getcwd()
    output_directory = current_directory + '/erturk/'
    path = 'questions' if 'questions' in website_url else 'answers'

    driver = webdriver.Chrome()
    driver.get(website_url)
    wait = WebDriverWait(driver, 15)
    element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    html_content = driver.page_source
    driver.quit()
    soup = BeautifulSoup(html_content, 'html.parser')

    if 'General Software Engineering' in html_content:
        output_directory += 'software/'
        if 'This question is banned' in html_content: output_directory += 'banned/' + path
        else: output_directory += 'available/' + path
    else:
        output_directory += 'others/' + path
        if not os.path.exists(output_directory): os.makedirs(output_directory)

    file_name = f"{website_url.split('/')[-1]}.pdf"
    output_file_path = os.path.join(output_directory, file_name)
    op = {'page-size': 'A4', 'margin-top': '5mm', 'margin-right': '5mm', 'margin-bottom': '5mm', 'margin-left': '5mm'}
    pdfkit.from_string(soup.prettify(), output_file_path, options=op, verbose=True)


if __name__ == '__main__':
    pages = []
    for i in range(1, 5001):
        pages.append("URL/questions/" + str(i))
        pages.append("URL/answers/" + str(i))

    chunk_size = 20
    page_chunks = [pages[i:i + chunk_size] for i in range(0, len(pages), chunk_size)]

    num_processes = 500
    with multiprocessing.Pool(processes=num_processes) as pool:
        for chunk in page_chunks:
            pool.map(convert_from_html_to_pdf, chunk)
