from django.contrib import admin
from .models import Book, Author, Category

class BookInlineTc(admin.TabularInline):
    model = Book.categories.through
    extra = 1

class BookInline(admin.TabularInline):
    model = Book
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [BookInlineTc]
    exclude = ('books', )
    list_display = ('name', )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories', )
    list_display = ('title', 'author')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    list_display = ('first_name', 'last_name')