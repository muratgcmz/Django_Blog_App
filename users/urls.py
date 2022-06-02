from django.urls import path
from .views import user_logout, user_login

urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='user_login'),
]