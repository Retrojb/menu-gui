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

        connection.close()
        return restaurants

    def get_one_restaurant(self, name):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        cursor.execute('SELECT name=? FROM restaurant', (name,))
        restaurant = [{'name': row[0], 'address': row[1], 'visited': row[3]} for row in cursor.fetchone()]

        connection.close()
        return restaurant

    def add_restaurant(self, name, address):
        connection = sqlite3.connect('restaurants.db')
        cursor = connection.cursor()
        # questions call the values of the tuple behind the values
        cursor.execute('INSERT INTO restaurants VALUES(?, ?, 0)', (name, address))
        connection.commit()
        connection.close()

    def update_restaurant(self, name):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        cursor.execute('UPDATE restaurants SET name='' WHERE name=? ', (name,))
        connection.commit()
        connection.close()


    def mark_if_visted(self, name):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        cursor.execute('UPDATE restaurants SET visited=1 WHERE name=?', (name,))
        connection.commit()
        connection.close()


    def delete_restaurant(self, name):
        connection = sqlite3.connect('restaurant.db')
        cursor = connection.cursor()

        cursor.execute('DELETE FROM restaurants WHERE name=?', (name,))
        connection.commit()
        connection.close()
