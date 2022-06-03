from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
   
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    username = models.CharField(max_length=50, null=True, blank=True,)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to = 'media/', null=True, blank=True, default='/media/indir.png' )
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username


