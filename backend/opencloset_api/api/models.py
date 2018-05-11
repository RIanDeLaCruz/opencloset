from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=16)
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.username

class ItemSection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class ItemCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    EXTRA_EXTRA_SMALL = 'XXS'
    EXTRA_SMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    EXTRA_LARGE = 'XL'
    EXTRA_EXTRA_LARGE = 'XXL'
    EXTRA_EXTRA_EXTRA_LARGE = 'XXXL'
    FREE_SIZE = 'FS'

    SIZE_CHOICES = (
            (EXTRA_EXTRA_SMALL, EXTRA_EXTRA_SMALL),
            (EXTRA_SMALL, EXTRA_SMALL),
            (SMALL, SMALL),
            (MEDIUM, MEDIUM),
            (LARGE, LARGE),
            (EXTRA_LARGE, EXTRA_LARGE),
            (EXTRA_EXTRA_LARGE, EXTRA_EXTRA_LARGE),
            (EXTRA_EXTRA_EXTRA_LARGE, EXTRA_EXTRA_EXTRA_LARGE),
            (FREE_SIZE, FREE_SIZE)
    )

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.CharField(
        max_length=4,
        choices=SIZE_CHOICES,
        default=MEDIUM
    )
    brand = models.CharField(max_length=255)
    description = models.TextField()
    condition = models.TextField()
    picture = models.FileField(upload_to='uploads/')
    section = models.ForeignKey(
        'ItemSection',
        on_delete=models.CASCADE,
        related_name="items"
    )
    category = models.ForeignKey(
        'ItemCategory',
        on_delete=models.CASCADE,
        related_name='items'
    )
    tag = models.TextField(
        null=True,
        blank=True
    )
    lent_by = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='lent_item'
    )
    rented_by = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
        related_name='rented_item',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
