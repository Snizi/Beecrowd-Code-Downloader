from modules.constants import SUBMISSIONS_LIST
from .helpers import convert_web_element
from .constants import SUBMISSIONS_LIST


def get_submissions(driver):
    return convert_web_element(driver.find_elements_by_xpath(
        '//*[@id="element"]/table/tbody/tr/td[1]'))


def get_exercise_ids(driver):
    return convert_web_element(driver.find_elements_by_xpath(
        '//*[@id="element"]/table/tbody/tr/td[3]'))


def get_language_extensions(driver):
    return convert_web_element(driver.find_elements_by_xpath(
        '//*[@id="element"]/table/tbody/tr/td[6]'))


def scrape_answers(driver, page_num):

    driver.get(SUBMISSIONS_LIST + str(page_num))
    submissions_ids = get_submissions(driver)
    exec_ids = get_exercise_ids(driver)
    language_extensions = get_language_extensions(driver)

    return submissions_ids, exec_ids, language_extensions
