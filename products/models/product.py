from django.db import models


class Category(models.Model):
    """ Maxsulotlar Turi """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    """ Maxsulotlar """
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def is_in_stock(self):
        """Omborda mahsulod bor bolsa True qaytaradi"""
        return self.stock > 0

    def reduce_stock(self, quantity):
        """ombordagi mahsulod yetarli bolsa uni ayradi va saqlaydi"""
        if quantity > self.stock:
            return False
        self.stock -= quantity
        self.save()
        return True

    def increase_stock(self, amount):
        """Omborga mahsulod qoshish"""
        self.stock += amount
        self.save()

    class Meta:
        """Mahsulodlarni name boyicha tartiblaydi"""
        ordering = ['name']
