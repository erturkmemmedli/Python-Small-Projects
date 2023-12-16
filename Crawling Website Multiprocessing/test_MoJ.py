import os
import requests
from bs4 import BeautifulSoup
import pdfkit



def convert_from_html_to_pdf():
    current_directory = os.getcwd()
    i = 1

    while i <= 15:
        for path in ['articles', 'news']:
            output_directory = current_directory + '/erturk/'
            website_url = "https://justice.gov.az/" + path + '/' + str(i)
            response = requests.get(website_url)
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            if 'Tələbə Qəbulu' in html_content:
                output_directory += 'software/'
                if 'Müsabiqə Komissiyası' in html_content:
                    output_directory += 'banned/' + path
                else:
                    output_directory += 'available/' + path
            else:
                output_directory += 'others/' + path
            if not os.path.exists(output_directory):
                os.makedirs(output_directory)
            output_file_path = os.path.join(output_directory, f"{i}.pdf")

            pdf_options = {'page-size': 'A4', 'margin-top': '5mm', 'margin-right': '5mm',
                           'margin-bottom': '5mm', 'margin-left': '5mm', 'orientation': 'Landscape',
                           'dpi': 300, 'image-quality': 100}

            pdfkit.from_string(soup.prettify(), output_file_path, options=pdf_options, verbose=True)

        i += 1
