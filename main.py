from time import sleep

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options

from modules.helpers import get_max_pages_num, create_dir
from modules.login import login
from modules.scrape_answers import scrape_answers
from modules.scrape_source_code import scrape_code, write_to_file

chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(options=chrome_options)

submission_url = 'https://www.urionlinejudge.com.br/judge/pt/runs/code/'

login(driver)
create_dir('URI-Source-Codes')

total_pages = get_max_pages_num(driver)

for cur_page in range(1, total_pages + 1):
    submissions_ids, exec_ids, language_extensions = scrape_answers(driver, cur_page)

    for i in range(len(submissions_ids)):

        try:
            driver.get(submission_url + submissions_ids[i])
            code_lines = scrape_code(driver)
            write_to_file(code_lines, exec_ids[i], language_extensions[i])
        except StaleElementReferenceException:
            driver.get(submission_url + submissions_ids[i])
            sleep(1)
            code_lines = scrape_code(driver)
            sleep(1)
            write_to_file(code_lines, exec_ids[i], language_extensions[i])
        except IndexError:
            print('All the source codes were downloaded.')
            driver.quit()
            break
