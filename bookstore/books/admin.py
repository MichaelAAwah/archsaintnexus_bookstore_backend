from django.contrib import admin
from django.utils.html import format_html
from .models import Book
import cloudinary.uploader

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author', 'price', 'release_date', 'pub_date', 'image_preview')
    list_filter = ('author', 'release_date', 'pub_date')
    search_fields = ('book_name', 'author')
    readonly_fields = ('image_preview', 'image_url')  # Prevent manual input for image_url

    fieldsets = (
        ('Book Details', {
            'fields': ('book_name', 'author', 'price', 'release_date', 'pub_date')
        }),
        ('Book Cover', {
            'fields': ('image', 'image_preview')
        }),
    )

    def image_preview(self, obj):
        if obj.image_url:
            return format_html(f'<img src="{obj.image_url}" width="100" height="100" style="border-radius:5px;" />')
        return "(No Image)"
    image_preview.short_description = "Cover Image"

    def save_model(self, request, obj, form, change):
        """
        Override save_model to upload image to Cloudinary before saving the Book instance.
        """
        image = request.FILES.get('image')  # Get uploaded image

        if image:
            upload_result = cloudinary.uploader.upload(image)
            obj.image_url = upload_result.get('secure_url')  # Store Cloudinary URL

        super().save_model(request, obj, form, change)  # Save the book instance

admin.site.register(Book, BookAdmin)
