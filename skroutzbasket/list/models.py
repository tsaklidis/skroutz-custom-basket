from django.db import models


class List(models.Model):
    name = models.CharField(max_length=255, default='', blank=False)
    items = models.ManyToManyField('list.item', blank=False)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=255, default='', blank=False)
    link = models.TextField(default='', blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)

    def __unicode__(self):
        return self.title
