from django.contrib import admin
from .models import Prefecture, Post, City, Occupation, Industry, Salary, Tag

admin.site.register(Post)
admin.site.register(Prefecture)
admin.site.register(City)
admin.site.register(Occupation)
admin.site.register(Industry)
admin.site.register(Salary)
admin.site.register(Tag)