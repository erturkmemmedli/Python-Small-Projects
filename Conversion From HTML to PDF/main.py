import os
import pdfkit
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Install wkhtmltopdf to be able to use pdfkit and add to PATH
# Get help from https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf
# Check `wkhtmltopdf --version` in terminal to check if it is available
# You may also need to install the Chrome WebDriver


def convert_from_html_to_pdf():
    # Get current directory
    current_directory = os.getcwd()

    i = 1
    while True:
        for path in ['questions', 'answers']:
            # Initiate output directory
            output_directory = current_directory + '/erturk/'

            # Define URL of the page you want to crawl
            website_url = "URL" + path + '/' + str(i)

            # Fetch HTML content of the page
            response = requests.get(website_url)

            # Create a Selenium WebDriver
            driver = webdriver.Chrome()

            # Open the website in the browser
            driver.get(website_url)

            # Wait for content to load (you can adjust the timeout as needed)
            wait = WebDriverWait(driver, 10)
            element = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

            # Capture the content of the final page
            html_content = driver.page_source

            # Close the browser
            driver.quit()
            if not html_content:
                break

            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')

            # Define output file path for the PDF
            if 'General Software Engineering' in html_content:
                output_directory += 'software/'
                if 'This question is banned' in html_content:
                    output_directory += 'banned/' + path
                else:
                    output_directory += 'available/' + path
            else:
                output_directory += 'others/' + path
                if not os.path.exists(output_directory):
                    os.makedirs(output_directory)

            # Define output path to save PDF file
            output_file_path = os.path.join(output_directory, f"{i}.pdf")

            # Configure pdfkit options
            pdf_options = {
                'page-size': 'A4',
                'margin-top': '5mm',
                'margin-right': '5mm',
                'margin-bottom': '5mm',
                'margin-left': '5mm',
                'orientation': 'Landscape',
                'dpi': 300,
                'image-quality': 100
            }

            # Generate the PDF from the HTML content
            pdfkit.from_string(soup.prettify(), output_file_path, options=pdf_options, verbose=True)

        # Search, crawl, and download processes are completed
        if not html_content:
            print(f"Processing {path} is completed!")
            break

        i += 1


if __name__ == '__main__':
    # webpage1 = 'https://www.geeksforgeeks.org/generate-all-possible-sorted-arrays-from-alternate-elements-of-two-given-arrays/'
    # webpage2 = 'https://hudoc.echr.coe.int/#{%22documentcollectionid2%22:[%22GRANDCHAMBER%22,%22CHAMBER%22],%22itemid%22:[%22001-226390%22]}'
    # webpage3 = 'https://hudoc.echr.coe.int/#{%22documentcollectionid2%22:[%22GRANDCHAMBER%22,%22CHAMBER%22],%22itemid%22:[%22001-225882%22]}'
    # webpage4 = 'https://hudoc.echr.coe.int/#{%22documentcollectionid2%22:[%22GRANDCHAMBER%22,%22CHAMBER%22],%22itemid%22:[%22001-225807%22]}'

    convert_from_html_to_pdf()
