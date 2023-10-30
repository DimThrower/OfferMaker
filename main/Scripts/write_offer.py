from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import os
import pyautogui
import ctypes
from selenium.webdriver.firefox.options import Options
from main.Static.HTML import TextFields, CheckBoxes, Buttons
from main.Scripts import misc
from main.Static import settings
import pygetwindow as gw

def create_offer(doc_name, address, seller_name,
                buyer_name, price, lot, block,
                closing_date, title_company, legal_description,
                title_company_address,
                earnest_money, option_money, city, zip_code,
                subdivision, county, escrow_agent, option_days,
                ):
    
    try:
        # Specify the Firefox binary location
        binary = FirefoxBinary(firefox_path=settings.firefoxDrivePath)

        # Create Firefox options
        options = Options()

        # Run browser in headless mode
        options.add_argument("--headless")

        # Create WebDriver instance
        browser = webdriver.Firefox(firefox_binary=binary, options=options)

        # Intialize TextFields, CheckBoxes, Elements, PropertyProfile classes
        text_field = TextFields()
        check_box = CheckBoxes()
        btns = Buttons()

        # Define some repetitive inputs
        initial = ''
        na = 'N/A'
        objecions_use = 'Single Family'
        sleep = 0

        # Check if the text is non
        def text_none_check(text):
            if text is None:
                return ""
            else:
                return text

    

        # Create the contract conenring input that goes at the top of the TREC page
        contract_concerning = f'{address}, {city}, TX {zip_code}'

        # Create a new window
        browser.execute_script("window.open();")

        # CLose the old window
        browser.close()

        # Switch to the new window
        browser.switch_to.window(browser.window_handles[-1])

        # Open the pdf TREC file
        browser.get(settings.blank_TREC_file_path)

        # Click previous a bunch to go back to the first page
        for _ in range(1, 12):
            browser.find_element(
                By.CSS_SELECTOR, btns.previous).click()

        # Wait for the pdf to load so elements can find all the elements
        misc.wait_until_appeared_BLOCK(
            browser=browser, css_element=text_field.seller, timeout=10)

        # Scale the page so that all the elements are visable
        browser.find_element(
            By.CSS_SELECTOR, btns.scale_dpdwn).click()
        browser.find_element(By.CSS_SELECTOR, btns.fitpage).click()

        # Find the next page button
        next_page_btn = browser.find_element(
            By.CSS_SELECTOR, btns.next)

        # First Page
        browser.find_element(By.CSS_SELECTOR, text_field.seller).send_keys(
            text_none_check(seller_name))
        browser.find_element(By.CSS_SELECTOR, text_field.buyer).send_keys(
            text_none_check(buyer_name))
        browser.find_element(By.CSS_SELECTOR, text_field.lot).send_keys(
            text_none_check(lot))
        browser.find_element(By.CSS_SELECTOR, text_field.block).send_keys(
            text_none_check(block))
        browser.find_element(By.CSS_SELECTOR, text_field.subdivision).send_keys(
            text_none_check(subdivision))
        browser.find_element(By.CSS_SELECTOR, text_field.city).send_keys(
            text_none_check(city))
        browser.find_element(By.CSS_SELECTOR, text_field.county).send_keys(
            text_none_check(county))
        browser.find_element(By.CSS_SELECTOR, text_field.address).send_keys(
            text_none_check(f'{address} {zip_code}'))
        browser.find_element(By.CSS_SELECTOR, text_field.exclusions).send_keys(
            text_none_check(na))
        browser.find_element(By.CSS_SELECTOR, text_field.cash_portion).send_keys(
            text_none_check(price))
        browser.find_element(By.CSS_SELECTOR, text_field.finance_portion).send_keys(
            text_none_check(na))
        browser.find_element(By.CSS_SELECTOR, text_field.total_price).send_keys(
            text_none_check(price))
        browser.find_element(By.CSS_SELECTOR, text_field.init_pg1).send_keys(
            text_none_check(initial))
        time.sleep(sleep)
        # Click the button to the next  page
        next_page_btn.click()
        time.sleep(sleep)

        # Second Page
        browser.find_element(By.CSS_SELECTOR, text_field.prop_add1).send_keys(
            text_none_check(contract_concerning))
        browser.find_element(By.CSS_SELECTOR, text_field.escrow_agent).send_keys(
            text_none_check(escrow_agent))
        browser.find_element(By.CSS_SELECTOR, text_field.title_address).send_keys(
            text_none_check(title_company_address))
        browser.find_element(By.CSS_SELECTOR, text_field.em).send_keys(
            text_none_check(earnest_money))
        browser.find_element(By.CSS_SELECTOR, text_field.om).send_keys(
            text_none_check(option_money))
        browser.find_element(By.CSS_SELECTOR, text_field.add_em).send_keys(
            text_none_check(na))
        browser.find_element(By.CSS_SELECTOR, text_field.add_em_days).send_keys(
            text_none_check(na))
        browser.find_element(By.CSS_SELECTOR, text_field.option_days).send_keys(
            text_none_check(option_days))
        browser.find_element(
            By.CSS_SELECTOR, check_box.buyer_pay_title_policy).click()
        browser.find_element(By.CSS_SELECTOR, text_field.title_company_name).send_keys(
            text_none_check(title_company))
        browser.find_element(
            By.CSS_SELECTOR, check_box.no_amend_or_del).click()
        browser.find_element(By.CSS_SELECTOR, text_field.init_pg2).send_keys(
            text_none_check(initial))
        time.sleep(sleep)
        # Click the button to the next  page
        next_page_btn.click()
        time.sleep(sleep)

        # Third Page
        browser.find_element(By.CSS_SELECTOR, text_field.prop_add2).send_keys(
            text_none_check(contract_concerning))
        browser.find_element(
            By.CSS_SELECTOR, check_box.buyer_pay_survey).click()
        browser.find_element(By.CSS_SELECTOR, text_field.survey_days).send_keys(
            text_none_check('5'))
        browser.find_element(By.CSS_SELECTOR, text_field.objections).send_keys(
            text_none_check(objecions_use))
        browser.find_element(By.CSS_SELECTOR, text_field.objection_days).send_keys(
            text_none_check('3'))
        # if 'yes' in prop_dict[pp.hoa]:
        #     browser.find_element(
        #         By.CSS_SELECTOR, check_box.yes_hoa).click()
        # else:
        #     browser.find_element(
        #         By.CSS_SELECTOR, check_box.no_hoa).click()

        browser.find_element(
            By.CSS_SELECTOR, check_box.no_hoa).click()
        browser.find_element(By.CSS_SELECTOR, text_field.init_pg3).send_keys(
            text_none_check(initial))
        time.sleep(sleep)
        # Click the button to the next  page
        next_page_btn.click()
        time.sleep(sleep)

        # Fourth Page
        browser.find_element(By.CSS_SELECTOR, text_field.prop_add3).send_keys(
            text_none_check(contract_concerning))
        browser.find_element(By.CSS_SELECTOR, text_field.req_notices).send_keys(
            text_none_check(na))
        browser.find_element(
            By.CSS_SELECTOR, check_box.seller_disclosure).click()
        browser.find_element(By.CSS_SELECTOR, text_field.sd_days).send_keys(
            text_none_check('5'))
        browser.find_element(By.CSS_SELECTOR, text_field.init_pg4).send_keys(
            text_none_check(initial))
        time.sleep(sleep)
        # Click the button to the next  page
        next_page_btn.click()
        time.sleep(sleep)

        # Fifth Page
        browser.find_element(By.CSS_SELECTOR, text_field.prop_add4).send_keys(
            text_none_check(contract_concerning))
        browser.find_element(
            By.CSS_SELECTOR, check_box.as_is).click()
        browser.find_element(By.CSS_SELECTOR, text_field.service_contract).send_keys(
            text_none_check(na))
        browser.find_element(By.CSS_SELECTOR, text_field.broker_discolsure).send_keys(
            text_none_check(""))#'Buyer has an active realtor license'))
        # Set the closing date
        cd = closing_date
        browser.find_element(By.CSS_SELECTOR, text_field.closing_date).send_keys(
            text_none_check(cd))
        browser.find_element(By.CSS_SELECTOR, text_field.init_pg5).send_keys(
            text_none_check(initial))
        time.sleep(sleep)
        # Click the button to the next  page
        next_page_btn.click()
        time.sleep(sleep)

        # Sixth Page
        browser.find_element(By.CSS_SELECTOR, text_field.prop_add5).send_keys(
            text_none_check(contract_concerning))
        browser.find_element(
            By.CSS_SELECTOR, check_box.buyer_poss).click()
        browser.find_element(By.CSS_SELECTOR, text_field.special_prov1).send_keys(
            text_none_check(legal_description))
        browser.find_element(By.CSS_SELECTOR, text_field.special_prov2).send_keys(
            text_none_check('Buyers agrees to pay all standard closing cost, excluding due taxes, liens, and brokerage fees'))
        browser.find_element(By.CSS_SELECTOR, text_field.special_prov3).send_keys(
            text_none_check('Option period to begin day after contract lockbox placed on property and code given to buyer'))
        browser.find_element(By.CSS_SELECTOR, text_field.other_exp).send_keys(
            text_none_check(na))
        browser.find_element(By.CSS_SELECTOR, text_field.init_pg6).send_keys(
            text_none_check(initial))
        time.sleep(sleep)
        # Click the button to the next  page
        next_page_btn.click()
        time.sleep(sleep)

        # Seventh Page
        browser.find_element(By.CSS_SELECTOR, text_field.prop_add6).send_keys(
            text_none_check(contract_concerning))
        browser.find_element(By.CSS_SELECTOR, text_field.init_pg7).send_keys(
            text_none_check(initial))
        time.sleep(sleep)
        # Click the button to the next  page
        next_page_btn.click()
        time.sleep(sleep)

        # Eighth Page
        browser.find_element(By.CSS_SELECTOR, text_field.prop_add7).send_keys(
            text_none_check(contract_concerning))
        browser.find_element(By.CSS_SELECTOR, text_field.buy_address).send_keys(
            text_none_check(""))#'2404 S Grand Blvd, Pearland, TX 77581'))
        browser.find_element(By.CSS_SELECTOR, text_field.buy_email).send_keys(
            text_none_check(""))#'info@rightwayhomesolutions.com'))
        # if 'yes' in prop_dict[pp.hoa]:
        #     browser.find_element(
        #         By.CSS_SELECTOR, check_box.hoa_addendum).click()
        # if prop_dict[pp.lead_based_paint] is not None:
        browser.find_element(
            By.CSS_SELECTOR, check_box.lbp_addendum).click()
        browser.find_element(By.CSS_SELECTOR, text_field.init_pg8).send_keys(
            text_none_check(initial))
        time.sleep(sleep)
        # Click the button to the next  page
        next_page_btn.click()
        time.sleep(sleep)

        # Ninth Page
        browser.find_element(By.CSS_SELECTOR, text_field.prop_add8).send_keys(
            text_none_check(contract_concerning))
        time.sleep(sleep)
        # Click the button to the next  page
        next_page_btn.click()
        time.sleep(sleep)

        # Temth Page
        browser.find_element(By.CSS_SELECTOR, text_field.prop_add9).send_keys(
            text_none_check(contract_concerning))
        time.sleep(sleep)
        # Click the button to the next  page
        next_page_btn.click()
        time.sleep(sleep)

        # Eleventh Page
        browser.find_element(By.CSS_SELECTOR, text_field.prop_add10).send_keys(
            text_none_check(contract_concerning))

        # Click the download button
        browser.find_element(By.CSS_SELECTOR, '#download').click()

        # Wait some time for 'Save As' window to appear
        time.sleep(5)

        # Set contract save path
        offer_folder = settings.contract_save_path



        # Generate appropriates file path, take out "/" and replace with "-"
        modified_string_filename = doc_name.replace(
            "/", "-")

        # Set path for pdf file
        file_path = f'{offer_folder}\\{modified_string_filename}.pdf'
        print(
            f"Path for file offer_folder: {offer_folder}\nmodified_string_filename: {modified_string_filename}\nfile path: {file_path}")

        start_time = time.time()
        while True:
            # Find the save as window
            windows = gw.getWindowsWithTitle('Save As')

            if len(windows) > 0:
                # Get save as window from windows
                save_as_window = windows[0]

                # Activate the save as window
                ctypes.windll.user32.SetForegroundWindow(
                    save_as_window._hWnd)

                # Make the pdf file name
                pyautogui.typewrite(file_path)
                time.sleep(1)

                # Activate the save as window
                ctypes.windll.user32.SetForegroundWindow(
                    save_as_window._hWnd)

                # Press enter on the Save as window to save pdf
                pyautogui.press('enter')

            if time.time() - start_time > 5:
                # If the time limit is reached
                # Remove the folder if it did not save
                os.remove(file_path)
                print("File deleted successfully.")
                break

            try:

                if os.path.isfile(file_path):
                    print(f'File saved: {file_path}')

                else:
                    time.sleep(1)
                    print(f'File did not save: {file_path}')

            except IndexError:
                time.sleep(1)
                print(f'File did not save: {file_path}')
                
        print(f'File Already Exist')

    finally:
        browser.quit()
