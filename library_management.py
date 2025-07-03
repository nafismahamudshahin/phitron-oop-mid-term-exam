class Library:
    __book_list = []
    @classmethod
    def entry_book(self,book):
        self.__book_list.append(book)
        
class Book:
    def __init__(self,book_id,title,author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        Library.entry_book(self)
    
    def borrow_book(self):
        if self.__availability:
            self.__availability = False
        else: print("This book already borrowing")
    def return_book(self):
        if not self.__availability:
            self.__availability = True
        else: print("this book not available in your hoom Right now this book inside my library.")
    
# Book(101,"computer office application","Lutfor Rahaman") 
# Book(102,"computer office application","Lutfor Rahaman") 
# Book(103,"computer office application","Lutfor Rahaman") 
        