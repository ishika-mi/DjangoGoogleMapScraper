from django.db import models

# Create your models here.
class LocationDetails(models.Model):
    search_text = models.CharField(max_length=225)
    business_title = models.CharField(max_length=255)
    address = models.TextField(null=True, blank=True)
    website = models.URLField(max_length=225,null=True, blank=True)
    phone_number = models.CharField(max_length=15,null=True, blank=True)

    class Meta:
        unique_together = ('business_title', 'address',)