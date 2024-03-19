from django.db import models
from django.contrib.auth.models import User
from charta_management import models as charta_management_models


class SavedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='saved_books')
    book = models.ForeignKey(charta_management_models.Book, on_delete=models.CASCADE, related_name='saved_by_users')

    def __str__(self):
        return f"{self.user.username}'s Saved Book: {self.book.title}"


class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(charta_management_models.Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()

    class Meta:
        # Define unique together constraint
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} rated {self.book.title} {self.rating}"