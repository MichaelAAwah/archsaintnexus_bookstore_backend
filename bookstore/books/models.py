from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(null=True)
    release_date = models.DateField("date released")
    pub_date = models.DateField("date published")

    def __str__(self):
        return self.book_name