# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.


class book():
    def __init__(self,title,author,genre)
        self.title = title
        self.author = author
        self.genre = genre

    def method1(self):
        return"Parent method 1"

class novel(book):
    def __init__(self,title, author, genre)
       super.()__init__(self,title,author)
       self.genre = genre

    def method2(self):
        return"Child method 2"



