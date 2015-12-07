"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):

	name = models.CharField(max_length=30)
	description = models.TextField()
	user = models.ForeignKey(User)
	reputation = models.IntegerField(default=0)
	ct = models.DateTimeField(auto_now=True)
	class Meta:
		db_table = "tag"
	def __str__(self):
		return self.name	

class Question(models.Model):
	title = models.CharField(max_length=150)
	content = models.TextField()
	ct = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User)
	votes = models.IntegerField(default=0)
	answers = models.IntegerField(default=0)
	views = models.IntegerField(default=0)
	tags = models.ManyToManyField(Tag)
	class Meta:
		db_table = "question"
	def __str__(self):
		return self.title	

class Answer(models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	answer = models.TextField()
	votes = models.IntegerField(default=0)
	ct = models.DateTimeField(auto_now=True)
	class Meta:
		db_table = "answer"
	def __str__(self):
		return self.answer	

class Profile(models.Model):
	pic = models.CharField(max_length=100)
	reputation = models.IntegerField(default=0)
	user = models.ForeignKey(User)
	class Meta:
		db_table = "profile"