from django.db import models
#Отвечает за роботу с БД

#TODO: categories: samsung(smartphones), notebooks --> ACER, MacBook, Asus, Accessories --> Earphones, Powerbank

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(primary_key=True)
    parent = models.ForeignKey('self', blank = True, null = True, on_delete=models.CASCADE, related_name='children')

    def __str__(self) -> str:
        if self.parent:
            return f'{self.parent} --> {self.title}'
        return self.title

class Product(models.Model):
    STATUS_CHOICES = (
        ('in stock', 'In stock'),
        ('out of stock', 'Out of stock'),
        ('awaiting', 'Awaiting')
    )

    name = models.CharField(max_length=155)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='prod_images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'product_id': self.pk})

    def __str__(self):
        return self.name
