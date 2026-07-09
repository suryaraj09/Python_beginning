class RentalLimitException(Exception):
    pass

class LibraryManagment:
    def __init__(self, name, max_books=3):
        self.name = name
        self.max_books = max_books
        self.books = []
        print(f"\nLibrary card for '{self.name}' created. Book limit = {self.max_books}\n")

    def show_books(self):
        print(f"Books currently borrowed by {self.name} = {self.books}")

    def check_limit(self):
        if len(self.books) >= self.max_books:
            raise RentalLimitException(f"Too many books. {self.name} can only have {self.max_books} books.")

    def borrow_book(self, book_title):
        try:
            self.check_limit()
            self.books.append(book_title)
            print(f"Book '{book_title}' has been borrowed by {self.name} successfully!!")
        except RentalLimitException as error:
            print(f"Borrowing failed: {error}")
    
    def return_book(self, book_title):
        try:
            self.books.remove(book_title)
            print(f"Book '{book_title}' has been returned by {self.name} successfully!!")
        except ValueError:
            print(f"Return failed: {self.name} does not have '{book_title}' borrowed.")

    def transfer_book(self, book_title, other_member):
        try:
            if book_title not in self.books:
                raise ValueError(f"{self.name} does not have '{book_title}' borrowed.")
            
            other_member.check_limit()
            
            self.books.remove(book_title)
            other_member.books.append(book_title)
            print(f"Book '{book_title}' transferred successfully from {self.name} to {other_member.name}!!")
        except (RentalLimitException, ValueError) as error:
            print(f"Transfer failed: {error}")

    
class PremiumMember(LibraryManagment):
    def __init__(self, name, max_books=6):
        super().__init__(name, max_books)

    def borrow_book(self, book_title):
        # Premium members get a special print message
        try:
            self.check_limit()
            self.books.append(book_title)
            print(f"Book '{book_title}' has been borrowed by Premium Member {self.name} successfully!! (Priority Pass)")
        except RentalLimitException as error:
            print(f"Borrowing failed: {error}")


class StudentMember(LibraryManagment):
    def __init__(self, name, max_books=5):
        super().__init__(name, max_books)
        self.fee = 0.50
    
    def borrow_book(self, book_title):
        try:
            self.check_limit()
            self.books.append(book_title)
            print(f"Book '{book_title}' has been borrowed by Student {self.name} (Processing fee of ${self.fee:.2f} applied).")
        except RentalLimitException as error:
            print(f"Borrowing failed: {error}")