from django.urls import path
from .views import user_logout, user_login, register, profile
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('login/', user_login, name='user_login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)