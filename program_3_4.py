# Write a program that creates a database named phonebook.db.
# The database should have a table named Entries, with columns for a person’s name
# and phone number.Next, write a CRUD application that lets the user add rows to
# # the Entries table, look up a person’s phone number, change a person’s phone number,
# # and delete specified rows.

import sqlite3

def main():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    phonebook_table = '''CREATE TABLE Entries(ID INTEGER PRIMARY KEY NOT NULL, name STRING, phone_number INTEGER)'''
    cur.execute(phonebook_table)

    rows = int(input('How many rows would you like: '))
    data = []

    for i in range(rows):
        primary_key = 1
        name = input("Enter name: ")
        phone = int(input('Enter phone number: '))
        tuple = (primary_key,name, phone)
        data.append(tuple)
        primary_key += 1


    for item in data:
        cur.executemany('INSERT INTO Entries(?,?,?)',data)

    search = str(input("Would you like to search for a phone number? "))
    if search == 'y' or 'yes':
        phone_number_search = int(input("Who's phone number are you looking for: "))
        cur.execute("search * from Entries where phone_number=:c", {'c':phone_number_search})
        phone_search = cur.fetchall()
        print(phone_search)
    else:
        pass

    phone_replace = str(input("Would you like to change a phone number? "))
    if phone_replace == 'y' or 'yes':
        phone_number_search = int(input("What phone number are you looking to change: "))
        new_number = int(input("Enter the new phone number: "))
        update = cur.execute('''UPDATE Entries
                            SET phone_number = ?
                            WHERE phone_number == ?''',
                                (new_number, phone_number_search))
    else:
        pass

    deletion = str(input("Would you like to delete any rows? "))
    if deletion == 'y' or 'yes':
        row_search = int(input("What row would you like to delete?: "))
        delete = cur.execute('''DELETE FROM Entries
                                     WHERE ID == ?''',
                                        (row_search))

    else:
        pass






    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

