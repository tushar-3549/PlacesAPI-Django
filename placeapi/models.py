from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    profile_pic = models.ImageField(upload_to="profile_img", blank=True, null=True)

    def __str__(self):
        return self.username


class District(models.Model):
    name = models.CharField(max_length=100, unique=True)
    regex = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class SubDistrict(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="subdistricts")
    name = models.CharField(max_length=100)
    regex = models.CharField(max_length=255, blank=True)
    lat = models.FloatField(null=True, blank=True)
    long = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Union(models.Model):
    subdistrict = models.ForeignKey(SubDistrict, on_delete=models.CASCADE, related_name='unions')
    name = models.CharField(max_length=100)
    regex = models.CharField(max_length=255, blank=True)
    thana_no = models.IntegerField()
    lat = models.FloatField()
    long = models.FloatField()
    is_suggested = models.BooleanField(default=False)
    postcode = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class SemiMetroArea(models.Model):
    union = models.ForeignKey(Union, on_delete=models.CASCADE, related_name='semi_metros')
    name = models.CharField(max_length=100)
    regex = models.CharField(max_length=255, blank=True)
    lat = models.FloatField()
    long = models.FloatField()

    def __str__(self):
        return self.name