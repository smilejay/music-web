# -*- coding: utf-8 -*-
from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    singer = models.CharField(max_length=64, db_index=True)
    gender = models.CharField(max_length=4, blank=True, default='男', db_index=True)
    category = models.IntegerField()
    song_file = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'song'


class Category(models.Model):
    name = models.CharField(max_length=64, db_index=True)
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'category'
