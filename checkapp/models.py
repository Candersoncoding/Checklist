from django.db import models
from logapp.models import User

class Item(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def return_JSON(self):
        return {'id': self.id, 'name': self.name}

class Checklist(models.Model):
    title = models.CharField(max_length=60)
    user = models.ForeignKey(User, related_name= 'checklists', on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name='checklists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)