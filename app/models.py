from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
	name = models.CharField(unique=True,max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	location = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return self.name
class slides(models.Model):
	name=models.CharField(unique=True,max_length=200, null=True)
	img = models.ImageField(upload_to='prod/')
	desc=models.TextField(null=True)

class Category(models.Model):
	name = models.CharField(unique=True,max_length=200, null=True)
	img = models.ImageField(upload_to='catg/',max_length=200, null=True)
	desc=models.TextField(null=True)
	def __str__(self):
		return self.name
class Seller(models.Model):
	name = models.CharField(unique=True,max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	location = models.CharField(max_length=200, null=True)
	category=models.ForeignKey(Category, null=True, on_delete= models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	seller = models.ForeignKey(Seller, null=True, on_delete= models.CASCADE)
	img = models.ImageField(upload_to='prod/')
	category = models.ForeignKey(Category, null=True, on_delete= models.CASCADE)
	def __str__(self):
		return self.name

class Cart(models.Model):
	customer = models.ForeignKey(Customer, null=True, on_delete= models.CASCADE)
	product = models.ForeignKey(Product, null=True, on_delete= models.CASCADE)
	def __str__(self):
		return self.product.name

class Order(models.Model):
	STATUS = (('Pending', 'Pending'),('Out for delivery', 'Out for delivery'),('Delivered', 'Delivered'),)
	customer = models.ForeignKey(Customer, null=True, on_delete= models.CASCADE)
	product = models.ForeignKey(Product, null=True, on_delete= models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	seller = models.ForeignKey(Seller, null=True, on_delete= models.CASCADE)
	address= models.CharField(max_length=200,null=True)
	def __str__(self):
		return self.product.name