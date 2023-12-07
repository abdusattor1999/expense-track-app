from django.contrib import admin
from .models import Book, BookCategory, Publisher, Expanse


admin.site.register(Book)
admin.site.register(BookCategory)
admin.site.register(Publisher)
admin.site.register(Expanse)