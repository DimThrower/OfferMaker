from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import os
import inspect
from selenium.webdriver.firefox.options import Options
from main.Static import HTML
from main.Scripts import HTML_ACTIONS, misc
from main.Static import settings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize classes
urls = HTML.URLs()
selectors = HTML.Selectors()
innerHTML_class = HTML.InnerHTML()

def tax_scrape(address):
    try:
        chromeDriverPath = settings.chromeDrivePath
        options = Options()
        # options.binary_location = settings.chromeDrivePath

        # Keep the browser from showing by making it headless
        options.add_argument("--headless")

        # Saves on GPU process since images aren't rendered
        options.add_argument("--disable-gpu")

        # Initalize broser instance
        # browser = webdriver.Chrome(executable_path=chromeDriverPath, options=options)
        browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        browser.get(urls.har)

        # Log into HAR
        username_element = browser.find_element(
            By.CSS_SELECTOR, selectors.user)
        browser.execute_script(
            "arguments[0].value = arguments[1];", username_element, settings.HAR_USERNAME)

        password_element = browser.find_element(
            By.CSS_SELECTOR, selectors.password)
        browser.execute_script(
            "arguments[0].value = arguments[1];", password_element, settings.HAR_PASSWORD)

        # Click login btn
        HTML_ACTIONS.click(browser, wait=2, e_type='css', element=selectors.login_btn,
                errmsg=f'({inspect.currentframe().f_lineno}) - Could not click login btn')
        time.sleep(10)


        # Click Matrix
        HTML_ACTIONS.click(browser, wait=2, e_type='css', element=selectors.matrix_btn,
                errmsg=f'({inspect.currentframe().f_lineno}) - Could not click matrix')
        time.sleep(2)

        # Closing Har tab
        browser.switch_to.window(browser.window_handles[0])
        browser.close()

        # Wait for the first window to close
        while len(browser.window_handles) > 1:
            print('Waiting for login page to close')
            continue 

        # Switch back to new tab
        browser.switch_to.window(browser.window_handles[0])

        news_postpone_btn = misc.check_element_exists_BLOCK(browser, css_selector=selectors.new_postpone_btn, timeout=2)
        if news_postpone_btn:
            HTML_ACTIONS.click(browser, wait=1, e_type="css", element=selectors.new_postpone_btn, errmsg="Could not click postpone button")

        # Find the tax drop down
        tax_drp_dwn = browser.find_element(By.CSS_SELECTOR, selectors.tax_drp_dwn)

        # Make the drp down visible by changing its CSS
        browser.execute_script("arguments[0].style.display = 'block';", tax_drp_dwn)

        # Click the Realist button
        HTML_ACTIONS.click(browser, wait=0, e_type="css", element=selectors.realist_btn, errmsg=f'({inspect.currentframe().f_lineno}) - Could not click Realist')

        # Closing Matrix tab
        browser.switch_to.window(browser.window_handles[0])
        browser.close()

        # Wait for the first window to close
        while len(browser.window_handles) > 1:
            print('Waiting for login page to close')
            continue 

        # Switch back to new tab
        browser.switch_to.window(browser.window_handles[0])

        # Wait for the Realist input to appear 
        misc.check_element_exists_BLOCK(browser, css_selector=selectors.realist_address_input, timeout=10)

        HTML_ACTIONS.click(browser, wait=1, e_type="css", element=selectors.realist_address_input, errmsg=f'({inspect.currentframe().f_lineno}) - Could not click Realist Input Button')
        HTML_ACTIONS.text_input(browser, wait=10, e_type="css", element=selectors.realist_address_input, insert=address, errmsg=f'({inspect.currentframe().f_lineno}) - Could not input address')
        HTML_ACTIONS.click(browser, wait=1, e_type="css", element=selectors.realist_submit_btn, errmsg=f'({inspect.currentframe().f_lineno}) - Could not click Realist Submit Button')

        # Wait for tax page to load
        misc.check_element_exists_BLOCK(browser, css_selector=selectors.tax_dom_check, timeout=1)

        # Get the Address Title
        address_title = misc.check_element_exists_BLOCK(browser, css_selector=selectors.realist_address_header)
        inner_html_address_title = address_title.get_attribute("innerHTML")
        
        modified_address  = inner_html_address_title.split(" County")[0]

        # Split the address by commas
        address_parts = modified_address.split(', ')

        # Get the last part as the county
        county_val = address_parts[-1]

        # Find the target element in the browser using Selenium
        legal_description = misc.check_element_exists_XPATH(browser, xpath=f'//td[text()="{innerHTML_class.legal_description}"]', timeout=1, calling_line=f"{misc.line()} cannot find legal desciption")  # Modify the XPath as needed
        block = misc.check_element_exists_XPATH(browser, xpath=f"//td[text()='{innerHTML_class.block}']", timeout=1, calling_line=f"{misc.line()} cannot find block")  # Modify the XPath as needed
        lot = misc.check_element_exists_XPATH(browser, xpath=f"//td[text()='{innerHTML_class.lot}']", timeout=1, calling_line=f"{misc.line()} cannot find lot")  # Modify the XPath as needed
        owner_name = misc.check_element_exists_XPATH(browser, xpath=f"//td[text()='{innerHTML_class.owner_name}']", timeout=1, calling_line=f"{misc.line()} cannot find owners_name")  # Modify the XPath as needed
        subdivision = misc.check_element_exists_XPATH(browser, xpath=f"//td[text()='{innerHTML_class.subdivision}']", timeout=1, calling_line=f"{misc.line()} cannot find subdivision")  # Modify the XPath as needed
        zip_code = misc.check_element_exists_XPATH(browser, xpath=f"//td[text()='{innerHTML_class.zip_code}']", timeout=1, calling_line=f"{misc.line()} cannot find zip_code")  # Modify the XPath as needed
        city = misc.check_element_exists_XPATH(browser, xpath=f"//td[text()='{innerHTML_class.city}']", timeout=1, calling_line=f"{misc.line()} cannot find city")  # Modify the XPath as needed
    
        # legal_description = browser.find_element(By.XPATH, f'//td[text()="{innerHTML_class.legal_description}"]')  # Modify the XPath as needed
        # block = browser.find_element(By.XPATH, f"//td[text()='{innerHTML_class.block}']")  # Modify the XPath as needed
        # lot = browser.find_element(By.XPATH, f"//td[text()='{innerHTML_class.lot}']")  # Modify the XPath as needed
        # owner_name = browser.find_element(By.XPATH, f"//td[text()='{innerHTML_class.owner_name}']")  # Modify the XPath as needed
        # subdivision = browser.find_element(By.XPATH, f"//td[text()='{innerHTML_class.subdivision}']")  # Modify the XPath as needed
        if legal_description:
            legal_description_val = legal_description.find_element(By.XPATH, './following-sibling::td').text
        else:
            legal_description_val = "N/A"
        if block:
            block_val = block.find_element(By.XPATH, './following-sibling::td').text
        else:
            block_val = "N/A"
        if lot:
            lot_val = lot.find_element(By.XPATH, './following-sibling::td').text
        else:
            lot_val = "N/A"
        if owner_name:
            owner_name_val = misc.rearrange_name(owner_name.find_element(By.XPATH, './following-sibling::td').text)
        else:
            owner_name_val = ""

        if subdivision:
            subdivision_val = subdivision.find_element(By.XPATH, './following-sibling::td').text
        else:
            subdivision_val = ""

        if city:
            city_val = city.find_element(By.XPATH, './following-sibling::td').text
        else:
            city_val = ""

        if zip_code:
            zip_code_val = zip_code.find_element(By.XPATH, './following-sibling::td').text
        else:
            zip_code_val = ""
        
        return({'legal_description_val':legal_description_val,
                'block_val':block_val,
                'lot_val':lot_val,
                'owner_name_val':owner_name_val,
                'subdivision_val':subdivision_val,
                'zip_code':zip_code_val,
                "city":city_val,
                'county':county_val})
    finally:
        browser.quit()


