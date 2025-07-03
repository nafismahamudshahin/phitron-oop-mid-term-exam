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