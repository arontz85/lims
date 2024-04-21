from django.shortcuts import render
#from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import book,reader,issuedBooks
#from .models import reader, book
#from .forms import *
from .forms import readerForm, bookForm, loginForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import auth
#from .decorators import allowed_users
#from django.contrib.auth import logout
# Create your views here.



@login_required(login_url="/accounts/login/")
def home(request):
    
    return render(request,'home.html',context={"current_tab": "home"})

#@login_required(login_url="/accounts/login/")
def welcome(request):
    return render(request,'welcome.html',context={"current_tab": "welcome"})


def logout_view(request):
    logout(request)
    messages.success(request, "You Loged out successfuly")
    return redirect('login')



# This function displays the list of issued books.
@login_required(login_url="/accounts/login/")
def view_issued_books(request):
    issued=issuedBooks.objects.all()
    return render(request,'view_issued_books.html',context={ "current_tab":"issued","issued":issued})

# This function is adding issued book into database table.
@login_required(login_url="/accounts/login/")
def save_issued_book(request):
    issuedbooks=issuedBooks(reader_details=request.POST['reader_details'],
                            book_details=request.POST['book_details'],
                            issue_date=request.POST['issueDate'],
                            due_date=request.POST['dueDate'], 
                            book_condition=request.POST['bookCondition'] )
    issuedbooks.save()
    messages.success(request, "Book issued successfuly")
    return redirect('/view_issued_books')
    
    

# This function is rendering the data in to the webpage.
@login_required(login_url="/accounts/login/")
def add_issued_book(request):
    loadReader=reader.objects.all()
    loadBook=book.objects.all()
    return render(request,'add_issued_book.html',context={"loadBook":loadBook,"loadReader":loadReader})

@login_required(login_url="/accounts/login/")    
def return_issued_book(request, pk):
     return_book=issuedBooks.objects.get(id=pk)
     return_book.delete()
     messages.success(request, "Book returned successfuly")
     return redirect('/view_issued_books')   

@login_required(login_url="/accounts/login/")      
def searched_issued_book(request):
    if request.method == 'POST':
        searched=request.POST['searched']
        IssuedBook=issuedBooks.objects.filter(reader_details__contains=searched)
    return render(request,'view_issued_books.html',context={"current_tab": "issued","IssuedBook":IssuedBook})   

@login_required(login_url="/accounts/login/")
def book_borrower(request):
    borrower=reader.objects.all()
    return render(request,'issue_book.html',context={"borrower":borrower})

@login_required(login_url="/accounts/login/")
def books(request):
    return render(request,'books.html',context={"current_tab": "books"})

@login_required(login_url="/accounts/login/")
def returns(request):
    return render(request,'returns.html',context={"current_tab": "returns"})

@login_required(login_url="/accounts/login/")
def shopping(request):
    return HttpResponse("Welcome to Shooping Center")

@login_required(login_url="/accounts/login/")
def save_student(request):
    student_name=request.POST['student_name']
    return render(request,'welcome.html',context={'student_name':student_name})

@login_required(login_url="/accounts/login/")
def readers_tab(request):
    readers=reader.objects.all()
    return render(request,'readers.html',context={"current_tab": "readers","readers":readers})

@login_required(login_url="/accounts/login/")
def books_tab(request):
    books=book.objects.all()
    return render(request,'books.html',context={"current_tab": "books","books":books})
    
@login_required(login_url="/accounts/login/")
def searched_values(request):
    if request.method == 'POST':
        searched=request.POST['searched']
        readers=reader.objects.filter(reader_name__contains=searched)
    return render(request,'readers.html',context={"current_tab": "readers","readers":readers})
   
@login_required(login_url="/accounts/login/")
def save_reader(request):
    reader_item=reader(reference_id=request.POST['reader_ref_id'],
                       reader_name=request.POST['reader_name'],
                       reader_contact=request.POST['reader_contact'],
                       reader_address=request.POST['address'],
                       guardian_name=request.POST['reader_guardian'],
                       reader_email=request.POST['reader_email'],
                       category=request.POST['category'],
                       active=True )
    reader_item.save()
    return redirect('/readers')

@login_required(login_url="/accounts/login/")
def searched_books(request):
    if request.method == 'POST':
        searched=request.POST['searched']
        books=book.objects.filter(book_title__contains=searched)
    return render(request,'books.html',context={"current_tab": "books","books":books})
   
@login_required(login_url="/accounts/login/")
def save_book(request):
    book_item=book( book_title=request.POST['book_title'],
                       author_name=request.POST['book_author'],
                       book_isbn=request.POST['book_isbn'],
                       book_description=request.POST['description'],
                       active=True )
    book_item.save()
    return redirect('/books')

@login_required(login_url="/accounts/login/")
def update_reader(request, pk):
    update_reader=reader.objects.get(id=pk)
    form = readerForm(instance=update_reader)
    if request.method=='POST':
        form=readerForm(request.POST, instance=update_reader)
        if form.is_valid():
            form.save()
            messages.success(request, "Reader's data has been updated")
            return redirect('/readers')
    context = {'form':form}
    return render(request,'update_reader.html',context)

@login_required(login_url="/accounts/login/")
def delete_reader(request, pk):
    delete_reader=reader.objects.get(id=pk)
    delete_reader.delete()
    return redirect('/readers')

@login_required(login_url="/accounts/login/") 
def update_book(request,pk):
    update_book=book.objects.get(id=pk)
    form = bookForm(instance=update_book)
    if request.method=='POST':
        form=bookForm(request.POST, instance=update_book)
        if form.is_valid():
            form.save()
            return redirect('/books')
    
    context = {'form':form}
    return render(request,'update_book.html',context)

@login_required(login_url="/accounts/login/")
def delete_book(request, pk):
    delete_book=book.objects.get(id=pk)
    delete_book.delete()
    return redirect('/books')
    

 