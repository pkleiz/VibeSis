from django.db import models


class Categories(models.TextChoices):
    sale = 'SL', 'Sale'
    short = 'SH', 'Short'
    pants = 'CA', 'Calça'
    dress = 'VE', 'Vestido'
    skirt = 'SA', 'Saia'
    overalls = 'MA', 'Macação/Macaquinho'
    cropped = 'CR', 'Cropped'
    tshirt = 'CM', 'Camisa'
    body = 'BO', 'Body'
    jacketcoat = 'JA', 'Jaqueta/Casaco'
    set = 'CN', 'Conjunto'
    Accessories = 'AC', 'Acessórios',


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    categories = models.CharField(
        max_length=2,
        choices=Categories.choices,
        default=Categories.sale
    )
    color = models.CharField(max_length=20)
    quantity = models.IntegerField()
    size = models.CharField(max_length=2)
    description = models.TextField()
    image1 = models.ImageField(upload_to='products', null=True, blank=True)
    image2 = models.ImageField(upload_to='products', null=True, blank=True)
    image3 = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self):
        return self.name

    def full_name(self):
        return self.name + 'Cor: ' + self.color + 'Tamanho: ' + self.size

    full_name.admin_order_field = 'name'
