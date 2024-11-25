from django.db import models

from solo.models import SingletonModel

from django.core.validators import MinLengthValidator


class ProductCategory(models.Model):

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Категории товаров'
        verbose_name = 'Категория товара'

    def __str__(self):
        return self.name


class Product(models.Model):

    CATEGORY_CHOICES = [
        ('полукопченые', 'Полукопченые'),
        ('вареные', 'Вареные'),
        ('сэндвичи', 'Сэндвичи'),
    ]

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    categories = models.CharField(default=True, max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    consist = models.TextField(default=True, verbose_name='состав')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.name


class Publication(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()
    created_date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикация'


class Recipes(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    ingredients = models.TextField(default=True)
    directions = models.TextField(default=True)

    class Meta:
        verbose_name_plural = 'Рецепты'
        verbose_name = 'Рецепт'


class AboutCompany(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name_plural = 'О компании'
        verbose_name = 'Обо компании'


class SocialMediaContact(SingletonModel):
    instagram = models.URLField()
    facebook = models.URLField()
    phone_number = models.CharField(
        max_length=20, validators=[MinLengthValidator(7)],
    )

    class Meta:
        verbose_name_plural = 'Социальные сети и контакт'
        verbose_name = 'Социальные сети и контакт'

