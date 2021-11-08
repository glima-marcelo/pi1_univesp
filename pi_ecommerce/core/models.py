from django.utils.text import slugify
from django.db import models
from django.urls import reverse


class Caracteristica(models.Model):
    code_charact = models.CharField(max_length=2, default='')
    description = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.description


class Item(models.Model):
    code_prod = models.CharField(max_length=25)
    name_prod = models.CharField(max_length=50)
    name_long = models.CharField(max_length=255)
    code_charact_fk = models.ForeignKey(Caracteristica, null=True, on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, default='')

    def __str__(self):
        return self.name_prod

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_prod)
        super(Item, self).save()

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.slug)])
