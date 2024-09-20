from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_view),
    path('authors/', views.authors_view),
    path('categories/', views.categories_view),
]