from django.contrib import admin
from .models import Tag, Post, Author
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display= ("first_name","last_name","email_address")

class PostAdmin(admin.ModelAdmin):
    list_display= ("title","date","author")
    list_filter= ("tags","author")
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Post,PostAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)