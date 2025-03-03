from django.utils.text import slugify
from django.utils import timezone
from django.db.models.signals import pre_save
from django.db import models

# Create your models here.
class Region(models.Model):
    name =  models.CharField(unique=True, max_length=123)

    def __str__(self):
        return self.name

class Hospital(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='hospital')
    name = models.CharField(max_length=255,)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField()
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    opening_hours = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False, null=True, blank=True, max_length=225)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ImageHospital(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='hospital_image')
    image = models.ImageField(upload_to='hospital_logos/', blank=True, null=True)

    def __str__(self):
        return self.hospital.name

class Department(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=123)

    def __str__(self):
        return f"{self.hospital.name} --> ({self.name})"


class Doctor(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='doctors')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='doctors')
    name = models.CharField(max_length=123)
    specialty = models.CharField(max_length=123)
    phone = models.CharField(max_length=20, blank=True, null=True)
    opening_hours = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.name} --> {self.specialty}"



def blog_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name + " - " + timezone.now().strftime('%Y-%m-%d %H:%M:%S.%f'))


pre_save.connect(blog_pre_save, sender=Hospital)