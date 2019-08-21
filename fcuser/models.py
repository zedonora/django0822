from django.db import models

# Create your models here.


class Fcuser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(verbose_name='비밀번호', max_length=64)
    register_date = models.DateTimeField(
        verbose_name='등록날짜', auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
