class URLs:
    har = 'https://matrix.harmls.com/Matrix/SavedSearches.aspx'

class InnerHTML:
    owner_name = "Owner Name"
    lot = "Lot #"
    block = "Block #"
    subdivision = 'Subdivision'
    legal_description = 'Legal Description'
    zip_code = "Tax Billing Zip"
    city = "Township"


    year_built = "Effective Year Built:"
    bed = 'Bedrooms:'
    bath = 'Full Baths:'
    half_bath = 'Half Baths:'
    sqft = "Building Sq Ft:"
    mud = "M.U.D. Information:"
    arv = "RealAVM:"

class Selectors:
    # Har Selectors
    user = '#username'
    password = '#password'
    login_btn = '#login_btn'
    matrix_btn = 'body > div.pageContent > div.pc_content.color_carbon > div:nth-child(2) > div.col-md-4.col-12.order-md-2.order-0 > div:nth-child(1) > a'
    first_mls_link = '#wrapperTable > td:nth-child(11) > span'
    listing_link = '#wrapperTable > div > div > div:nth-child(3) > div > span > div.mtx-containerNavTabs > ul > li:nth-child(1)'
    tax_link = '#wrapperTable > div > div > div:nth-child(3) > div > span > div.mtx-containerNavTabs > ul > li:nth-child(2)'
    next_btn = '#m_lblPagingSummary > span > a:nth-child(2)'
    current_num = '#m_lblPagingSummary > b:nth-child(2)'
    final_num = '#m_lblPagingSummary > b:nth-child(3)'
    listing_dom_check = '#wrapperTable'
    tax_dom_check = '#wrapperTable > div > div > div:nth-child(1) > div > div > div.d-borderWidthBottom--1.d-borderStyle--solid.d-bordercolor--systemDark.d-borderWidthRight--0.d-borderWidthTop--0.d-borderWidthLeft--0.d-marginTop--10.col-sm-8 > span'
    mls_id_html = '#wrapperTable > tbody > tr > td > span > table > tbody > tr:nth-child(5) > td.display.d48m10 > table > tbody > tr.d48m11 > td.d48m15 > table > tbody > tr:nth-child(3) > td.d48m27 > span'
    tax_drp_dwn = '#m_topNavList > li:nth-child(7) > ul'
    tax_dom_check = '#mat-expansion-panel-header-12 > span.mat-content.ng-tns-c92-41 > mat-panel-title'

    # Realist Selectors
    realist_btn = "#m_topNavList > li:nth-child(7) > ul > li:nth-child(1) > a"
    realist_address_input = "#cdk-accordion-child-0 > div > div > div > div > div > div > div > input"
    realist_submit_btn = "body > rlst-root > rlst-dashboard > mat-sidenav-container > mat-sidenav > div > rlst-search-panel > div.card.h-100 > div > div > rlst-quick-search > form > div.search-controls > button.btn.btn-default.btn-dark.ml-5.search-btn.btn-lg"
    realist_address_header = "body > rlst-root > rlst-reports > rlst-subheader > header > div > div > h1"
    
from selenium.webdriver.common.by import By

class Buttons:
    save = '#download'
    previous = '#previous'
    next = '#next'
    scale_dpdwn = '#scaleSelect'
    fitpage = '#pageFitOption'

