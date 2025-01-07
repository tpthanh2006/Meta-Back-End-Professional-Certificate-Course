from django.db import models

# Create your models here.
class Employees(models.Model):
  first_name = models.CharField(max_length = 200)
  last_name = models.CharField(max_length = 200)
  role = models.CharField(max_length = 100)
  shift = models.IntegerField()

  def __str__(self):
    return self.first_name

'''class Booking(models.Model):
  first_name = models.CharField(max_length = 200)
  last_name = models.CharField(max_length = 200)
  guest_count = models.IntegerField()
  reservation_time = models.DateField(auto_now = True)
  comments = models.CharField(max_length = 1000)


class MenuCategory(models.Model):
  menu_category_name = models.CharField(max_length=200)

class Menu(models.Model):
  menu_item = models.CharField(max_length=200)
  price = models.IntegerField(null=False)
  category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)'''