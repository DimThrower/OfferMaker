import tkinter as tk
from tkinter import Entry, Label, Checkbutton, StringVar
from main.Scripts import misc, tax_scrape, write_offer
import tkinter.messagebox
from main.Static.settings import TREC, TREC_types
    

def submit():

    trec = TREC()
    trec_types = TREC_types()

    address = address_var.get()
    doc_name = doc_name_var.get()
    seller_name = seller_name_var.get()
    buyer_name = buyer_name_var.get()
    price = price_var.get()
    closing_days = closing_days_var.get()
    title_company = title_company_var.get()
    escrow_officer = escrow_officer_var.get()
    title_company_address = title_company_address_var.get()
    earnest_money = earnest_money_var.get()
    option_money = option_money_var.get()
    option_days = option_days_var.get()

    # Check the values of default buttons
    doc_name_default = doc_name_default_var.get()
    seller_name_default = seller_name_defualt_var.get()
    buyer_name_default = buyer_name_default_var.get()
    closing_days_default = closing_days_default_var.get()
    title_company_default = title_company_default_var.get()
    escrow_officer_default = escrow_officer_default_var.get()
    title_company_address_default = title_company_address_default_var.get() 
    earnest_money_default = earnest_money_default_var.get()
    option_money_default = option_money_default_var.get()
    option_days_default = option_days_default_var.get()

    contract_type = variable.get()

        # Define the fields to validate as a list of tuples
    fields_to_validate = [
        (address, False),  # Address doesn't have a default option
        (doc_name, doc_name_default),
        (seller_name, seller_name_default),
        (buyer_name, buyer_name_default),
        (price, False),  # Price doesn't have a default option
        (closing_days, closing_days_default),
        (title_company, title_company_default),
        (escrow_officer, escrow_officer_default),
        (title_company_address, title_company_address_default),
        (earnest_money, earnest_money_default),  # Earnest Money doesn't have a default option
        (option_money, option_money_default),
        (option_days, option_days_default),
    ]

     # Check if any of the fields are non-empty or their default buttons are checked
    checked_fields = list(map(misc.has_non_empty_string_or_true, fields_to_validate))

    # Make sure all field has a submission
    valid_submission = all(checked_fields)

    if valid_submission:
        print("Submit valid data")

        tax_details = tax_scrape.tax_scrape(address)

        if doc_name_default:
            doc_name = f"{address} Offer Draft"

        if seller_name_default:
            seller_name = tax_details["owner_name_val"]

        if buyer_name_default:
            buyer_name = "Cornerstone Home Solutions, LLC"

        if closing_days_default:
            closing_date = misc.generate_closing_date()
        else:
            closing_date = misc.generate_closing_date(int(closing_days))

        if title_company_default:
            title_company = 'StarTex Title (Carrie)'

        if escrow_officer_default:
            escrow_officer = 'Carrie Morrison'

        if title_company_address_default:
            title_company_address = '1111 N Loop W Suite 1100, 77008'

        if earnest_money_default:
            if misc.convert_str_2_float(price) * 0.01 > 950:
                earnest_money = 950
            else:
                earnest_money = misc.convert_str_2_float(price) * 0.01

        if option_money_default:
            option_money = 50

        if option_days_default:
            option_days = 10

        legal_description = tax_details['legal_description_val']
        block = tax_details['block_val']
        lot = tax_details['lot_val']
        subdivision = tax_details['subdivision_val']
        city = tax_details['city']
        zip_code = tax_details['zip_code']
        county = tax_details['county']

        if contract_type == TREC_types.signed_with_POF:
            trec_path = trec.signed_with_pof
        elif contract_type == TREC_types.signed:
            trec_path = trec.signed
        elif contract_type == TREC_types.backside:
            trec_path = trec.backside
        else:
            trec_path = trec.not_signed


        print("Document Name:", doc_name)
        print("Seller Name:", seller_name)
        print("Buyer Name:", buyer_name)
        print("Price:", price)
        print("Closing Days:", closing_days)
        print("Title Company:", title_company)
        print("Escrow Officer:", escrow_officer)
        print("Title Company Address:", title_company_address)
        print("Earnest Money:", earnest_money)
        print("Option Money:", option_money)
        print("Option Days:", option_days)
        print("Legal Description",legal_description)
        print("Block", block)
        print('Lot', lot)
        print('Subdivision', subdivision)
        print('City:', city)
        print('Zip Code:', zip_code)
        print("County:", county)
        print("Contract Type:", contract_type)

        file_result, file_path = write_offer.create_offer(
            doc_name=doc_name, 
            address=address, 
            seller_name=seller_name,
            buyer_name=buyer_name, 
            price=price, 
            lot=lot, 
            block=block,
            closing_date=closing_date, 
            title_company=title_company, 
            legal_description=legal_description,
            title_company_address=title_company_address,
            earnest_money=earnest_money, 
            option_money=option_money, 
            city=city, 
            zip_code=zip_code,
            subdivision=subdivision, 
            county=county, 
            escrow_agent=escrow_officer, 
            option_days=option_days,
            trec_path=trec_path,
        )

        if file_result == "file saved":
            tkinter.messagebox.showinfo("Success", f"File saved at {file_path}")
        if file_result == "file already exist":
            tkinter.messagebox.showerror("Failed", f"File already exist at {file_path}")
        if file_result == "error":
            tkinter.messagebox.showerror("Failed", f"Internal error, contact admin")
        
    else:
        # Display an error message on the GUI
        tkinter.messagebox.showerror("Error", "Please fill out the input fields or check the default buttons")


    # tax_details = tax_scrape(address)
    
    # print("Document Name:", doc_name)
    # print("Seller Name:", seller_name)
    # print("Buyer Name:", buyer_name)
    # print("Price:", price)
    # print("Closing Date:", closing_date)
    # print("Title Company:", title_company)
    # print("Escrow Officer:", escrow_officer)
    # print("Title Company Address:", title_company_address)
    # print("Earnest Money:", earnest_money)
    # print("Option Money:", option_money)
    # print("Option Days:", option_days)

    #property_details = tax_scrape()