class TextFields:
    seller = '#pdfjs_internal_id_1499R'
    buyer = '#pdfjs_internal_id_1500R'
    lot = '#pdfjs_internal_id_1501R'
    block = '#pdfjs_internal_id_1502R'
    subdivision = '#pdfjs_internal_id_1503R'
    city = '#pdfjs_internal_id_1504R'
    county = '#pdfjs_internal_id_1505R'
    address = '#pdfjs_internal_id_1506R'
    exclusions = '#pdfjs_internal_id_1508R'
    cash_portion = '#pdfjs_internal_id_1509R'
    finance_portion = '#pdfjs_internal_id_1514R'
    total_price = '#pdfjs_internal_id_1515R'
    escrow_agent = '#pdfjs_internal_id_282R'
    title_address = '#pdfjs_internal_id_284R'
    em = '#pdfjs_internal_id_279R'
    om = '#pdfjs_internal_id_277R'
    add_em = '#pdfjs_internal_id_278R'
    add_em_days = '#pdfjs_internal_id_283R'
    option_days = '#pdfjs_internal_id_281R'
    title_company_name = '#pdfjs_internal_id_293R'
    survey_days = '#pdfjs_internal_id_308R'
    objections = '#pdfjs_internal_id_309R'
    objection_days = '#pdfjs_internal_id_310R'
    req_notices = '#pdfjs_internal_id_326R'
    sd_days = '#pdfjs_internal_id_337R'
    service_contract = '#pdfjs_internal_id_344R'
    broker_discolsure = '#pdfjs_internal_id_352R'
    closing_date = '#pdfjs_internal_id_353R'
    special_prov1 = '#pdfjs_internal_id_360R'
    special_prov2 = '#pdfjs_internal_id_370R'
    special_prov3 = '#pdfjs_internal_id_369R'
    other_exp = '#pdfjs_internal_id_366R'
    buy_address = '#pdfjs_internal_id_416R'
    buy_email = '#pdfjs_internal_id_417R'

    prop_add1 = '#pdfjs_internal_id_280R'
    prop_add2 = '#pdfjs_internal_id_301R'
    prop_add3 = '#pdfjs_internal_id_324R'
    prop_add4 = '#pdfjs_internal_id_346R'
    prop_add5 = '#pdfjs_internal_id_362R'
    prop_add6 = '#pdfjs_internal_id_383R'
    prop_add7 = '#pdfjs_internal_id_411R'
    prop_add8 = '#pdfjs_internal_id_458R'
    prop_add9 = '#pdfjs_internal_id_490R'
    prop_add10 = '#pdfjs_internal_id_545R'
                        
    init_pg1 = '#pdfjs_internal_id_1522R'
    init_pg2 = '#pdfjs_internal_id_292R'
    init_pg3 = '#pdfjs_internal_id_320R'
    init_pg4 = '#pdfjs_internal_id_330R'
    init_pg5 = '#pdfjs_internal_id_354R'
    init_pg6 = '#pdfjs_internal_id_364R'
    init_pg7 = '#pdfjs_internal_id_376R'
    init_pg8 = '#pdfjs_internal_id_407R'        

class CheckBoxes:
    buyer_pay_title_policy = '#pdfjs_internal_id_287R'
    no_amend_or_del = '#pdfjs_internal_id_295R'
    buyer_pay_survey = '#pdfjs_internal_id_306R'
    yes_hoa = '#pdfjs_internal_id_300R'
    no_hoa = '#pdfjs_internal_id_312R'
    seller_disclosure = '#pdfjs_internal_id_331R'
    as_is = '#pdfjs_internal_id_343R'
    buyer_poss = '#pdfjs_internal_id_361R'
    hoa_addendum = '#pdfjs_internal_id_421R'
    lbp_addendum = '#pdfjs_internal_id_441R'

text_field = TextFields()
check_box = CheckBoxes()
btns = Buttons()

