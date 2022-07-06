from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.CharField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    image_url = models.URLField(max_length=350, null=True)
    description = models.TextField(blank=True)
    hoselSetting = models.CharField(max_length=200, blank=True)
    cg = models.IntegerField(null=True)
    loft = models.FloatField(null=True)
    lie = models.FloatField(null=True)
    faceAngle= models.FloatField(null=True)
    offset = models.CharField(max_length=200, blank=True)
    soleWidth = models.CharField(max_length=200, null=True)
    brand = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    leftHand = models.BooleanField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated =  models.DateTimeField(auto_now=True)
    amazon_link = models.URLField(null=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])


class MyDashApp(models.Model):
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=350, null=True)
    def __str__(self):
        return self.name