class Library:
    __book_list = []
    @classmethod
    def entry_book(self,book):
        self.__book_list.append(book)
    
    @classmethod
    def view_all_books(self):
        if not self.__book_list:
            print("not book available")
        else:
            for book in self.__book_list:
                book.view_book_info()
    @classmethod
    def find_book_by_id(self,id):
        for book in self.__book_list:
            if book.get_book_id() == id:
                return book
        return None
    
class Book:
    def __init__(self,book_id,title,author):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = True
        Library.entry_book(self)
    
    def borrow_book(self):
        if self.__availability: self.__availability = False
        else: print("This book already borrowing")
        
    def return_book(self):
        if not self.__availability:
            self.__availability = True
        else: print("this book not available in your home Right now this book inside my library.")
    
    def view_book_info(self):
        
        print(f"book id: {self.__book_id} , title : {self.__title} , author: {self.__author} , {'available' if self.__availability else 'Not available'}")
        
    def get_book_id(self):
        return self.__book_id
    
Book(101,"OOP","Jankar Mahbub") 
Book(102,"C++","Rahat khan Pathan") 
Book(103,"Competitive Programming","Rifat")

# menu bar:
while True:
    print("\n_______ Welcome to the Library ______")
    print("1. View All Books")
    print(f"2. Borrow book")
    print(f"3. Return book")
    print(f"4. Exit.\n")
    op = int(input("Select option: "))
    if op == 1:
        print("\nLibrary books: ")
        Library.view_all_books()
    elif op == 2:
        book_id = int(input("Enter your book ID: "))
        book = Library.find_book_by_id(book_id)
        if book: book.borrow_book()
        else: print("\ninvalid book id.")
    elif op == 3:
        book_id = int(input("Enter your book ID: "))
        book = Library.find_book_by_id(book_id)
        if book: book.return_book()
        else: print("\ninvalid book id.")
    elif op == 4:
        break
    else: print(f"You select {op} but this is not Valid Option.") 
        