from Config import Configuration
from selenium import webdriver
import os

class SeleniumTester(object):

    def __init__(self):
        self.selenium = __import__('selenium', globals(), locals(), ['webdriver'])

    def initialize_chrome_driver(self, driver_exe_path, driver_options):
        try:
            chrome_driver = webdriver.Chrome(driver_exe_path, chrome_options=driver_options)
            return chrome_driver
        except Exception as e:
            print 'Initializing chrome driver object failed with: ' + str(e)
            pass

    def initialize_chrome_driver_options(self):
        try:
            chrome_driver_options = webdriver.ChromeOptions()
            return chrome_driver_options
        except Exception as e:
            print 'Initializing chrome driver options failed with: ' + str(e)
            pass

    def change_user_download_dir_for_chrome_driver(self, chrome_driver_options, export_dir_path):
        try:
            preferences = {'download.default_directory': str(export_dir_path)}
            chrome_driver_options.add_experimental_option('prefs', preferences)
        except Exception as e:
            print 'Chnaging download direcory for chrome driver failed with: ' + str(e)

    def get_driver_pid(self, driver):
        if driver:
            return driver.service.process.pid
        else:
            pass

    def quit_driver(self, driver):
        try:
            driver.quit()
        except Exception as e:
            print 'Terminating driver failed with: ' + str(e)

class SystemAdmin(object):

    def __init__(self):
        self.os = __import__('os')

    def kill_task_by_pid_forcefully(self, pid):
        self.os.system("taskkill /f /pid " + str(pid))





config_instance = Configuration()
export_dir = config_instance.EXPORT_DIR

driver_options = webdriver.ChromeOptions()
preferences = {'download.default_directory' : str(export_dir)}
driver_options.add_experimental_option('prefs', preferences)

# Create code driver and open Chrome
driver = webdriver.Chrome(config_instance.DRIVER_DIR_PATH, chrome_options=driver_options)

# Open EMS web page
driver.get(config_instance.DEFAULT_LINK)

# find login link to click at, and continue to login page
driver.find_element_by_link_text('Log in').click()

# select username text box element
username_box = driver.find_element_by_xpath('//*[@id="layout_ctl00_ctl00_content"]/table/tbody/tr[1]/td[2]/input')
username_box.send_keys(config_instance.USER_NAME)
# select password text box element
password_box = driver.find_element_by_xpath('//*[@id="layout_ctl00_ctl00_content"]/table/tbody/tr[2]/td[2]/input')
password_box.send_keys(config_instance.PASSWORD)
# select login button and click
driver.find_element_by_xpath('//*[@id="layout_ctl00_ctl00_content"]/table/tbody/tr[4]/td[2]/input').click()

for page_url in config_instance.LINKS_ARRAY:
    driver.get(page_url)
    element = driver.find_element_by_xpath('//*[@id="layout_ctl00_ctl00_ctl01_ctl00_a"]/div[1]/a[2]').click()
    driver.find_element_by_xpath('//*[@id="layout_ctl00_ctl00_ctl01_ctl00_a"]/div[2]/a[5]').click()
    driver.find_element_by_xpath('//*[@id="layout_ctl00_ctl00_ctl01_ctl00_a"]/div[2]/div[4]/select[2]/option[2]').click()
    driver.find_element_by_xpath('//*[@id="layout_ctl00_ctl00_ctl01_ctl00_a"]/div[2]/div[4]/a').click()
    driver.find_element_by_xpath('//*[@id="layout_ctl00_ctl00_ctl01_ctl00_a"]/div[1]/a[3]').click()


# Close driver and Chrome
os.system("taskkill /f /pid " + str(driver.service.process.pid))
driver.quit()