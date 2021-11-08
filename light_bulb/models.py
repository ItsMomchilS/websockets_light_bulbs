from django.db import models


class LightBulbUser(models.Model):
    name = models.CharField(max_length=25)
    bulb_status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
