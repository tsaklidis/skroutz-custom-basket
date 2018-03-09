from django.core.validators import URLValidator
from django.db import models

from ..Utilities.unique.functions import get_random_string


class List(models.Model):
    name = models.CharField(unique=True, max_length=255,
                            default='', blank=True)

    token = models.CharField(max_length=17, blank=True)

    items = models.ManyToManyField('list.item', blank=True)

    def total_sum(self):
        total_sum = 0
        for item in self.items.all():
            total_sum = total_sum + item.price

        return '{0}'.format(total_sum)

    def save(self, *args, **kwargs):
        self.name = get_random_string(10)
        self.token = get_random_string(15, prefix='tk')
        super(List, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=255, default='', blank=False)

    link = models.TextField(validators=[URLValidator()])

    image_link = models.TextField(validators=[URLValidator()])

    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)

    def __unicode__(self):
        return self.title
