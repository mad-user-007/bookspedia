from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from django.utils import timezone
import pytz


# Create your views here.
def book_view(request, book_id):

    try:
        book = Book.objects.filter(id=book_id)[0]
    except:
        book = None

    context = {
        'book': book,
    }
    return render(request, 'catalog/book_view.html', context)


def home(request):
    books = Book.objects.all()
    recent_books = Book.objects.order_by('pub_date')[:10]
    context = {
        'books': books,
        'recent_books': recent_books,
    }


    return render(request, 'catalog/index.html', context)


def about_us(request):
    return render(request, 'catalog/about_us.html')


def add_book(request):
    return render(request, 'catalog/add_book.html')

def contact_us(request):
    return render(request, 'catalog/contact_us.html')


def report(request):
    return render(request, 'catalog/report.html')