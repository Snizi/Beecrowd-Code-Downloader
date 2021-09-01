import os

from selenium.common.exceptions import NoSuchElementException

from .constants import SUBMISSIONS_LIST


def convert_web_element(web_element):
    """
    This function receives a web element list, iterate over it
    and then return a list, if we try to access the elements
    without setting a new list, selenium will prompt an error.
    """
    return [i.text for i in web_element]


def get_max_pages_num(driver):

    driver.get(SUBMISSIONS_LIST)
    try:
        total_pages = int(str(driver.find_element_by_xpath(
            '//*[@id="table-info"]').text).split()[2])
        return total_pages
    except NoSuchElementException:
        return None


def create_dir(directory):
    folder = directory + '/'
    if not os.path.exists(folder):
        os.mkdir(folder)
        return folder
    return folder


def read_file(file_path):
    with open(file_path) as f:
        source = f.read()
        return source
