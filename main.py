import tkinter as tk
from tkinter import messagebox, simpledialog


class UserInterface:

    USER_CHOICE = """
    Enter:
    -'a' to add a new restaurant
    -'l' to list all restaurants
    -'r' tp mark a restaurant as visited
    -'d' to delete a restaurant
    -'q' to quit
    
    Your choice:"""

    def user_interface(self):
        user_input = simpledialog.askstring('Welcome', 'Good Day old sport! \n' + {UserInterface.USER_CHOICE})
        while user_input != 'q':
            if user_input == 'a':
                UserInterface.prompt_add_restaurant()
            elif user_input == 'l':
                UserInterface.list_restaurants()
            elif user_input == 'r':
                UserInterface.prompt_visited()
            elif user_input == 'd':
                UserInterface.prompt_delete()
            else:
                messagebox.showinfo('Error', "Command Error: Try Again \n " + {UserInterface.USER_CHOICE})

    '''
        Long term would be to change these commands into switch cases and getters to refactor
        ie. def add(): return restaurant.add_restaurant
        def requested_user_action(): switch = { 1: add, 2:....} func = switch.get(arg, " something ")  return func
        which would later lower the lines writen out. Possible to abstract out in the long run?
    '''

    def prompt_add_restaurant(self):
        name = simpledialog.askstring('Add', 'Enter the name of a new restaurant: ')
        address = simpledialog.askstring('Add', f'Enter the address {name}: ')

        restaurants.add_restaurant(name, address)

    def list_restaurants(self):
        global restaurants
        restaurants = restaurants.get_all_restaurants()
        for restaurant in restaurants:
            return restaurant

    def prompt_visited(self):
        name = simpledialog.askstring('Visited', 'Enter a restaurant you have been to: ')

        restaurants.mark_if_visited(name)

    def prompt_delete(self):
        return


root = tk.Tk()
root.mainloop()
