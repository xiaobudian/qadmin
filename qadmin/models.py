"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	title = models.CharField(max_length=150)
	content = models.TextField()
	ct = models.DateTimeField(auto_now=True)
	uid = models.ForeignKey(User)
	class Meta:
		db_table = "question"
	def __str__(self):
		return self.title	