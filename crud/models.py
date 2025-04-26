from django.db import models
from django.contrib.auth.models import User
class Crud(models.Model):
    title=models.CharField(max_length=255)
    subTitle=models.CharField(max_length=255,blank=True,null=True)
    description=models.TextField()
    image=models.ImageField(upload_to='images',blank=True,null=True)
    author_id=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    created_at=models.DateTimeField( auto_now_add=True)