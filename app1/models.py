from django.db import models
from django.contrib.auth.models import User
import datetime

today = datetime.date.today()
# Create your models here.
class Category(models.Model):
    title = models.CharField( max_length=15 )
    content = models.CharField( max_length=500 )

    def __str__(self):
        return self.title

class Post(models.Model):

    Posttext = models.CharField( max_length=500 )
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    date_time = models.DateTimeField(default = datetime.datetime.now(), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.user.username+" "+str(today) 

