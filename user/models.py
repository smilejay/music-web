from django.db import models


class User(models.Model):
    openid = models.CharField(max_length=64, db_index=True)
    nickname = models.CharField(max_length=64, blank=True)
    gender = models.CharField(max_length=4, blank=True)
    figureurl = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=32, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'