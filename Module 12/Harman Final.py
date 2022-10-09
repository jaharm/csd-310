#Jessica Harman
#WhataBook
#CYBR410
#October 6, 2022
#Credit to: Professor Krasso
#Credit to: Daniel Clark


import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config) 
cursor = db.cursor()

 
def Welcome(): #Welcome with image
    print("Welcome to Whatabook")
    print("""\
                ,..........   ..........,
           ,..,'          '.'          ',..,
         ,' ,'            :            ', ',
       ,' ,'  WhatABook  :             ', ',
     ,' ,'              :              ', ',
   ,' ,'............., : ,.............', ',
 ,'  '............   '.'   ............'  ',
 '''''''''''''''''';''';''''''''''''''''''
                    ''' """)
def Show_meue(): #main login menu for user with options
    print("Please select item from menu with item number\n 1. View Books\n 2. View Store Locations\n 3. My Account\n 4. Exit")
   
def show_books(): #Option to pull list of books from what a book 
    cursor.execute("SELECT book_id, book_name, author, details from book;")
    books = cursor.fetchall()
    for book in books:
        print("Book ID: {}\n  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2], book[3]))
            
def show_locations(): #Shows locations for what a book from database
    cursor.execute("SELECT store_id, locale from store;")
    stores = cursor.fetchall()
    for store in stores:
            print(" Store ID: {}\n Local: {}\n".format(store[0], store[1]))

def validate_user():#Validates that a user exist between 1 and 3; couldn't figure out how to pull query from mysql db
    userID = int(input('\nEnter Account ID: \n'))
    if userID > 1 or userID <3:
        return userID
    else: 
        print("Invalid User ID, please try again\n")
        exit()
def show_account_menu(): #brings up the user account menu 
    try:
        print('\nAccount Menu\n')
        user_menu = int(input(' 1. Wishlist\n 2. Add Book\n 3. Main Menu\n'))
        if user_menu < 4 or user_menu > 0:
            return user_menu
        else:
            print("Incorrect input, please try again.")
            exit()
    except ValueError:
        print("Invalid Menu Selection, please try again")
        exit()
  
def show_wishlist(cursor, userID): #query for the users wishlist
    cursor.execute ("SELECT user.user_id, book.book_id, book.book_name, book.author FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = {}".format (userID))
    user_wishlist = cursor.fetchall()
    for book in user_wishlist: 
        print ("\n User ID:{}\n Book ID:{}\n Book Name: {}\n Author:".format(book[0], book[1], book[2]), book[3])

def show_books_to_add(cursor, userID): #query to show books not on the users wishlist 
    cursor.execute("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(userID))
    books_avaliable = cursor.fetchall()
    print('\nBooks Available to Add\n')
    for book in books_avaliable:
        print("Book ID: {}\n Book Name: {}\n Author: {}\n".format(book[0], book[1], book[2], book[3]))

def add_book(cursor,userID,book_id): #insert statement to add book to the users wishlist
    cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(userID, book_id))
#
def user_menu_access(): #def to pull up user menu
    user_acct_menu = True
    while user_acct_menu == True:
        userID = validate_user() #validates the user is between 1 and 3
        menu = show_account_menu() #shows the user account menu
        if menu == 1: #option 1 is for user wishlist 
            show_wishlist(cursor,userID) #option to show the user's wish list 
            continuing = input("Would you like to continue? (y or n):   ")
            if continuing.lower == 'y': #changed input to lowercase
                pass
            else:
                user_acct_menu = False
        elif menu == 2:
            show_books_to_add(cursor,userID) #shows books based on the user id and what is not listed on wishlist
            try:
                book_id = int(input("Enter the id of the book to add to your wishlist: \n")) #prompt to capture the user input for book id to add to list
                if book_id:
                    add_book(cursor, userID, book_id)
                    db.commit() #commit statement to update whatabook database
                    print('Book id: {} was successfully added to wishlist.\n'.format(book_id)) #validates the book was added
                    continuing = input("Would you like to continue? (y or n):   ") 
                    if continuing.lower == 'y':
                        pass
                    else:
                        user_acct_menu = False
            except ValueError:
                print("Input must contain all integers, please try again")
                exit()
        else:
            user_acct_menu = False 

user_selection = None

Welcome()
while True:
    try:
        
        Show_meue()
        user_selection = int(input('Enter selection: ')) #option input for main menu for all books, locations, and access to user menue
        if user_selection == 1:
             show_books()
        elif user_selection == 2:
             show_locations()
        elif user_selection == 3:
            user_menu_access() #def for user menu
        elif user_selection == 4:
            print('Have a nice day')
            db.close()
            break
    except mysql.connector.Error as err: #error statements for connection

        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The supplied username or password are invalid")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("  The specified database does not exist")

        else:
            print(err)
db.close()   #closing of the database connection