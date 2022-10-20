from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    image = models.ImageField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField('Category name', max_length=200, help_text='Enter category')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='categories')

    def __str__(self):
        return f'{self.name} ({self.owner})'

    def get_absolute_url(self):
        return reverse('category', args=[str(self.id)])


class Note(models.Model):
    title = models.CharField('Title', max_length=200, help_text='Enter note title')
    text = models.CharField('Note text', max_length=1000, help_text='Enter note text')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='notes')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='notes')
    image = models.ImageField('Image', upload_to='images', null=True, blank=True)

    def __str__(self):
        return f'{self.title}, {self.category.name}, {self.owner}'

    def get_absolute_url(self):
        return reverse('note', args=[str(self.id)])
