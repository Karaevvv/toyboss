# Generated by Django 5.1.2 on 2024-10-30 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_recipes_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='directions',
            field=models.TextField(default=True),
        ),
    ]
