from django.forms import ModelForm
from django import forms
from .models import book,reader,issuedBooks
from django.contrib.auth.forms import AuthenticationForm
#from .views import *
from django.forms.widgets import TextInput,EmailInput
#from .models import reader, book
#from .forms import *

class bookForm(ModelForm):
    class Meta:
        model=book
        fields='__all__'

class readerForm(ModelForm):
    class Meta:
        model=reader
        fields='__all__'



class issuedBooksForm(ModelForm):
    class Meta:
       model = issuedBooks
       fields = '__all__'

class saveIssuedBooksForm(ModelForm):
    class Meta:
       model = reader
       fields = '__all__'

class loginForm(ModelForm):
    class Meta:
        model=reader
        fields=['category','reference_id','reader_email']
        
        

#class BookForm(forms.ModelForm):
 #   class Meta:
  #     model = Book
   #     fields = '__all__'
        
#class Book_instanceForm(forms.ModelForm):
 #   class Meta:
  #      model=BookInstance
   #     fields = ['book','book_number']

#class Book_IssueForm(forms.ModelForm):
  #  class Meta:
   #     model=Book_Issue
    #    exclude = ['issue_date', 'due_date','remarks_on_return','date_returned']