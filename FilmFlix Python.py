import sqlite3

# Function to connect to the database
def connect_to_database():
    try:
        connection = sqlite3.connect("filmflix 2.db")
        return connection
    except sqlite3.Error as e:
        print("Error connecting to the database:", e)
        return None


# Function to create the table if it doesn't exist
def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS tblFilms (
                            filmID INTEGER PRIMARY KEY,
                            title TEXT,
                            yearReleased INTEGER,
                            rating TEXT,
                            duration INTEGER,
                            genre TEXT
                        )''')
        connection.commit()
    except sqlite3.Error as e:
        print("Error creating table:", e)

# Function to add a record to the database
def add_record(connection, film):
    try:
        cursor = connection.cursor()
        cursor.execute('''INSERT INTO tblFilms (title, yearReleased, rating, duration, genre)
                          VALUES (?, ?, ?, ?, ?)''', film)
        connection.commit()
        print("Record added successfully.")
    except sqlite3.Error as e:
        print("Error adding record:", e)

# Function to delete a record from the database
def delete_record(connection, film_id):
    try:
        cursor = connection.cursor()
        cursor.execute('''DELETE FROM tblFilms WHERE filmID = ?''', (film_id,))
        connection.commit()
        print("Record deleted successfully.")
    except sqlite3.Error as e:
        print("Error deleting record:", e)

# Function to update a record in the database
def update_record(connection, film_id, field, new_value):
    try:
        cursor = connection.cursor()
        cursor.execute('''UPDATE tblFilms SET {} = ? WHERE filmID = ?'''.format(field), (new_value, film_id))
        connection.commit()
        print("Record updated successfully.")
    except sqlite3.Error as e:
        print("Error updating record:", e)

# Function to print all records in tblFilms
def print_all_records(connection):
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM tblFilms''')
        records = cursor.fetchall()
        if records:
            for record in records:
                print(record)
        else:
            print("No records found.")
    except sqlite3.Error as e:
        print("Error fetching records:", e)

# Function to print records based on specific criteria
# Function to print records based on specific criteria
def print_records_by_criteria(connection, criteria, value):
    try:
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM tblFilms WHERE {} = ?'''.format(criteria), (value,))
        records = cursor.fetchall()
        if records:
            for record in records:
                print(record)
        else:
            print("No records found for the given criteria.")
    except sqlite3.Error as e:
        print("Error fetching records:", e)



# Main function to run the application
def main():
    connection = connect_to_database()
    if connection:
        create_table(connection)
        print(connection)

        while True:
            print("\nOptions menu:")
            print("1. Add a record")
            print("2. Delete a record")
            print("3. Amend a record")
            print("4. Print all records")
            print("5. Print details of all films")
            print("6. Print all films of a particular genre")
            print("7. Print all films of a particular year")
            print("8. Print all films of a particular rating")
            print("9. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                film = (input("Enter title: "), int(input("Enter year released: ")),
                        input("Enter rating: "), int(input("Enter duration: ")),
                        input("Enter genre: "))
                add_record(connection, film)
            elif choice == '2':
                film_id = int(input("Enter the film ID to delete: "))
                delete_record(connection, film_id)
            elif choice == '3':
                film_id = int(input("Enter the film ID to update: "))
                field = input("Enter the field to update (title/yearReleased/rating/duration/genre): ")
                new_value = input("Enter the new value: ")
                update_record(connection, film_id, field, new_value)
            elif choice == '4':
                print_all_records(connection)
            elif choice == '5':
                print_all_records(connection)
            elif choice == '6':
                genre = input("Enter the genre to filter: ")
                print_records_by_criteria(connection, 'genre', genre)
            elif choice == '7':
                year = int(input("Enter the year to filter: "))
                print_records_by_criteria(connection, 'yearReleased', year)
            elif choice == '8':
                rating = input("Enter the rating to filter: ")
                print_records_by_criteria(connection, 'rating', rating)
            elif choice == '9':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

        connection.close()

if __name__ == "__main__":
    main()
