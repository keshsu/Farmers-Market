from django.db import models
from django.utils.timezone import datetime
from django.conf import settings
from django.shortcuts import reverse
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from datetime import date


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = User.username
    email = User.email

    def __str__(self):
        return self.customer.name


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category", null=True)
    featured = models.BooleanField(default=0)

    def __str__(self):
        return self.category_name


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(blank=False, max_length=100)
    website = models.CharField(blank=True, max_length=50)
    image = models.ImageField(upload_to="resturant", null=True)

    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @property
    def products(self):
        return Product.objects.filter(vendor=self.id).distinct()

@receiver(post_delete, sender=Vendor)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 


class Product(models.Model):
    dish_name = models.CharField(max_length=100)
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, null=True)
    price = models.FloatField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="product", null=True)
    description = models.TextField()
    popular = models.BooleanField(default=False)
    outofstock = models.BooleanField(default=False)

    def __str__(self):
        return self.dish_name

@receiver(post_delete, sender=Product)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blog", null=True)
    description = models.TextField(max_length=400)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
@receiver(post_delete, sender=Blog)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 


class Advertisement(models.Model):
    image = models.ImageField(upload_to="ads", null=True)
    adlink = models.CharField(max_length=200, blank=True, null=True)


@receiver(post_delete, sender=Advertisement)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 
class About(models.Model):
    image = models.ImageField(upload_to="about", null=True)
    descripttion = models.TextField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

@receiver(post_delete, sender=About)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 

class Order(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    # items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateField(default=date.today())
    phone = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    delivery_charge = models.FloatField(null=True)
    total = models.FloatField(null=True)
    item_length = models.IntegerField(null=True)
    status = models.CharField(max_length=100, default="Pending", null=True)
    remarks = models.TextField(null=True)
    complete = models.BooleanField(default=False)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([int(item.get_total) for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        # total = sum([item.quantity for item in orderitems])
        total = len([item for item in orderitems])
        return total


class OrderItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return f"{self.quantity} of {self.product.dish_name}"


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject


class userDetail(models.Model):
    orderu = models.OneToOneField(
        Order, on_delete=models.CASCADE, unique=True, default="")
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.phone


class CoverImage(models.Model):
    source = models.CharField(max_length=100)
    image = models.ImageField(upload_to="coverimage",null=True)
@receiver(post_delete, sender=CoverImage)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 

class MainCoverImage(models.Model):
    heading = models.TextField(null=True, blank= True)
    subheading = models.TextField(null=True, blank= True)
    image = models.ImageField(upload_to="maincoverimage/",null=True)
@receiver(post_delete, sender=MainCoverImage)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 

class IndexPageAbout(models.Model):
    bigimage = models.ImageField(upload_to="indexpageabout/bigimage/",null=True)
    smallimage = models.ImageField(upload_to="indexpageabout/smallimage/",null=True)
    heading = models.CharField(max_length=200)
    par_one = models.CharField(max_length=500)
    par_two = models.CharField(max_length=500)

@receiver(post_delete, sender=IndexPageAbout)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 


class Clients(models.Model):
    image = models.ImageField(upload_to="clients/",null=True)
    
@receiver(post_delete, sender=Clients)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="testimonials/")
    content = models.TextField()
    designation = models.CharField(max_length=100)
    display = models.BooleanField(default=False)

@receiver(post_delete, sender=Testimonial)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False) 
