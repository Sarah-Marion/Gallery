from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# Create your models here.

class LibGroup(models.Model):

    title = models.CharField(max_length=30, default='')
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(LibGroup, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('lib.views.lib_detail', args=[str(self.id)])



class Technique(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    published_date = models.DateTimeField(blank=True)
    craft = models.ImageField(upload_to="craft")
    group = models.ForeignKey('LibGroup')

    def __str__(self):
        self.save()

    def publish(self):
        self.save()

    def get_absolute_url(self):
        return reverse('lib.views.craft_detail', args=[str(self.id)])

    
