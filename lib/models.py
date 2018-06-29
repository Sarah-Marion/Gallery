from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from pyuploadcare.dj.models import ImageField

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
    # craft = ImageField(blank=True, manual_crop="800x800")
    craft_upload = ImageField(blank=True, manual_crop="800x800")
    group = models.ForeignKey('LibGroup')

    def __str__(self):
        self.save()

    def publish(self):
        self.save()

    def get_absolute_url(self):
        return reverse('lib.views.craft_detail', args=[str(self.id)])


class Location(models.Model):
    location_name = models.CharField(max_length=150)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    
    @classmethod
    def update_location(cls, id, new_location):
        cls.objects.filter(id=id).update(location_name=new_location)


class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    
    @classmethod
    def update_category(cls, id, new_category):
        cls.objects.filter(id=id).update(category_name=new_category)

class Image(models.Model):
    image_name = models.CharField(max_length=100)
    # image_link = ImageField(blank=True, manual_crop="800x800")
    image_upload = ImageField(blank=True, manual_crop="800x800")
    image_description = models.TextField()
    image_location = models.ForeignKey(Location, null=True)
    image_category = models.ForeignKey(Category, null=True)
    image_time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_description

    class Meta:
        ordering=['image_name']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image_link=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def get_image_by_name(cls, name):
        images = cls.objects.filter(image_name__icontains=name).all()
        return images

    @classmethod
    def get_image_by_location(cls, location):
        images = Image.objects.filter(image_location__location_name=location)
        return images

    @classmethod
    def get_image_by_category(cls, category):
        images = cls.objects.filter(image_category__category_name__icontains=category).all()
        return images