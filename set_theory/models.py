from django.db import models

class InstagramAccount(models.Model):
    account_handle = models.CharField('Account handle', max_length=30)
    cat = models.BooleanField(default=False)
    dog = models.BooleanField(default=False)