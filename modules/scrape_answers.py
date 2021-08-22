from .helpers import convert_web_element


def get_submissions(driver):
    return convert_web_element(driver.find_elements_by_xpath('//*[@id="element"]/table/tbody/tr/td[1]'))


def get_exercise_ids(driver):
    return convert_web_element(driver.find_elements_by_xpath('//*[@id="element"]/table/tbody/tr/td[3]'))


def get_language_extensions(driver):
    return convert_web_element(driver.find_elements_by_xpath('//*[@id="element"]/table/tbody/tr/td[6]'))


def scrape_answers(driver, page_num):
    submissions_list = 'https://www.urionlinejudge.com.br/judge/pt/runs?answer_id=1&page='

    driver.get(submissions_list + str(page_num))
    submissions_ids = get_submissions(driver)
    exec_ids = get_exercise_ids(driver)
    language_extensions = get_language_extensions(driver)

    return submissions_ids, exec_ids, language_extensions
