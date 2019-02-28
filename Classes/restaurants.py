import sqlite3


class restaurant:

    restaurants = 'data.db'

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

    def add_restaurant(self, name, address):
        connection = sqlite3.connect('restaurants.db')
        cursor = connection.cursor()
        # questions call the values of the tuple behind the values
        cursor.execute('INSERT INTO restaurants VALUES(?, ?, 0)', (name, address))
        connection.commit()
        connection.close()

    print(restaurants)


