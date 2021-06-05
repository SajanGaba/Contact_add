# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 15:27:15 2021

@author: Sajan Gaba
"""
#%%
# Defining dummy contact
ph_nums = [["Sajan","2123431343"],
           ["Gaba","43224334"],
           ["Chadf","1212323232"]]
ph_header = ["Index","Name","Phone Number"]
name_pos = 0
num_pos = 1
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
#%%
def editing_item():
    print("Editing Current Contact...")
#%%
def deleting_item():
    print("Deleting Current Contact...")
#%%
def quit_item():
    print("Exiting Now, see you next time...")
#%%
def main_loop():
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
        