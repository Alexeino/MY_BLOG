from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.core.validators import MinLengthValidator
# Create your models here.



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email_address = models.EmailField()


    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=30)
    image_name = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True,db_index=True) #db_index = True is automatically True for SlugFields...
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)


    def __str__(self):
        return f"{self.title}"
