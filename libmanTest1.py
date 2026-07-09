from library_managment import LibraryManagment, PremiumMember, StudentMember

# 1. Register Members
print("--- Creating Members ---")
alice = LibraryManagment("Alice", 2)
bob = PremiumMember("Bob")
charlie = StudentMember("Charlie")

# 2. Test standard borrowing and limit check
print("\n--- Alice's Borrowing ---")
alice.borrow_book("The Hobbit")
alice.borrow_book("1984")
alice.borrow_book("To Kill a Mockingbird") 
alice.show_books()

# 3. Test transferring books
print("\n--- Transferring Book ---")
alice.transfer_book("1984", bob)            
alice.show_books()
bob.show_books()

# 4. Test Student Member borrowing
print("\n--- Student Member Borrowing ---")
charlie.borrow_book("Python Basics")
charlie.show_books()