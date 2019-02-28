import sqlite3


class Restaurant:

    restaurants = 'restaurant.db'

    def __init__(self, name, address, visited):
        self.name = name
        self.address = address
        self.visited = visited

    def __getitem__(self, r):
        return self.restaurants[r]


    def create_restaurant_table(self):
        connect = sqlite3.connect('restaurants.db')
        cursor = connect.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS restaurants(name text primary key, address text, visited integer) ')

        connect.commit()
        connect.close()


    def get_all_restaurants(self):
        connection = sqlite3.connect('restaurants.db')
        cursor = connection.cursor()

        cursor.excute('SELECT name, * FROM restaurants')
        restaurants = [{'name': row[0], 'address': row[1], 'visited': row[3]} for row in cursor.fetchall()]
        # restaurants = cursor.fetchall()  #returns a list of tupils [(name, address, visited)...)]
        #convert tuples to dictionary


        connection.close()
        return cursor

    def add_restaurant(self, name, address):
        connection = sqlite3.connect('restaurants.db')
        cursor = connection.cursor()
        # questions call the values of the tuple behind the values
        cursor.execute('INSERT INTO restaurants VALUES(?, ?, 0)', (name, address))
        connection.commit()
        connection.close()

    def update_restaurant(self):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        cursor.execute()
        connection.commit()
        connection.close()


    def mark_if_visted(self, name):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        cursor.execute()
        connection.commit()
        connection.close()


    def delete_restaurant(self):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        cursor.execute()
        connection.commit()
        connection.close()