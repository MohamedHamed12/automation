from selenium import webdriver
from selenium.webdriver.common.by import By  # Import the By module
from contextlib import contextmanager

@contextmanager
def create_webdriver(*args, **kwargs):
    options = webdriver.FirefoxOptions()
    options.set_preference("webdriver.gecko.driver", "/usr/bin/geckodriver")  # Set the path to GeckoDriver here
    driver = webdriver.Firefox(options=options, *args, **kwargs)
    try:
        yield driver
    finally:
        driver.quit()

# Usage of the context manager
with create_webdriver() as driver:
    driver.get("https://codeforces.com/contests")
    driver.implicitly_wait(10)
    datatable_div = driver.find_element(By.CSS_SELECTOR, "div.datatable")  # Use the By.CSS_SELECTOR locator
    print(datatable_div.text)
