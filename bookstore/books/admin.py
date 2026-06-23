from books.models import Book,Category,ISBN
from django.contrib import admin

# Register your models here.

class ISBN_inline(admin.StackedInline):
    model = ISBN
    can_delete = False
    extra=0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at")
    list_filter = ("categories", "user", "created_at")
    search_fields = ("title","isbn__isbn_number")

    inlines = [ISBN_inline]
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    
