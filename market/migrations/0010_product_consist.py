# Generated by Django 5.1.2 on 2024-11-19 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0009_product_categories_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='consist',
            field=models.TextField(default=True, verbose_name='состав'),
        ),
    ]
