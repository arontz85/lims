"""
URL configuration for lims_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import home,books_tab,readers_tab,save_reader,save_student, delete_reader,book_borrower
from .views import searched_values,save_book,searched_books,searched_issued_book,returns,books,welcome
from .views import logout_view
#from .forms import bookForm,readerForm,issuedBooks,saveIssuedBooksForm
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('',welcome),
    path('home', home),
    #path('html',html),
    path('welcome',welcome),
    path('accounts/login',logout_view, name='logout'),
    path('readers', readers_tab),
    path('books', books_tab),
    path('save',save_student),
    path('readers/add', save_reader),
     path('readers/search', searched_values),
     path('books/add', save_book),
     path('books/search', searched_books),
     path('issuedbooks/search', searched_issued_book),
    
    #path('home', signin),
    #path('signout', views.signout, name='signout'),
     path('delete_reader', delete_reader),
     path('update_book/<str:pk>/', views.update_book, name ='update_book'),
     path('update_reader/<str:pk>/', views.update_reader, name ='update_reader'),
     path('delete_book/<str:pk>/', views.delete_book, name ='delete_book'),
     path('delete_reader/<str:pk>/', views.delete_reader, name ='delete_reader'),
     path('return_issued_book/<str:pk>/', views.return_issued_book, name ='return_issued_book'),
     path('save_issued_book', views.save_issued_book, name='save_issued_book'),
      path('add_issued_book', views.add_issued_book, name= 'add_issued_book'),
     #path('add_issued_book/<str:pk>/', views.add_issued_book, name= 'add_issued_book'),
     path('view_issued_books', views.view_issued_books, name= 'view_issued_books'),
     
     
    path('issue_book', book_borrower),
    
    path('books', books),
    path('returns', returns),
    #path('shop',shopping),

    #path('add_new_book_instance', views.add_new_book_instance, name='add_new_book_instance'),
   # path('add_book_issue', views.add_book_issue, name='book_issue'),
   
   # path('return_book/<int:id>',views.return_issued_book,name="return_issued_book"),
   # path('edit_issued/<int:id>',views.edit_issued,name="edit_issued"),
]
