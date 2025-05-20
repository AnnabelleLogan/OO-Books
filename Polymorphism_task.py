Read through the Colab notebook carefully. You can run the blocks of Python code to see Polymorphism in action.
Complete the tasks listed at the end of the link after you have stepped through the demo code of Polymorphism.
Note: Once you have implemented Polymorphism in your codespace, ensure you commit and push your changes.


#Questions

1. What is object-oriented programming (OOP)?
A. A programming model based on the concept of classes and objects.

2. Which of the following is a fundamental concept of OOP?
B. Inheritance

3. What does ‘encapsulation’ refer to in OOP?
B. Bundling data with the methods that operate on that data.

4. Which term describes the concept of basing a new class on an existing class?
B. Inheritance

5. What is a class in OOP?
B. A blueprint from which objects are created.

6. What is an object in OOP?
A. A representation of an entity within a program.

7. What does polymorphism allow in OOP?
A. Objects to change their type.

8. Which OOP concept is characterised by hiding the internal state and requiring all
interaction to be performed through an object's methods?
B. Encapsulation

9. How does OOP contribute to software maintenance and reusability?
C. By facilitating code reuse through inheritance and polymorphism.

10. Which of the following best describes method overloading?
C. Defining multiple methods within a class with the same name but different
parameters.

11. Structure: Describe how the structure of the code is different between the two
approaches, particularly the handling of data and behaviour.

Procedural programming does not use classes whilst OOP programming does. They handle the data
differently in the sense that uses attributes and classes to handle data whilst the other seems to 
hide it under one variable. Behaviour-wise OOP handles it with methods whilst Procedural Programming
handles it with functions.

12. Scalability: Discuss how adding new features (like loaning a book) might be
implemented in each approach. Which approach seems more scalable and
maintainable?

I think it would be fairly easy to program as it is similar to the delete function, in simple it could
theoretically just have a name change and it would work, then perhaps a randomiser if necessary to say when
a book has returned. I believe with method would likely work in both.

13. Readability and organisation: Which code is more readable and easier to
understand? How does the organisation of code in each paradigm affect this?

I believe procedural programming is easier to read at first glance as you need some knowledge
to be able to dechipher OOP in python.

14. Modularity: In object-oriented programming, each book is an object with its own
properties and methods. How does this compare with the procedural approach in
terms of modularity and code reuse?

It seems that the functions and methods are different/ seperate to the objects. The objects are 
defined and are known whilst the methods dont have a connection to them besides when in use.

15. Data abstraction: Discuss how object-oriented programming provides better data
abstraction. For instance, if the internal representation of a book changes, how would
that affect each system?

If the internal representation of a book changed in Procedural programming then the system would likely
jam up. Whilst with OOP it is an easy fix with a new attribute.

#examples:

PROCEDURAL PROGRAMMING EXAMPLE (PYTHON)
library = [{"title": "To Kill a Mockingbird", "author": "Harper Lee", "copies": 3},
{"title": "1984", "author": "George Orwell", "copies": 5},
{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "copies": 2}]
def displayBooks(library):
for book in library:
print(f"Title: {book['title']}, Author: {book['author']}, Copies:
{book['copies']}")
def addBook(library, title, author, copies):
library.append({"title": title, "author": author, "copies": copies})
def removeBook(library, title):
global library
library = [book for book in library if book['title'] != title]
# Test functions
displayBooks(library)
addBook(library, "Harry Potter", "J.K. Rowling", 4)
removeBook(library, "1984")
displayBooks(library)


OBJECT-ORIENTED PROGRAMMING EXAMPLE (PYTHON)
class Book:
  def __init__(self, title, author, copies):
    self.title = title
    self.author = author
    self.copies = copies
class Library:
  def __init__(self):
    self.books = []
  def displayBooks(self):
    for book in self.books:
print(f"Title: {book.title}, Author: {book.author}, Copies: {book.copies}")
  def addBook(self, book):
    self.books.append(book)
  def removeBook(self, title):
    self.books = [book for book in self.books if book.title != title]
# Test the system
lib = Library()
lib.addBook(Book("To Kill a Mockingbird", "Harper Lee", 3))
lib.addBook(Book("1984", "George Orwell", 5))
lib.addBook(Book("The Great Gatsby", "F. Scott Fitzgerald", 2))
lib.displayBooks()
lib.addBook(Book("Harry Potter", "J.K. Rowling", 4))
lib.removeBook("1984")


