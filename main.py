import tkinter as tk
from tkinter import messagebox, simpledialog

USER_CHOICE = """
Enter:
-'a' to add a new restaurant
-'l' to list all restaurants
-'r' tp mark a restaurant as visited
-'d' to delete a restaurant
-'q' to quit

Your choice:"""


def user_interface():
    user_input = simpledialog.askstring('Welcome', 'Good Day old sport! \n' + {USER_CHOICE})
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_restaurant()
        elif user_input == 'l':
            list_restaurants()
        elif user_input == 'r':
            prompt_visited()
        elif user_input == 'd':
            prompt_delete()
        else:
            print("Command Error: Try Again \n " + {USER_CHOICE})


'''
    Long term would be to change these commands into switch cases and getters to refactor
    ie. def add(): return restaurant.add_restaurant
    def requested_user_action(): switch = { 1: add, 2:....} func = switch.get(arg, " something ")  return func
    which would later lower the lines writen out. Possible to abstract out in the long run?
'''


def prompt_add_restaurant():
    name = simpledialog.askstring('Add', 'Enter the name of a new restaurant: ')
    address = simpledialog.askstring('Add', f'Enter the address {name}: ')

    restaurants.add_restaurant(name, address)


def list_restaurants():
    global restaurants
    restaurants = restaurants.get_all_restaurants()
    for restaurant in restaurants:
        return restaurant


def prompt_visited():
    name = simpledialog.askstring('Visited', 'Enter a restaurant you have been to: ')

    restaurants.mark_if_visited(name)


def prompt_delete():
    return

class Gui:
    root = tk.Tk()

    # as of 10pm 2/26 returning error module 'class.restaurants' has no attribute 'get_all_restaurnats'
    restaurants.get_all_restaurants()
    root.mainloop()
