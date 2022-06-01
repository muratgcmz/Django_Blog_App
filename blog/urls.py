from .views import post_list, post_create, post_update
from django.urls import path

urlpatterns = [
    path('', post_list, name='home'),
    path('create/', post_create, name='create'),
    path('update/<int:id>', post_update, name='update'),
    
]