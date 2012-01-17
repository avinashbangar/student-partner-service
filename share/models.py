from django.db import models

class Users(models.Model):
    """Model will include all users"""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    sex = models.BooleanField()
    mobile_number = models.CharField(max_length=255)
    fb_link = models.URLField(max_length=300)
    current_city = models.CharField(max_length=255)
    partner = models.BooleanField(default=0)
    exam_city = models.ForeignKey('City')
    exam_date = models.DateField(auto_now_add=False,auto_now=False)
    is_active = models.BooleanField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class City(models.Model):
    """Model will include all exam cities"""
    name = models.CharField(max_length=255)
    cf_1 = models.CharField(max_length=255)
    cf_2 = models.CharField(max_length=255)
    cf_3 = models.CharField(max_length=255)
    cf_4 = models.CharField(max_length=255)
    cf_5 = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Request(models.Model):
    requester = models.CharField(max_length=255)
    requested_to = models.CharField(max_length=255)
    is_active = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)