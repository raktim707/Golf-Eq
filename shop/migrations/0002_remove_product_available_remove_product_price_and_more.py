# Generated by Django 4.0.3 on 2022-06-13 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='available',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='faceAngle',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='hoselSetting',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='leftHand',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='lie',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='loft',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='offset',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='soleWidth',
            field=models.CharField(max_length=200, null=True),
        ),
    ]