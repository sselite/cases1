from django.db import models



CATEGORY = [
    ('iPhone XR', 'iPhone XR'),
    ('iPhone 11', 'iPhone 11'),
    ('iPhone 12', 'iPhone 12'),
    ('iPhone 12 Pro', 'iPhone 12 Pro'),
    ('iPhone 12 Pro Max', 'iPhone 12 Pro Max'),
    ('iPhone 13', 'iPhone 13'),
    ('iPhone 13 Pro', 'iPhone 13 Pro'),
    ('iPhone 13 Pro Max', 'iPhone 13 Pro Max'),
]


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="products/")
    image2 = models.FileField(upload_to="products/")
    content = models.TextField()
    device = models.CharField(max_length=20, choices=CATEGORY, default="iPhone 11")
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    number = models.TextField()
    product_id = models.TextField()

    def __str__(self):
        return self.name