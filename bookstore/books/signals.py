from django.db.models.signals import post_save
from django.dispatch import receiver
from books.models import Book, ISBN

@receiver(post_save, sender=Book)
def create_isbn(sender, instance, created, **kwargs):
    if created:
        ISBN.objects.create(
            book=instance,
            author_name="Unknown Author",
            book_title=instance.title
        )