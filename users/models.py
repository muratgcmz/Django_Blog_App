from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to = 'media/', default='media/indir.png' )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.username


# image resizer with pillow Profile modeline ait save methodunu override ile değiştirip büyük dosyaları küçültüyoruz, burada 200 pixele düşürdük
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path) 

        if img.height > 200 or img.width > 200:
            new_img = (200, 200)
            img.thumbnail(new_img)
            img.save(self.image.path)