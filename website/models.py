from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/item_images', default='media/item_images/item_default.webp',)
    
    def __str__(self):
        return f"{self.user.username} profile"