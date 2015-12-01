"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):

	name = models.CharField(max_length=30)
	description = models.TextField()
	user = models.ForeignKey(User)
	class Meta:
		db_table = "tag"
	def __str__(self):
		return self.name	

class Question(models.Model):
	title = models.CharField(max_length=150)
	content = models.TextField()
	ct = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User)
	votes = models.IntegerField()
	answers = models.IntegerField()
	views = models.IntegerField()
	tags = models.ManyToManyField(Tag)
	class Meta:
		db_table = "question"
	def __str__(self):
		return self.title	

class Question_Answers(models.Model):
	user = models.ForeignKey(User)
	question = models.ForeignKey(Question)
	answer = models.TextField()
	votes = models.IntegerField()
	ct = models.DateTimeField(auto_now=True)
	class Meta:
		db_table = "question_answers"
	def __str__(self):
		return self.answer	