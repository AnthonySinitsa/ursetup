from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Setup(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def get_total_price(self):
    # method to calculate totla price of setup
    return sum(item.get_total_price() for item in self.items.all())