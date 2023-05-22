from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):

    name = models.CharField(
        'name', max_length = 30, db_index = True, null = False , blank = False, default='Max'
    )
    body = models.TextField(
        'body', max_length = 230, db_index = True, null = False , blank = False, default='tell us something Max'
    )
    created_at = models.DateTimeField(
        'created_at', db_index = True, null = True , blank = True, auto_now_add = True
    )
    image= CloudinaryField(
        'image', blank=True, db_index= True
    )
    like= models.IntegerField(
        null=True, blank= True, default=0
    )

    def __str__(self):
        return self.name