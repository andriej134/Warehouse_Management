from django.db import models

class Product(models.Model):
    SHAPE_CHOICES = [
        ('okrągły', 'Okrągły'),
        ('kwadratowy', 'Kwadratowy'),
        ('niestandardowy', 'Niestandardowy'),
    ]
    SIZE_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
    ]
    COLOR_CHOICES = [
        ('W', 'W'),
        ('B', 'B'),
        ('G', 'G'),
    ]

    DIAMETER_CHOICES = [
        ('100', '100'),
        ('125', '125'),
        ('160', '160'),
    ]





    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    diameter = models.DecimalField(max_digits=6, decimal_places=2)
    shape = models.CharField(max_length=20, choices=SHAPE_CHOICES)
    size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)

    

    def __str__(self):
        return f"{self.shape} {self.size} {self.color} ({self.diameter} mm)"

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    stock_level = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product.name} - {self.stock_level}"