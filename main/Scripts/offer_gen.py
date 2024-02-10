from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time
import os
import shutil
import ctypes
from main.Static.HTML import (TextFields, CheckBoxes, Buttons)
from main.Scripts import write_offer_v2
from main.Static import settings



pdf_text_fields = TextFields()
pdf_box_fields = CheckBoxes()
na = "N/A"
checked = "/On"

time.sleep(4)

def create_offer(doc_name, address, seller_name,
                buyer_name, price, lot, block,
                closing_date, title_company, legal_description,
                title_company_address,
                earnest_money, option_money, city, zip_code,
                subdivision, county, escrow_agent, option_days, trec_path):


                
    contract_concerning = f'{address}, {city}, TX {zip_code}'

    

    lbp_check_box = checked

    hoa_no_check_box = checked
    hoa_yes_check_box = ""

    pdf_data_dict = {
            #1st Page
            pdf_text_fields.seller: seller_name,
            pdf_text_fields.buyer: buyer_name,
            pdf_text_fields.lot: str(lot),
            pdf_text_fields.block: str(block),
            pdf_text_fields.subdivision: subdivision,
            pdf_text_fields.city: city,
            pdf_text_fields.county: county,
            pdf_text_fields.address: f"{address}, {zip_code}",
            pdf_text_fields.exclusions: na,
            pdf_text_fields.cash_portion: str(price),
            pdf_text_fields.finance_portion: na,
            pdf_text_fields.total_price: str(price),

            #2nd Page
            pdf_text_fields.prop_add1: contract_concerning,
            pdf_text_fields.escrow_agent: escrow_agent,
            pdf_text_fields.title_address: title_company_address,
            pdf_text_fields.em: earnest_money,
            pdf_text_fields.add_em_days: na,
            pdf_text_fields.om: option_money,
            pdf_text_fields.option_days: option_days,
            pdf_box_fields.buyer_pay_title_policy: checked,
            pdf_text_fields.title_company_name: title_company,
            pdf_box_fields.no_amend_or_del: checked,

            #3rd Page
            pdf_text_fields.prop_add2: contract_concerning,
            pdf_box_fields.buyer_pay_survey: checked,
            pdf_text_fields.survey_days: "5",
            pdf_text_fields.objections: "Single-Family",
            pdf_text_fields.objection_days: "3",
            pdf_box_fields.yes_hoa: hoa_yes_check_box,
            pdf_box_fields.no_hoa: hoa_no_check_box,

            #4th Page
            pdf_text_fields.prop_add3: contract_concerning,
            pdf_text_fields.req_notices: na,
            pdf_box_fields.seller_disclosure: checked,
            pdf_text_fields.sd_days: "5",

            #5th Page
            pdf_text_fields.prop_add4: contract_concerning,
            pdf_box_fields.as_is: checked,
            pdf_text_fields.service_contract: na,
            pdf_text_fields.broker_discolsure: na,
            pdf_text_fields.closing_date: str(closing_date),

            #6th Page
            pdf_text_fields.prop_add5: contract_concerning,
            pdf_text_fields.service_contract: na,
            pdf_box_fields.buyer_poss: checked,
            pdf_text_fields.special_prov1: legal_description,
            pdf_text_fields.special_prov2: 'Buyers agrees to pay all standard closing cost, excluding due taxes, liens, and brokerage fees',
            pdf_text_fields.special_prov3: 'Option period to begin day after contract lockbox placed on property and code given to buyer',
            pdf_text_fields.other_exp: na,   

            #7th Page
            pdf_text_fields.prop_add6: contract_concerning,

            #8th Page
            pdf_text_fields.prop_add7: contract_concerning,
            pdf_box_fields.lbp_addendum: lbp_check_box,
            pdf_box_fields.hoa_addendum: hoa_yes_check_box,
            pdf_text_fields.buy_email: "charles@cornerstonehomesolutions.com",

            #9th Page
            pdf_text_fields.prop_add8: contract_concerning,

            #10th Page
            pdf_text_fields.prop_add9: contract_concerning,

            #11th Page
            pdf_text_fields.prop_add10: contract_concerning,
            }
    
    offer_folder = settings.contract_save_path

    output_pdf_path = os.path.join(offer_folder, f"{doc_name}.pdf")

    save_successsful = write_offer_v2.fill_pdf(input_pdf_path=trec_path,
                                        output_pdf_path=output_pdf_path,
                                        pdf_data_dict=pdf_data_dict)
    if save_successsful:
        print ("Save good")

