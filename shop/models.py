from django.db import models

class CrochetItem(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField() 
    price = models.DecimalField(max_digits=6, decimal_places=2)  
    image = models.ImageField(upload_to='crochet_images/')
    category = models.CharField(max_length=50, default='general')

    def __str__(self):
        return self.name