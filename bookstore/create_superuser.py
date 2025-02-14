import os
import django

# Ensure Django settings are loaded
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookstore.settings")
django.setup()

from django.contrib.auth import get_user_model

def create_superuser():
    User = get_user_model()
    username = os.getenv("DJANGO_SUPERUSER_USERNAME", "admin")
    email = os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@admin.com")
    password = os.getenv("DJANGO_SUPERUSER_PASSWORD", "admin")

    if not User.objects.filter(username=username).exists():
        print(f"🛠 Creating superuser: {username}")
        User.objects.create_superuser(username=username, email=email, password=password)
        print("✅ Superuser created successfully!")
    else:
        print("⚡ Superuser already exists.")

if __name__ == "__main__":
    create_superuser()
