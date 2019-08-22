from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(verbose_name='상품명', max_length=256)
    price = models.IntegerField(verbose_name='상품가격')
    description = models.TextField(verbose_name='상품설명')
    stock = models.IntegerField(verbose_name='재고')
    register_date = models.DateTimeField(
        verbose_name='등록날짜', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fastcampus_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'