class Elements:
    def __init__(self, browser):
        
        self.seller = browser.find_element(By.CSS_SELECTOR, text_field.seller)
        self.buyer = browser.find_element(By.CSS_SELECTOR, text_field.buyer)
        self.lot = browser.find_element(By.CSS_SELECTOR, text_field.lot)
        self.block = browser.find_element(By.CSS_SELECTOR, text_field.block)
        self.subdivision = browser.find_element(By.CSS_SELECTOR, text_field.subdivision)
        self.city = browser.find_element(By.CSS_SELECTOR, text_field.city)
        self.county = browser.find_element(By.CSS_SELECTOR, text_field.county)
        self.address = browser.find_element(By.CSS_SELECTOR, text_field.address)
        self.exclusions = browser.find_element(By.CSS_SELECTOR, text_field.exclusions)
        self.cash_portion = browser.find_element(By.CSS_SELECTOR, text_field.cash_portion)
        self.finance_portion = browser.find_element(By.CSS_SELECTOR, text_field.finance_portion)
        self.total_price = browser.find_element(By.CSS_SELECTOR, text_field.total_price)
        self.escrow_agent = browser.find_element(By.CSS_SELECTOR, text_field.escrow_agent)
        self.title_address = browser.find_element(By.CSS_SELECTOR, text_field.title_address)
        self.em = browser.find_element(By.CSS_SELECTOR, text_field.em)
        self.om = browser.find_element(By.CSS_SELECTOR, text_field.om)
        self.add_em = browser.find_element(By.CSS_SELECTOR, text_field.add_em)
        self.add_em_days = browser.find_element(By.CSS_SELECTOR, text_field.add_em_days)
        self.op = browser.find_element(By.CSS_SELECTOR, text_field.option_days)
        self.title_name = browser.find_element(By.CSS_SELECTOR, text_field.title_company_name)
        self.survey_days = browser.find_element(By.CSS_SELECTOR, text_field.survey_days)
        self.objections = browser.find_element(By.CSS_SELECTOR, text_field.objections)
        self.objection_days = browser.find_element(By.CSS_SELECTOR, text_field.objection_days)
        self.req_notices = browser.find_element(By.CSS_SELECTOR, text_field.req_notices)
        self.sd_days = browser.find_element(By.CSS_SELECTOR, text_field.sd_days)
        self.service_contract = browser.find_element(By.CSS_SELECTOR, text_field.service_contract)
        self.broker_discolsure = browser.find_element(By.CSS_SELECTOR, text_field.broker_discolsure)
        self.closing_date = browser.find_element(By.CSS_SELECTOR, text_field.closing_date)
        self.special_prov1 = browser.find_element(By.CSS_SELECTOR, text_field.special_prov1)
        self.special_prov2 = browser.find_element(By.CSS_SELECTOR, text_field.special_prov2)
        self.special_prov3 = browser.find_element(By.CSS_SELECTOR, text_field.special_prov3)
        self.other_exp = browser.find_element(By.CSS_SELECTOR, text_field.other_exp)
        self.buy_address = browser.find_element(By.CSS_SELECTOR, text_field.buy_address)
        self.buy_email = browser.find_element(By.CSS_SELECTOR, text_field.buy_email)

        self.prop_add1 = browser.find_element(By.CSS_SELECTOR, text_field.prop_add1)
        self.prop_add2 = browser.find_element(By.CSS_SELECTOR, text_field.prop_add2)
        self.prop_add3 = browser.find_element(By.CSS_SELECTOR, text_field.prop_add3)
        self.prop_add4 = browser.find_element(By.CSS_SELECTOR, text_field.prop_add4)
        self.prop_add5 = browser.find_element(By.CSS_SELECTOR, text_field.prop_add5)
        self.prop_add6 = browser.find_element(By.CSS_SELECTOR, text_field.prop_add6)
        self.prop_add7 = browser.find_element(By.CSS_SELECTOR, text_field.prop_add7)
        self.prop_add8 = browser.find_element(By.CSS_SELECTOR, text_field.prop_add8)
        self.prop_add9 = browser.find_element(By.CSS_SELECTOR, text_field.prop_add9)

        self.init_pg1 = browser.find_element(By.CSS_SELECTOR, text_field.init_pg1)
        self.init_pg2 = browser.find_element(By.CSS_SELECTOR, text_field.init_pg2)
        self.init_pg3 = browser.find_element(By.CSS_SELECTOR, text_field.init_pg3)
        self.init_pg4 = browser.find_element(By.CSS_SELECTOR, text_field.init_pg4)
        self.init_pg5 = browser.find_element(By.CSS_SELECTOR, text_field.init_pg5)
        self.init_pg6 = browser.find_element(By.CSS_SELECTOR, text_field.init_pg6)
        self.init_pg7 = browser.find_element(By.CSS_SELECTOR, text_field.init_pg7)
        self.init_pg8 = browser.find_element(By.CSS_SELECTOR, text_field.init_pg8)


        self.buyer_pay_title_policy = browser.find_element(By.CSS_SELECTOR, check_box.buyer_pay_title_policy)
        self.no_amend_or_del = browser.find_element(By.CSS_SELECTOR, check_box.no_amend_or_del)
        self.buyer_pay_survey = browser.find_element(By.CSS_SELECTOR, check_box.buyer_pay_survey)
        self.yes_hoa = browser.find_element(By.CSS_SELECTOR, check_box.yes_hoa)
        self.no_hoa = browser.find_element(By.CSS_SELECTOR, check_box.no_hoa)
        self.sd = browser.find_element(By.CSS_SELECTOR, check_box.sd)
        self.as_is = browser.find_element(By.CSS_SELECTOR, check_box.as_is)
        self.buyer_poss = browser.find_element(By.CSS_SELECTOR, check_box.buyer_poss)
        self.hoa_addendum = browser.find_element(By.CSS_SELECTOR, check_box.hoa_addendum)
        self.lbp_addendum = browser.find_element(By.CSS_SELECTOR, check_box.lbp_addendum)