from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    product_category = models.CharField(max_length=50, default='')
    product_subcategory = models.CharField(max_length=50, default='')
    product_desc = models.CharField(max_length=100)
    product_price = models.IntegerField(default=0)
    product_release_date = models.DateField()
    product_img = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return f'{self.product_name} ({self.product_category})'


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=50)
    contact_email = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=12)
    contact_description = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.contact_name} ({self.contact_email})'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_name = models.CharField(max_length=50)
    order_email = models.CharField(max_length=50)
    order_add = models.CharField(max_length=300)
    order_phone = models.CharField(max_length=12)
    order_city = models.CharField(max_length=50)
    order_state = models.CharField(max_length=50)
    order_pincode = models.IntegerField()
    order_items = models.CharField(max_length=5000)
    order_amount = models.IntegerField(default=0)

    def __str__(self):
        return f"Order ({self.order_id})"


class OrderTracker(models.Model):
    track_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default='')
    track_desc = models.CharField(max_length=5000)
    track_timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.track_desc[:10]}..."