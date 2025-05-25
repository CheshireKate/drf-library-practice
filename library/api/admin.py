from django.contrib import admin

from library.api.books.models import Book, Author
from library.api.borrowings.models import Borrowing, ReturnBook
from library.api.users.models import User

admin.register(Book)
admin.register(Author)
admin.register(Borrowing)
admin.register(ReturnBook)
admin.register(User)

admin.register()
