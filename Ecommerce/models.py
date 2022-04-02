from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, related_name='book', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=15)
    pages = models.IntegerField()
    price = models.FloatField()
    stock = models.IntegerField()
    description = models.TextField()
    imgUrl = models.URLField()
    status = models.BooleanField(default=True)
    created_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_dt']

    def __str__(self):
        return self.title


class Product(models.Model):
    product_tag = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()
    created_dt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_dt']

    def __str__(self):
        return '{} {}'.format(self.product_tag, self.name)