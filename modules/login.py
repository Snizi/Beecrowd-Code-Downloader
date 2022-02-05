from getpass import getpass


def login(driver):
    login_url = 'https://www.beecrowd.com.br/judge/en/login'

    email = input('Email: ')
    password = getpass('Password: ')

    driver.get(login_url)

    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_xpath(
        '//*[@id="users-form"]/form/div[5]/input').click()
