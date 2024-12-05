# class Smartphone:
#     def __init__(self, brand, model, storage, color):
#         self.brand = brand
#         self.model = model
#         self.storage = storage
#         self.color = color
#         self.battery_level = 100

#     def make_call(self, number):
#         print(f"Calling {number}...")

#     def send_message(self, number, message):
#         print(f"Sending message to {number}: {message}")

#     def charge(self, minutes):
#         self.battery_level += minutes // 10

#     def check_battery(self):
#         print(f"Battery level: {self.battery_level}%")

# """
# Create a smartphone object
# """
# my_phone = Smartphone("Apple", "iPhone 12", 256, "Silver")
# my_phone.make_call("+2348164659374")
# my_phone.send_message("+2348164659374", "Hello, Ese! How are you today?")
# my_phone.charge(30)
# my_phone.check_battery()

class Book:
    def __init__(self, title, author, genre, publication_year, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.pages = pages

    def get_book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Pages: 1  {self.pages}")

# Create two book objects
book1 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 1960, 336)
book2 = Book("Pride and Prejudice", "Jane Austen", "Romance", 1813, 432)


book1.get_book_info()
book2.get_book_info()