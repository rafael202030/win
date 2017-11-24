from Config import Configuration
from selenium import webdriver


config_instance = Configuration()
export_dir = config_instance.EXPORT_DIR

options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : str(export_dir)}
options.add_experimental_option('prefs', prefs)

# Create code driver and open Chrome
driver = webdriver.Chrome('C:/Users/blahova.m/Downloads/chromedriver_win32/chromedriver.exe', chrome_options=options)

# Open EMS web page
driver.get('http://www.emsbrno.cz/p.axd/en/Products.html')

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
driver.quit()
