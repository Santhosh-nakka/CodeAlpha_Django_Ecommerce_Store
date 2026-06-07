from django.db import models


class Product(models.Model):

    CATEGORY_CHOICES = (
        ('Mobile', 'Mobile'),
        ('Laptop', 'Laptop'),
        ('Accessory', 'Accessory'),
        ('Shirt', 'Shirt'),
        ('Shoes', 'Shoes'),
        ('Watch', 'Watch'),
        ('Toy', 'Toy'),
        ('Sports', 'Sports'),
        ('Book', 'Book'),
        ('Gaming', 'Gaming'),
        ('Fitness', 'Fitness'),
        ('Furniture', 'Furniture'),
    )

    name = models.CharField(max_length=200)

    price = models.IntegerField()

    description = models.TextField()

    image = models.ImageField(
        upload_to='products/',
        blank=True,
        null=True
    )

    image_url = models.URLField(
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    stock = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Order(models.Model):

    customer_name = models.CharField(
        max_length=100,
        default="Unknown"
    )

    customer_email = models.EmailField(
        default="unknown@example.com"
    )

    customer_phone = models.CharField(
        max_length=15,
        default="0000000000"
    )

    customer_address = models.TextField(
        default="Unknown"
    )

    total_price = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order #{self.id}"

class Review(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    name = models.CharField(max_length=100)

    rating = models.IntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.product.name} - {self.name}"