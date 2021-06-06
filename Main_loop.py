# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:27:15 2021

@author: Sajan Gaba
"""
#%%
# Defining dummy contact
import csv
import os
ph_nums = [["Sajan","2123431343"],
           ["Gaba","43224334"],
           ["Chadf","1212323232"]]
ph_header = ["Index","Name","Phone Number"]
name_pos = 0
num_pos = 1
#%%
def save_phone_list():
    f = open("phonebook.csv",'w',newline="")
    for item in ph_nums:
        csv.writer(f).writerow(item)
    f.close()     
#%%
def phone_header_format(phone,index):
    out1 = "{0:<4} {1:<26} {2:15}"
    print(out1.format(index, phone[name_pos], phone[num_pos]))
#%%
def main_menu():
    print("Choose one of the following item from menu?")
    print("Press 'S' to Show")
    print("Press 'N' to add new contact")
    print("Press 'E' to edit")
    print("Press 'D' to delete")
    print("Press 'Q' to quit")
    n = ["S","N","E","D","Q"]
    action = input("Choice: ")
    if action.upper() in n:
        return action.upper()
    else:
        print("That's an invalid option. Please try again")
        return None
    save_phone_list()
#%%    
def show_item():
    print("Showing Saved Contacts...")
    phone_header_format(ph_header,"")
    index = 1
    for phone in ph_nums:
        phone_header_format(phone,index)
        index = index+1
    print()
#%%
def add_item():
    print("Adding New Contact...")
    in_name = input("Enter the name:")
    in_num = input("Enter the phone number:")
    phone = [in_name,in_num]
    ph_nums.append(phone)
    print("")
    main_loop()
#%%
def editing_item():
    print("Editing Current Contact...")
    e_item = input("Enter the index of contact you want to edit")
    e_item = int(e_item)
    print(ph_nums[e_item-1])
    ph = ph_nums[e_item-1]
    print(ph[name_pos])
    new_name = input("Enter the new name or press enter to skip: ")
    if new_name=="":
        new_name = ph[0]
    print(ph[num_pos])
    new_num = input("Enter the new number or press enter to skip: ")
    if new_num == "":
        new_num = ph[1]
    new_entry = [new_name, new_num]
    print(new_entry)
    ph_nums[e_item-1]=new_entry
    print("Your editings has been updated")
#%%
def delete_phone(del_item):
    del_item = int(del_item)
    del ph_nums[del_item-1]
    print("Deleted Phone#",del_item)
#%%
def deleting_item():
    print("Deleting Current Contact...")
    del_item = input("Choose the index number to delete:")
    try:
        del_item = int(del_item)
    except:
        print("Please enter a numerical value")
    if del_item.isdigit==False:
        print("Please enter a numerical value")
    if del_item <=0:
        print("Please enter a valid number")
        print()
    if del_item<=len(ph_nums):
        print("Please enter one from the available index")
        main_loop()
    if not del_item.isdigit():
        print("The number you have entered is not valid.")
    delete_phone(del_item)
#%%
def quit_item():
    print("Exiting Now, see you next time...")
    save_phone_list()
#%%
def load_list():
    if os.access("phonebook.csv",os.F_OK):
        l = open("phonebook.csv")
        for row in csv.reader(l):
            ph_nums.append(row)
        l.close()
#%%
def main_loop():
    load_list()
    while True:
        choice = main_menu()
        if choice=="S":
            show_item()
        if choice=="N":
            add_item()
        if choice=="E":
            editing_item()
        if choice=="D":
            deleting_item()
        if choice=="Q":
            quit_item()
        else:
            return None
        
    save_phone_list()