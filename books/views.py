from django.shortcuts import HttpResponse
from .models import Book, Author, Category

# Create your views here.
def books_view(request):
    books = Book.objects.all()
    response = ""

    for book in books:
        response += f"""
        <h2>{book.title}</h2>
    """
        response += f"""
        <ul>
            <li>Description: {book.description}</li>
            <li>Created at: {book.created_at}</li>
            <li>Updated at: {book.updated_at}</li>
            <li>Author: {book.author.first_name} {book.author.last_name}</li>
        </ul>
    """

    return HttpResponse(response)

def authors_view(request):
    authors = Author.objects.all()
    response = ""

    for author in authors:
        response += f"<h2>{author.first_name} {author.last_name}</h2>"
        response += "<ol>"
        for book in author.books_author.all():
            response += f"<li>{book.title}</li>"

        response += "</ol>"

    return HttpResponse(response)

def categories_view(request):
    categories = Category.objects.all()
    response = ""
    for category in categories:
        response += f"<h2>{category.name}</h2>"
        response += "<ol>"
        for book in category.books_category.all():
            response += f"<li>{book.title}</li>"
        response += "</ol>"

    return HttpResponse(response)