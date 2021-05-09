from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.db import models
import random
from django.utils.translation import gettext_lazy as _



class Users(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("الاسم"))

    address = models.CharField(max_length=200, null=True, blank=True, verbose_name=_("العنوان"))
    bio = models.TextField(null=True, blank=True, verbose_name='نبذة عن المريض')
    phone = models.BigIntegerField(verbose_name=_('رقم الهاتف'))

    code = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = _('المستخدمين')
        verbose_name_plural = _('المستخدمين')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.code = random.randint(0, 999999)
        super().save(*args, **kwargs)


class Libs(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('الاسم'))
    address = models.CharField(max_length=200, verbose_name=_('العنوان'))
    bio = models.TextField(null=True, blank=True, verbose_name=_('نبذة عن المختبر'))
    phone = models.BigIntegerField(verbose_name=_('رقم الهاتف'))
    code = models.IntegerField(null=True, blank=True)


    class Meta:
        verbose_name = _('المختبرات')
        verbose_name_plural = _('المختبرات')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.code = random.randint(0, 999999)
        super().save(*args, **kwargs)


class Reports(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name=_('المستخدم'))
    lib = models.ForeignKey(Libs, on_delete=models.CASCADE, verbose_name=_('المختبر'))
    file = models.FileField(upload_to="uploads/%Y/%m/%d/%s/%M", verbose_name=_('الملف'))
    name = models.CharField(max_length=200, verbose_name=_('عنوان التقرير'))
    data = models.DateField(auto_now=True)

    class Meta:
        verbose_name = _('التقارير')
        verbose_name_plural = _('التقارير')

    def __str__(self):
        return self.name


class Offer(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('العنوان'))
    descrp = models.TextField(verbose_name=_('الوصف'))
    price = models.FloatField(verbose_name=_('السعر'))
    image = models.ImageField(upload_to="uploads/%Y/%m/%d/%s/%M", verbose_name=_('الصورة'))
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = _('العروض')
        verbose_name_plural = _('العروض')

    def __str__(self):
        return self.title


GENDER = (
    ('ذكر', 'ذكر'),
    ('انثى', 'انثى'),
)


class Registers(models.Model):
    offer = models.ForeignKey(Offer, on_delete=models.DO_NOTHING, verbose_name=_('العرض'))
    firstname = models.CharField(max_length=200, verbose_name=_('الاسم الاول'))
    lasttname = models.CharField(max_length=200, verbose_name=_('الاسم الاخير'))
    phone = models.BigIntegerField(verbose_name=_('رقم الهاتف'))
    email = models.CharField(max_length=200, verbose_name=_('البريد الالكتروني'))
    address = models.CharField(max_length=200, verbose_name=_('العنوان'))
    gender = models.CharField(max_length=200, choices=GENDER, default='ذكر', verbose_name=_('الجنس'))

    class Meta:
        verbose_name = _('الحجوزات')
        verbose_name_plural = _('الحجوزات')

    def __str__(self):
        return self.firstname



@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)




