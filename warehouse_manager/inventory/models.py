from django.db import models

class Product(models.Model):
    KSZTALT_CHOICES = [
        ('okrągły', 'Okrągły'),
        ('kwadratowy', 'Kwadratowy'),
        ('niestandardowy', 'Niestandardowy'),
    ]
    ROZMIAR_CHOICES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
    ]
    
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    srednica = models.DecimalField(max_digits=6, decimal_places=2)
    ksztalt = models.CharField(max_length=20, choices=KSZTALT_CHOICES)
    rozmiar = models.CharField(max_length=2, choices=ROZMIAR_CHOICES)
    kolor = models.CharField(max_length=50)

    

    def __str__(self):
        return f"{self.ksztalt} {self.rozmiar} {self.kolor} ({self.srednica} mm)"

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