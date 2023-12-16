import os

current_directory = os.getcwd()
output_directory = current_directory + '/erturk/'


def folder_separation(output_directory, html_content, path):
    if 'General Software Engineering' in html_content:
        output_directory += 'software/'
        if 'This question is banned' in html_content:
            output_directory += 'banned/' + path
        else:
            output_directory += 'available/' + path
    else:
        output_directory += 'others/' + path
        if not os.path.exists(output_directory): os.makedirs(output_directory)
