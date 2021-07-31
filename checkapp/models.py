from django.db import models
from logapp.models import User

class ItemManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['name']) < 2 or len(post_data['name']) > 40:
            errors['name'] = 'Checklist item should be 2 to 40 characters in length.'

        return errors

class Item(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()

    def return_JSON(self):
        return {'id': self.id, 'name': self.name}
    
class ChecklistManager(models.Manager):

    def basic_validator(self, post_data):
        errors = {}

        if len(post_data['title']) < 2 or len(post_data['title']) > 40:
            errors['title'] = 'Checklist title should be 2 to 40 characters in length.'

        return errors

class Checklist(models.Model):
    title = models.CharField(max_length=40)
    user = models.ForeignKey(User, related_name= 'checklists', on_delete=models.CASCADE)
    items = models.ManyToManyField(Item, related_name='checklists')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ChecklistManager()