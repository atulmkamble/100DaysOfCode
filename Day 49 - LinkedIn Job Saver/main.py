"""
This program saves Data Scientist jobs in user's Linkedin profile
"""

# Import required libraries
from selenium import webdriver
from time import sleep

# Initialize global constants
LINKEDIN_EMAIL = ''  # TODO: Input your Linkedin email
LINKEDIN_PASSWORD = ''  # TODO: Input your Linkedin password
PHONE_NUMBER = ''  # TODO: Input your phone number
LINKEDIN_URL = 'https://www.linkedin.com/jobs/search/?f_L=India&f_LF=f_AL&geoId=102713980&keywords=data%20scientist' \
               '&location=India '
LINKEDIN_SAVED_JOBS_URL = 'https://www.linkedin.com/my-items/saved-jobs/'
CHROME_DRIVER_PATH = 'C:/Development/chromedriver.exe'  # TODO: Download the driver and use your path


def main():
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    driver.get(LINKEDIN_URL)
    driver.maximize_window()
    sign_in = driver.find_element_by_css_selector('.nav__button-secondary')
    sign_in.click()
    sleep(5)  # 3 seconds to load the website login page

    username = driver.find_element_by_id('username')
    username.send_keys(LINKEDIN_EMAIL)
    password = driver.find_element_by_id('password')
    password.send_keys(LINKEDIN_PASSWORD)
    submit_button = driver.find_element_by_css_selector('.login__form_action_container button')
    submit_button.click()
    sleep(5)  # 5 seconds to load the website after login

    # Get all job listings
    all_listings = driver.find_elements_by_css_selector(".jobs-search-results__list ")
    for job in all_listings:
        job_details = job.find_element_by_tag_name('li div div')
        print(job_details.text)
        print('Clicking job')
        job_details.click()
        print('Saving Job if unsaved')
        job_save = driver.find_element_by_css_selector('.jobs-save-button span')
        if job_save.text == 'Save':
            job_save.click()
        else:
            print('Already saved; skipped')
        print('Moving to next job')
        # 2 seconds delay inbetween saving jobs
        sleep(2)

    driver.get(LINKEDIN_SAVED_JOBS_URL)
    sleep(5)  # 5 seconds to load the saved jobs link

    # Quit the browser
    driver.quit()


if __name__ == '__main__':
    main()
