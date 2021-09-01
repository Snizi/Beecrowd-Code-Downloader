import time

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options

from modules.helpers import get_max_pages_num, create_dir
from modules.login import login
from modules.scrape_answers import scrape_answers
from modules.scrape_source_code import scrape_code, write_to_file
from modules.github_api import github
from modules.constants import SUBMISSION_URL


def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    login(driver)

    create_dir('URI-Source-Codes')

    total_pages = get_max_pages_num(driver)
    if total_pages is None:
        print("Wrong email or password")

    for cur_page in range(1, total_pages + 1):
        submissions_ids, exec_ids, language_extensions = scrape_answers(
            driver, cur_page)

        for i in range(len(submissions_ids)):

            try:
                driver.get(SUBMISSION_URL + submissions_ids[i])
                code_lines = scrape_code(driver)
                write_to_file(code_lines, exec_ids[i], language_extensions[i])
            except StaleElementReferenceException:
                driver.get(SUBMISSION_URL + submissions_ids[i])
                time.sleep(1)
                code_lines = scrape_code(driver)
                time.sleep(1)
                write_to_file(code_lines, exec_ids[i], language_extensions[i])
            except IndexError:
                print('All the source codes were downloaded.')
                driver.quit()
                upload_to_github = input(
                    "Do you want to upload the source codes to GitHub? Y/N? ")
                if upload_to_github.upper() == 'Y':
                    github()
                    print("All source codes were uploaded to GitHub =)")
                    break
                else:
                    break


if __name__ == "__main__":
    main()
