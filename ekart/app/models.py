from django.conf import UserSettingsHolder
from django.db import models
from django.contrib.auth.models import User
import datetime
import os

#it returns filename with date and time
def getFileName(request,filename):
       n_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
       new_filename="%s%s"%(n_time,filename)
       return os.path.join('uploads/',new_filename)

class category(models.Model):
       name=models.CharField(max_length=150,null=False,blank=False)
       image=models.ImageField(upload_to=getFileName,null=True,blank=True)
       description=models.TextField(max_length=500,null=False,blank=False)
       status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
       created_at=models.DateTimeField(auto_now_add=True)
       def __str__(self):
              return self.name
class product(models.Model):
       category=models.ForeignKey(category,on_delete=models.CASCADE)
       name=models.CharField(max_length=150,null=False,blank=False)
       vendor=models.CharField(max_length=150,null=False,blank=False)
       product_image=models.ImageField(upload_to=getFileName,null=True,blank=True)
       quantity=models.IntegerField(null=False,blank=False)
       orginal_price=models.FloatField(null=False,blank=False)
       selling_price=models.FloatField(null=False,blank=False)
       description=models.TextField(max_length=500,null=False,blank=False)
       status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
       trending=models.BooleanField(default=False,help_text="0-show,1-Trending")
       created_at=models.DateTimeField(auto_now_add=True)
       def __str__(self):
              return self.name
class Cart(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  product=models.ForeignKey(product,on_delete=models.CASCADE)
  product_qty=models.IntegerField(null=False,blank=False)
  created_at=models.DateTimeField(auto_now_add=True)
  def total_cost(self):
    total=self.product_qty*self.product.selling_price
    return total
class favorite(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      product=models.ForeignKey(product,on_delete=models.CASCADE)
      created_at=models.DateTimeField(auto_now_add=True)
 