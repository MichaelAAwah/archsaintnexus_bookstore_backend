from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE)  # Links to the Django User model
    author = models.CharField(max_length=255)
    image = models.ImageField(upload_to='temp/', null=True, blank=True)  # Temporary local storage
    image_url = models.URLField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True)  # Set when first created
    updated_at = models.DateTimeField(auto_now=True)  # Updates every time the object changes

    def __str__(self):
        return self.title
