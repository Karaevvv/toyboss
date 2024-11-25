# Generated by Django 5.1.2 on 2024-11-18 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_recipes_directions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='pizza_images/'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
