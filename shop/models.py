from django.db import models
from django.utils import timezone


class Order(models.Model):
    customer_name = models.CharField(max_length=150)
    item_bought = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateField()
    delivery_date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-order_date']

    def __str__(self):
        return f"{self.customer_name} – {self.item_bought} ({self.order_date})"

    @property
    def same_day(self):
        return self.order_date == self.delivery_date


class CrochetItem(models.Model):
    CATEGORY_CHOICES = [
        ('handwarmers', 'Handwarmers'),
        ('skirts', 'Skirts'),
        ('bouquets', 'Bouquets'),
    ]
    
    name = models.CharField(max_length=100) 
    description = models.TextField() 
    price = models.DecimalField(max_digits=6, decimal_places=2)  
    image = models.ImageField(upload_to='crochet_images/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='handwarmers')

    def __str__(self):
        return self.name