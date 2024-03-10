from django.db import models

from django.utils.html import mark_safe
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=100)
    image = models.ImageField(blank=True, )
    specifications = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.BooleanField(default=False)

    def get_percentage(self):
        new_price = (self.price/self.old_price) * 100
        return 100-new_price

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.title} - ${self.price} - {self.status}"
