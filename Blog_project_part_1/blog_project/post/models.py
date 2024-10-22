from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) 
    # A post can have multiple categories
    # Similarly a category can have multiple posts
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # To define One to Many / Many to One relationship
    # use models.ForeignKey
    # When author's profile is deleted, related post will also be deleted
    # Because of models.CASCADE

    def __str__(self):
        return self.title