app = tk.Tk()
app.title("Offer Input Form")



options = [TREC_types.signed_with_POF, 
           TREC_types.signed, 
           TREC_types.not_signed,
           TREC_types.backside,]

# Create a tkinter variable to store the selected option
variable = tk.StringVar(app)
variable.set(options[0])  # Set the default selected option

# Labels
Label(app, text="Address:").grid(row=0, column=0)
Label(app, text="Document Name:").grid(row=1, column=0)
Label(app, text="Seller Name:").grid(row=2, column=0)
Label(app, text="Buyer Name:").grid(row=3, column=0)
Label(app, text="Price:").grid(row=4, column=0)
Label(app, text="Closing Days:").grid(row=5, column=0)
Label(app, text="Title Company:").grid(row=6, column=0)
Label(app, text="Escrow Officer:").grid(row=7, column=0)
Label(app, text="Title Company Address:").grid(row=8, column=0)
Label(app, text="Earnest Money:").grid(row=9, column=0)
Label(app, text="Option Money:").grid(row=10, column=0)
Label(app, text="Option Days:").grid(row=11, column=0)
Label(app, text="Contract Type:").grid(row=12, column=0)


# Entry fields with adjusted width
entry_width = 50  # Adjust the width as needed

address_var = StringVar()
doc_name_var = StringVar()
seller_name_var = StringVar()
buyer_name_var = StringVar()
price_var = StringVar()
closing_days_var = StringVar()
title_company_var = StringVar()
escrow_officer_var = StringVar()
title_company_address_var = StringVar()
earnest_money_var = StringVar()
option_money_var = StringVar()
option_days_var = StringVar()

address_entry = Entry(app, textvariable=address_var, width=entry_width)
doc_name_entry = Entry(app, textvariable=doc_name_var, width=entry_width)
seller_name_entry = Entry(app, textvariable=seller_name_var, width=entry_width)
buyer_name_entry = Entry(app, textvariable=buyer_name_var, width=entry_width)
price_entry = Entry(app, textvariable=price_var, width=entry_width)
closing_days_entry = Entry(app, textvariable=closing_days_var, width=entry_width)
title_company_entry = Entry(app, textvariable=title_company_var, width=entry_width)
escrow_officer_entry = Entry(app, textvariable=escrow_officer_var, width=entry_width)
title_company_address_entry = Entry(app, textvariable=title_company_address_var, width=entry_width)
earnest_money_entry = Entry(app, textvariable=earnest_money_var, width=entry_width)
option_money_entry = Entry(app, textvariable=option_money_var, width=entry_width)
option_days_entry = Entry(app, textvariable=option_days_var, width=entry_width)

# Create the OptionMenu widget
dropdown = tk.OptionMenu(app, variable, *options)
dropdown.grid(row=12, column=1)

