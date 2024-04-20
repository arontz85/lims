from django.contrib import admin
from .models import reader,book,issuedBooks
# Register your models here.

admin.site.register(reader)
admin.site.register(book)
admin.site.register(issuedBooks)