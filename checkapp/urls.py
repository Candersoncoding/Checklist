from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.create_checklist),
    path('new_item/<int:checklist_id>', views.create_item),
    path('delete/<int:item_id>', views.destroy_item)
    
]