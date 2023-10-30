from django.db import models

class UserAccount(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    outlook_access_token = models.TextField(blank=True, null=True)
    outlook_refresh_token = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email

