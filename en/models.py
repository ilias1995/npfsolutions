from __future__ import unicode_literals
from redactor.fields import RedactorField
from django.db import models


# Create your models here.


class FeedProducts(models.Model):
    feed_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    feed_image = models.ImageField(upload_to='feed_img/ru/')
    feed_info = RedactorField(verbose_name=u'Text', redactor_options={'lang': 'en', 'focus': True}, upload_to='tmp/',
                              allow_file_upload=True, allow_image_upload=True)

    def __unicode__(self):
        return self.feed_name


class Poultry(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='feed_img/ru/')
    info = RedactorField(verbose_name=u'Text', redactor_options={'lang': 'en', 'focus': True}, upload_to='tmp/',
                         allow_file_upload=True, allow_image_upload=True)

    def __unicode__(self):
        return self.name


class Distributor(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    place = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class DistributorShip(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    place = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name