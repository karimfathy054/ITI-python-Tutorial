from django.contrib.auth import validators
import uuid
from django.db.models import CASCADE
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models



def validate_category_name(value):
    if len(value) < 2:
        raise ValidationError("Category name must be at least 2 characters long.")
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True,validators=[validate_category_name])
    
    def __str__(self):
        return self.name
    
def validate_book_title(value):
    if len(value) < 2 or len(value) > 50:
        raise ValidationError("Book title must be between 2 and 50 characters.")
class Book(models.Model):
    title = models.CharField(max_length=50,validators=[validate_book_title])
    description = models.TextField()
    rate = models.DecimalField(max_digits=3,decimal_places=2)
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User,on_delete=CASCADE,related_name="books")
    categories = models.ManyToManyField(Category,related_name="books")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        permissions = [
            ('can_add_book', 'Can add book'),
            ('can_edit_book', 'Can edit book'),
            ('can_delete_book', 'Can delete book'),
        ]
    
class ISBN(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name="isbn")
    author_name = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    isbn_number = models.CharField(max_length=13, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.isbn_number:
            self.isbn_number = str(uuid.uuid4().int)[:13]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.isbn_number
    