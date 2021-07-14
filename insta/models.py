from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    image=models.FileField(upload_to='posts',blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    # def __str__(self):
    #     return self.description
    
    @property
    def username(self):
        return self.user.username