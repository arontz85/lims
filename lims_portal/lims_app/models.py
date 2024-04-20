from django.db import models
#from datetime import datetime,timedelta
#import uuid

class book(models.Model):
    book_title = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    book_isbn = models.CharField(max_length=200)
    book_description=models.TextField(max_length=500, help_text="Summary about the book",null=True,blank=True)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.book_title + '-'+ self.book_isbn
    

class reader(models.Model):
    reference_id = models.CharField(max_length=100,unique=True)
    reader_name = models.CharField(max_length=100)
    reader_contact = models.CharField(max_length=200)
    reader_address = models.CharField(max_length=100)
    guardian_name=models.CharField(max_length=100,help_text="parent/guardian name")
    reader_email=models.EmailField(max_length=100, help_text="Guardian/parent e-mail")
    reading=models.ManyToManyField(book, blank=True)
    category=models.CharField(max_length=100, help_text="Enter: Staff or Reader only")
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.reader_name

class issuedBooks(models.Model):
    reader_details = models.CharField(max_length=200)
    issue_date=models.DateField()
    due_date=models.DateField()
    book_details=models.CharField(max_length=200)
    book_condition=models.CharField(max_length=200, default='In good condition')
    def __str__(self):
        return self.reader_details


