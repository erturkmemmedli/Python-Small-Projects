import os
import requests
from bs4 import BeautifulSoup
import pdfkit
import time
from random import randint



def convert_from_html_to_pdf(website_url):
    current_directory = os.getcwd()
    response = requests.get(website_url)

    # session = requests.Session()
    # response = session.get(website_url)
    # if response.url == website_url:
    #     html_content = response.text
    # else:
    #     final_url = response.url
    #     html_content = response.text
    # session.close()

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    file_name = f'example_{randint(0,10000)}.pdf'
    output_file_path = os.path.join(current_directory, file_name)
    pdf_options = {'page-size': 'A4', 'margin-top': '5mm', 'margin-right': '5mm', 'margin-bottom': '5mm',
                   'margin-left': '5mm', 'orientation': 'Landscape', 'dpi': 300,'image-quality': 100}
    pdfkit.from_string(soup.prettify(), output_file_path, options=pdf_options, verbose=True)
