# Generated by Django 4.0.3 on 2022-06-13 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_image_url_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cg',
            field=models.IntegerField(null=True),
        ),
    ]
