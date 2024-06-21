
from books.views import book_list, export_books_csv, export_books_pdf
from django.urls import path

urlpatterns = [path('export/csv/', export_books_csv, name='export_books_csv'), 
            path('export/pdf/', export_books_pdf, name='export_books_pdf'),
            path('book-list/',book_list,name= "book_list"),
]

