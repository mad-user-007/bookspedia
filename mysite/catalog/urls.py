from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('book/<int:book_id>/', views.book_view, name="book_view"),
    path('home/', views.home, name="home"),
    path('add/', views.add_book, name="add_book"),
    path('contact/', views.contact_us, name="contact"),
    path('about/', views.about_us, name="about"),
    path('report/', views.report, name="report"),
]
