from django.db import models

# Create your models here.

class DonationLinks(models.Model):
    link_name = models.CharField(max_length=500)
    link = models.URLField(max_length=1000)
    link_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.link_name + "- " + self.link