from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Review(models.Model):
    text = models.CharField(max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return self.text
