# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserDemo(models.Model):
	name = models.CharField(max_length=100)
	phone = models.BigIntegerField()
	email = models.EmailField(max_length=254)

	def __str__(self):
		return self.name
