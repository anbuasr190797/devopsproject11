from django.contrib import admin
from .models import User, Admin, Book_ground

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Book_ground)
