from django.contrib import admin

# Register your models here.
from .models import Post, Picture #User, 

#admin.site.register(User)
admin.site.register(Post)
admin.site.register(Picture)