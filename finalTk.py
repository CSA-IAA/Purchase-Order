'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ismail A Ahmed
Final TK program
Version .1
'''

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo #popup

root = Tk() #creates GUI
root.title("Purchase Order") #title

def about():
    messagebox.showinfo("About", "The User is entering a purchase order. They must enter their User ID, the purchase order, their name, their address, what they purchased \
, when they purchased the item, and the price of the item. They must also select their shipping type.\nThe user can also retrieve past purchase orders that they made in the system \
as all purchase order information is saved in the system.")

def hel():
    showinfo("Help", "User ID: The User ID must be exactly 9 characters long.\nZip Code: The Zip code must be 5 digits and it cannot be a negative number. It also cannot include decimals.\nItem price: The Item price must be a positive number and it cannot have more than 2 digits after the decimal. It also cannot have a number and then the decimal without any number after the decimal.")

def day_month(*args):
    if int(month.get()) == 2: #so that if user chooses "2" they can't choose "31" since there arent 31 days in february
        day.configure(to=28)
    elif int(month.get()) == 4:
        day.configure(to=30)
    elif int(month.get()) == 6:
        day.configure(to=30)
    elif int(month.get()) == 9:
        day.configure(to=30)
    elif int(month.get()) == 11:
        day.configure(to=30)
    elif int(month.get()) == 1: #cuz if they went to "11" and max was "30" then down to "10" max still stays "30" not "31"
        day.configure(to=31)
    elif int(month.get()) == 3:
        day.configure(to=31)
    elif int(month.get()) == 5:
        day.configure(to=31)
    elif int(month.get()) == 7:
        day.configure(to=31)
    elif int(month.get()) == 8:
        day.configure(to=31)
    elif int(month.get()) == 10:
        day.configure(to=31)
    elif int(month.get()) == 12:
        day.configure(to=31)

def check():
    # checks to make sure that the user has done everything before checking to see if it was done correctly
    if len(ships.curselection()):
        if len(PO.get()):
            if len(Fname.get()):
                if len(Lname.get()):
                    if len(address.get()):
                        if len(city.get()):
                            if len(States.get()):
                                if len(zipcode.get()):
                                    if len(items.get("1.0", "end-1c")) > 0:
                                        if len(price.get()):
                                            if len(userID.get()) == 9:
                                                # only if user completes everything
                                                confirm()
                                            else:
                                                showinfo("Error", "Please make sure have entered a User ID and that it is exactly nine characters long!")
                                                #user id check here so this error whont show if they didnt enter anything
                                        else:
                                            showinfo("Error", "Please enter in all of the information!")
                                    else:
                                        showinfo("Error", "Please enter in all of the information!")
                                else:
                                    showinfo("Error", "Please enter in all of the information!")
                            else:
                                showinfo("Error", "Please enter in all of the information!")
                        else:
                            showinfo("Error", "Please enter in all of the information!")
                    else:
                        showinfo("Error", "Please enter in all of the information!")
                else:
                    showinfo("Error", "Please enter in all of the information!")
            else:
                showinfo("Error", "Please enter in all of the information!")
        else:
            showinfo("Error", "Please enter in all of the information!")
    else:
        showinfo("Error", "Please enter in all of the information!")  # popup if they don't enter something

def confirm():
    try:
        if int(zipcode.get()) >= 0 and len(zipcode.get()) == 5:
            if float(price.get()) >= 0:
                if '.' in price.get():
                    if len(price.get().rsplit('.')[-1]) < 3 and len(price.get().rsplit('.')[-1]) > 0: #makes sure there is 1 or 2 numbers after decimal
                        calculate()
                    else:
                        showinfo("Error", "Please make sure that your item price does not have more than 2 digits after the decimal point and that it has a digit after the decimal point!")
                else: #otherwise '100' wont be accepted
                    calculate()
            else:
                showinfo("Error", "Please make sure you enter only positive numbers in numerical form!")
        else:
            showinfo("Error", "Please make sure you enter only positive numbers in numerical integer form with 5 digits for zip code!")
    except ValueError:
        showinfo("Error", "Please make sure you enter only positive numbers in numerical form for both zip code and item price! Also, make sure that your zipcode does not have a decimal.")

def calculate():
    box1 = ships.get(ANCHOR) #gets what they selected for price
    if box1 == "One day - $10": #if they selected one day then they pay 10 bucks
        ship_cost = 10
    elif box1 == "Two days - $5": #if they selected two days then they pay 5 bucks
        ship_cost = 5
    elif box1 == "Five days - $3": #if they selected five days then they pay 3 bucks
        ship_cost = 3
    tax_tax = (float(price.get()) * 0.0825) #how much tax there is on the product
    tax_tax = round(tax_tax, 2) #rounds tax to the second digit
    total_pricez = (float(price.get()) + tax_tax) #adds how much tax there is on the product with the price
    total_price = total_pricez + ship_cost #adds in shipping fee-no tax
    total_price = round(total_price, 2) #rounds the total price to the second digit
    total.set("Total: $"+ str(total_price))
    tax.set("Tax: $"+str(tax_tax))
    finish()

def finish():
    outfile = open('orderfile.txt', 'a') #if file doesnt exist, otherwise reading it wont be possible
    infile = open('orderfile.txt', 'r')
    content = infile.readlines()
    content = [x.strip() for x in content]
    # creates a list with the users in differnet elements(have commas seperating)
    z = [i.split('~', 1)[0] for i in content]  # gets the PO from the "content" list and puts in a new list
    if PO.get() in z:  # checks to see if PO user put in is in username list(z)
        showinfo("Error", "Sorry, but that purchase order already exists. Please try again!")
        infile.close()
        outfile.close()

    else:
        file = (PO.get() + '~' + userID.get() + '~' + Fname.get() + '~' + Lname.get() + '~' + address.get() + '~' +
                city.get() + '~' + States.get() + '~' + zipcode.get() + '~' + items.get("1.0", END) + '~'+ price.get() +
                '~' + ships.get(ANCHOR) + '~' + day.get() + '~' + month.get() + '~' + year.get() + '~' + tax.get() +
                '~' + total.get() + '\n') #stores in one variable so it can be written to file
        file = file.replace("\n", "", 1) #new line is created because of that END in items.get
        outfile.write(file) #writes info to file
        outfile.close()
        infile.close()
        showinfo("Success", "Congratulations, your purchase order has been successfully saved to the system!")
status = False
def retrieve():
    global status
    status = False
    if len(PO.get()): #to make sure they have entered a PO when they click retrieve button
        infile = open("orderfile.txt", 'r')
        content = infile.readlines()
        content = [x.strip() for x in content] #creates a list with orders in differnet elements(have commas seperating)
        z = [i.split('~', 1)[0] for i in content] # gets the PO from the "content" list and puts in a new list
        for x in z: #goes through each element(PO) and prints them on seperate lines without the junk(, [] '')
            if x == PO.get(): #as it goes through each element, it checks to see if that is the PO entered
                status = True
                a = z.index(x) #locates the INDEX of the PO(x) which has userID AND OTHER info from the "z" list
                b = [content[a]] #prints everything that is located in the PO(x) index from the "content" list as list
                l = [words for segments in b for words in segments.split('~')]
                # this splits the string/element(has only 1) in list. before:['PO~userID~First~Last~Street~City~Alaska~Zip~PItems~IPrice~Two days~3~1~2020']
                # after: ['PO', 'userID', 'First', 'Last', 'Street', 'City', 'Alaska', 'Zip', 'PItems', 'IPrice', 'Two days', '3', '1', '2020']

                userID.set(l[1]) #sets userid to that from the requested purchase order
                Fname.set(l[2]) #sets first name to that from the requested purchase order
                Lname.set(l[3]) #sets last name to that from the requested purchase order
                address.set(l[4]) #sets street address to that from the requested purchase order
                city.set(l[5]) #sets city to that from the requested purchase order
                States.set(l[6]) #sets state to that from the requested purchase order
                zipcode.set(l[7]) #sets zip code to that from the requested purchase order
                items.delete("1.0", END) #if there is an item in the text widget when they retrieve the product order, else it will say both products even though one isnt from the requested product order
                items.insert(END, l[8]) #inserts in the product to that from the requested purchase order
                price.set(l[9])#sets price to that from the requested purchase order
                day.delete(0, END)
                day.insert(0, l[11]) #sets day to that from the requested purchase order
                month.delete(0, END)
                month.insert(0, l[12]) #sets month to that from the requested purchase order
                year.delete(0, END)
                year.insert(0, l[13]) #sets year to that from the requested purchase order
                tax.set(l[14]) #sets tax to that from the requested purchase order
                total.set(l[15]) #sets total to that from the requested purchase order

                ships.select_clear(0, END)  # clears the selection
                a = ['One day - $10', 'Two days - $5', 'Five days - $3']
                z = a.index(l[10]) #finds the index of of one day/2 days/3 days(one of them-the one the user submitted)
                ships.select_set(z) #sets the listbox at the index of what the user submitted
                break # look at the for loop that doesnt have the list. if 5 users and the 2nd one is the users, three...
                # ...others are not the ones requested. if dont have break it will say NOT FOUND under the else. this...
                # ...breaks it after the user is found and doesn't go any further
        infile.close()
    else:
        messagebox.showinfo("Error", "Please enter a PO.")  # incase there is no PO entry when user clicks 'retrieve' button

    if status == False and len(PO.get()) > 0:
        messagebox.showinfo("Error", "Requested PO not found")


def clear():
    ships.select_clear(0, END)  # clears the selection
    items.delete("1.0", END)  # deletes given purchased items from textbox
    items.insert(END, "")  # adds blank space into text widget
    day.delete(0, END) #deletes the day
    day.insert(0, "1")  #inserts the default '1'
    month.delete(0, END) #deletes the month
    month.insert(0, "1")  #inserts the default '1'
    year.delete(0, END) #deletes the year
    year.insert(0, "2017")  #inserts the default '2017'
    userID.set('')  # clears the user ID
    PO.set('')  # clears the PO
    Fname.set('')  # clears the first name
    Lname.set('')  # clears the left name
    address.set('')  # clears the street address
    city.set('')  # clears the city
    States.set('')  # clears the state
    zipcode.set('')  # clears the zip code
    price.set('')  # clears the item price
    tax.set("Tax: $")  # clears the tax
    total.set("Total: $")  # clears the total price


root.option_add('*tearOff', FALSE) #gets rid of dashed line
menu = Menu(root) #creates menu
root.config(menu=menu) #adds ability to create options

subMenu = Menu(menu) #creats submenu
menu.add_cascade(label="File", menu=subMenu) # creates a memu option
subMenu.add_command(label="Exit", command=root.destroy) #file option

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu) #creates another menu option
helpMenu.add_command(label="Help", command=hel) #file option
helpMenu.add_command(label="About", command=about) #file option

mainframe = ttk.Frame(root, padding="5 10")
mainframe.grid(column=0, row=0, columnspan=3, rowspan=3, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

years = ['2017', '2018', '2019', '2020']
ship_day = ['One day - $10', 'Two days - $5', 'Five days - $3']

userID = StringVar()
PO = StringVar()
Fname = StringVar()
Lname = StringVar()
address = StringVar()
city = StringVar()
States = StringVar()
zipcode = StringVar()
price = StringVar()
shipping = StringVar(value=ship_day)
spin_day = StringVar()
spin_month = StringVar()
spin_year = StringVar()
tax = StringVar()
total = StringVar()

ttk.Entry(mainframe, textvariable=PO).grid(column = 2, row = 1, sticky = W)
ttk.Entry(mainframe, textvariable=userID).grid(column = 2, row = 2, sticky = W)
ttk.Entry(mainframe, textvariable=Fname).grid(column = 2, row = 3, sticky = W)
ttk.Entry(mainframe, textvariable=Lname).grid(column = 2, row = 4, sticky = W)
ttk.Entry(mainframe, textvariable=address).grid(column = 2, row = 5, sticky = W)
ttk.Entry(mainframe, textvariable=city, width = 20).grid(column = 2, row = 6, sticky = W)
ttk.Entry(mainframe, textvariable=zipcode).grid(column = 2, row = 8, sticky = W)
ttk.Entry(mainframe, textvariable=price, width = 20).grid(column = 4, row = 1, sticky = W)

state = ttk.Combobox(mainframe, textvariable=States, width=15, state = 'readonly')
state.grid(column=2, row=7, sticky=(W,E))
state['values'] = ('Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', \
         'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', ' Iowa', 'Kansas', 'Kentucky', 'Louisiana', \
         'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', \
         'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'Ohio', \
         'Oklahoma','Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', \
         'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming')
#states of the US
day = Spinbox(mainframe, from_=1, to=31, textvariable=spin_day, width = 10)#spinbox that has day numbers
day.grid(column=4, row = 4, sticky = W)
month = Spinbox(mainframe, from_=1, to=12, textvariable=spin_month, width = 4, command=day_month)#spinbox that has month numbers
month.grid(column=4, row = 4, sticky = E)
year = Spinbox(mainframe, values=years, textvariable=spin_year, width = 10)#spinbox that has year numbers
year.grid(column=5, row = 4, sticky = W)

items = Text(mainframe,wrap=WORD, width = 15,height=5)
#text widget that the items purchased. wrap makes sure that a word doesn't strech onto more than one line
items.grid(column=2, row = 9, sticky=(W,E)) #graph on diff line else "no index" error
items.insert(END, "") #adds text into text widget

ships = Listbox(mainframe, height=3, listvariable=shipping, exportselection=0) #shipping days
ships.grid(column = 4, row = 2, sticky = (N,W,E,S))
#creates listbox which has shipping days. listvariable acceses the shipping days and adds to listbox

ttk.Button(mainframe, text="Submit", width = 8, command=check).grid(column=4, row=7, sticky = (N,W))
ttk.Button(mainframe, text="Clear", width = 8, command=clear).grid(column=4, row=7, sticky = (N,E))
ttk.Button(mainframe, text="Retrieve", width = 9, command=retrieve).grid(column=5, row=7, sticky = (N,W))

ttk.Label(mainframe, text = "P.O.").grid(column = 1, row = 1, sticky =W)
ttk.Label(mainframe, text = "User ID").grid(column = 1, row = 2, sticky =W)
ttk.Label(mainframe, text = "First Name").grid(column = 1, row = 3, sticky =W)
ttk.Label(mainframe, text = "Last Name").grid(column = 1, row = 4, sticky =W)
ttk.Label(mainframe, text = "Street Address").grid(column = 1, row = 5, sticky =W)
ttk.Label(mainframe, text = "City").grid(column = 1, row = 6, sticky =W)
ttk.Label(mainframe, text = "State").grid(column = 1, row = 7, sticky =W)
ttk.Label(mainframe, text = "Zip Code").grid(column = 1, row = 8, sticky =W)
ttk.Label(mainframe, text = "Purchased Items").grid(column = 1, row = 9, sticky =W)
ttk.Label(mainframe, text = "Item Price").grid(column = 3, row = 1, sticky =W)
ttk.Label(mainframe, text = "Shipping").grid(column = 3, row = 2, sticky =W)
ttk.Label(mainframe, text = "Day").grid(column = 4, row = 3, sticky =W)
ttk.Label(mainframe, text = "Month").grid(column = 4, row = 3, sticky =E)
ttk.Label(mainframe, text = "Year").grid(column = 5, row = 3, sticky =W)
ttk.Label(mainframe, text = "Purchase Date").grid(column = 3, row = 4, sticky =W)
ttk.Label(mainframe, text = "Tax: ", textvariable=tax).grid(column = 4, row = 5, sticky =W)
ttk.Label(mainframe, text = "Total: ", textvariable=total).grid(column = 4, row = 6, sticky =W)
tax.set("Tax: $")
total.set("Total: $")
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

#continues the loop
root.mainloop()