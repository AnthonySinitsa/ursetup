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
  
class Item(models.Model):
  setup = models.ForeignKey(Setup, related_name='items', on_delete=models.CASCADE)
  title = models.CharField(max_length=200)
  description = models.TextField()
  url = models.URLField()
  image = models.ImageField(upload_to='item_images/')
  quantity = models.PositiveIntegerField(default=1)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  
  def get_total_price(self):
    # method calculate total price for this item (price * quantity)
    return self.price * self.quantity