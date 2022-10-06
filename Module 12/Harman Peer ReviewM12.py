#Jessica Harman
#WhataBook
#CYBR410
#October 6, 2022
#Credit to: Professor Krasso


import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config) # connect to the whatabook database 
cursor = db.cursor()

class Whatabook: 
        def Welcome(): 
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
        def Show_meue():
            print("Please select item from menu with item number\n 1. View Books\n 2. View Store Locations\n 3. My Account\n 4. Exit")
        
        def show_books(): 
            cursor.execute("SELECT book_id, book_name, author, details from book;")
            books = cursor.fetchall()
            for book in books:
                print("Book ID: {}\n  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[0], book[1], book[2], book[3]))
            
        def show_locations():
            cursor.execute("SELECT store_id, locale from store;")
            stores = cursor.fetchall()
            for store in stores:
                    print(" Store ID: {}\n Local: {}\n".format(store[0], store[1]))
        #def validate_user():
            #WORKING STILL 
        #def show_acct_menu():
            #print("Please select item from menu with item number\n 1. View Wishlist\n 2. View Books to Add\n 3. Add Book to Wishlist\n 4. Exit"")
        #def show_wishlist():
            #userID = input()
            #crusor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = UPDATE WITH INPUT;")
            #user_wishlist = cursor.fetchall()
            #for whishlist in user_wishlist: 
                #print(" User ID: {}\n First Name: {}\n Last Name: {}\n Book ID: {}\n Book Name: {}\n Author: {}\n".format(wishlist[0], wishlist[1], wishlist[2]), wishlist[3] ")
        #def show_books_to_add():
            # crusor.execute("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = UPDATE WITH INPUT);") 
            #books_to_add = cursor.fetchall()
            #for book in books_to_add:
                #print("Book ID: {}\n Book Name: {}\n Author: {}\n Details: {}\n".format book[0],book[1],book[2],book[3])
        #def add_book_to_wishlist():
            #user_id_input = input("Please enter User ID to add book to: ")
            #book_id_input = input("Please enter Book ID to add to wishlist: ")
            #crusor.execute("INSERT INTO wishlist(user_id, book_id) VALUES(user_id_input, book_id_input)")
selection = None
Whatabook.Welcome()
while True:
    try:
        
        Whatabook.Show_meue()
        selcetion = int(input('Enter selection: '))
        if selcetion == 1:
             Whatabook.show_books()
        elif selcetion == 2:
             Whatabook.show_locations()
        elif selcetion == 3:
             print('Vaildate USER WORKING')
             #additional menu still working to put options for the following: def show_acct_menu():, def show_wishlist(): , def show_books_to_add():, def add_book_to_wishlist():
        elif selcetion == 4:
            print('Have a nice day')
            db.close()
            break
    except mysql.connector.Error as err:

        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The supplied username or password are invalid")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("  The specified database does not exist")

        else:
            print(err)


   
    #finally:
     #   print('Have a nice day')
     #   db.close()
     #   break

        

    
    
   







