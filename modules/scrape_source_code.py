"""
File dedicated to the extraction and manipulation of the source code.
"""
from .helpers import create_dir


def scrape_code(driver):
    code_lines = driver.find_elements_by_xpath('//*[@id="code"]/div[2]/div/div[3]/div')
    return code_lines


def get_extension(language):
    #Receives the language name and return the extension.
    extensions = {'C++17': '.cpp',
                  'Python 3.9': '.py',
                  'Go': '.go',
                  'C++': '.cpp'}
    return extensions.get(language)

def get_language_name(extension):
    #Receives the language extension and return the formal name.
    languages = {
        '.cpp': 'C++',
        '.py': 'Python',
        '.go': 'Golang'
    }
    return languages.get(extension)

def write_to_file(elements, exec_id, language):
    src_folder = 'URI-Source-Codes/'
    extension = get_extension(language)
    formal_language_name = get_language_name(extension)

    lang_dir = create_dir(src_folder + formal_language_name)

    with open(lang_dir + exec_id + extension, 'w') as f:
        for element in elements:
            f.write(element.text + '\n')
