from django.db import models
from django.contrib.auth.models import User


Type_Choice = [
    ('C','Cheap'),
    ('A','Average'),
    ('E','Expensive'),
]

# Create your models here.
class Rental(models.Model):
  name = models.CharField(max_length=100)
  img = models.ImageField(upload_to='pics')
  desc = models.TextField()
  price = models.IntegerField()
  type = models.CharField(max_length=1,choices=Type_Choice,blank=True,null=True)
  dt = models.DateTimeField(auto_now_add=True, blank=True)
  reg_agent = models.ForeignKey(User,on_delete=models.CASCADE)


  def __str__(self):
    return self.name