# Create a label to display the selected option
label = tk.Label(app, text='')
label.grid(row=13, column=0, columnspan=2)


address_entry.grid(row=0, column=1)
doc_name_entry.grid(row=1, column=1)
seller_name_entry.grid(row=2, column=1)
buyer_name_entry.grid(row=3, column=1)
price_entry.grid(row=4, column=1)
closing_days_entry.grid(row=5, column=1)
title_company_entry.grid(row=6, column=1)
escrow_officer_entry.grid(row=7, column=1)
title_company_address_entry.grid(row=8, column=1)
earnest_money_entry.grid(row=9, column=1)
option_money_entry.grid(row=10, column=1)
option_days_entry.grid(row=11, column=1)

# Check buttons for default options
doc_name_default_var = tk.BooleanVar()
seller_name_defualt_var = tk.BooleanVar()
buyer_name_default_var = tk.BooleanVar()
closing_days_default_var = tk.BooleanVar()
title_company_default_var = tk.BooleanVar()
escrow_officer_default_var = tk.BooleanVar()
title_company_address_default_var = tk.BooleanVar()
earnest_money_default_var = tk.BooleanVar()
option_money_default_var = tk.BooleanVar()
option_days_default_var = tk.BooleanVar()



def toggle_entry_state(entry, var):
    if var.get():
        entry.config(state="disabled")
    else:
        entry.config(state="normal")

Checkbutton(app, text="Default", variable=doc_name_default_var, command=lambda: toggle_entry_state(doc_name_entry, doc_name_default_var)).grid(row=1, column=2)
Checkbutton(app, text="Realist", variable=seller_name_defualt_var, command=lambda: toggle_entry_state(seller_name_entry, seller_name_defualt_var)).grid(row=2, column=2)
Checkbutton(app, text="Default", variable=buyer_name_default_var, command=lambda: toggle_entry_state(buyer_name_entry, buyer_name_default_var)).grid(row=3, column=2)
Checkbutton(app, text="Default", variable=closing_days_default_var, command=lambda: toggle_entry_state(closing_days_entry, closing_days_default_var)).grid(row=5, column=2)
Checkbutton(app, text="Default", variable=title_company_default_var, command=lambda: toggle_entry_state(title_company_entry, title_company_default_var)).grid(row=6, column=2)
Checkbutton(app, text="Default", variable=escrow_officer_default_var, command=lambda: toggle_entry_state(escrow_officer_entry, escrow_officer_default_var)).grid(row=7, column=2)
Checkbutton(app, text="Default", variable=title_company_address_default_var, command=lambda: toggle_entry_state(title_company_address_entry, title_company_address_default_var)).grid(row=8, column=2)
Checkbutton(app, text="Default", variable=earnest_money_default_var, command=lambda: toggle_entry_state(earnest_money_entry, earnest_money_default_var)).grid(row=9, column=2)
Checkbutton(app, text="Default", variable=option_money_default_var, command=lambda: toggle_entry_state(option_money_entry, option_money_default_var)).grid(row=10, column=2)
Checkbutton(app, text="Default", variable=option_days_default_var, command=lambda: toggle_entry_state(option_days_entry, option_days_default_var)).grid(row=11, column=2)



# Set the initial values for default checkboxes
doc_name_default_var.set(True)
seller_name_defualt_var.set(True)
buyer_name_default_var.set(True)
closing_days_default_var.set(True)
title_company_default_var.set(True)
escrow_officer_default_var.set(True)
title_company_address_default_var.set(True)
earnest_money_default_var.set(True)
option_money_default_var.set(True)
option_days_default_var.set(True)
toggle_entry_state(doc_name_entry, doc_name_default_var)
toggle_entry_state(seller_name_entry, seller_name_defualt_var)
toggle_entry_state(buyer_name_entry, buyer_name_default_var)
toggle_entry_state(closing_days_entry, closing_days_default_var)
toggle_entry_state(title_company_entry, title_company_default_var)
toggle_entry_state(escrow_officer_entry, escrow_officer_default_var)
toggle_entry_state(title_company_address_entry, title_company_address_default_var)
toggle_entry_state(earnest_money_entry, earnest_money_default_var)
toggle_entry_state(option_money_entry, option_money_default_var)
toggle_entry_state(option_days_entry, option_days_default_var)

# Submit button
tk.Button(app, text="Submit", command=submit).grid(row=14, column=1)

app.mainloop()
