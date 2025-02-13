# Generated by Django 5.1.2 on 2024-11-18 13:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_alter_product_category_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.CharField(choices=[('полукопченые', 'Полукопченые'), ('вареные', 'Вареные'), ('сэндвичи', 'Сэндвичи')], default=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='market.productcategory'),
        ),
    ]
