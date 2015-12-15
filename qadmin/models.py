"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):

	name 		= models.CharField(max_length=30)
	desc 		= models.TextField(null=True)
	user 		= models.ForeignKey(User)
	reputation 	= models.IntegerField(default=0)
	ct 			= models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "tag"

	def __str__(self):
		return self.name	

class Question(models.Model):
	title 		= models.CharField(max_length=150)
	content 	= models.TextField()
	ct 			= models.DateTimeField(auto_now=True)
	user 		= models.ForeignKey(User)
	votes 		= models.IntegerField(default=0)
	answers 	= models.IntegerField(default=0)
	views 		= models.IntegerField(default=0)
	tags 		= models.ManyToManyField(Tag)
	favorite 	= models.IntegerField(default=0)

 	class Meta:
		db_table = "question"

	def __str__(self):
		return self.title	

class Question_Vote(models.Model):
	user 		= models.ForeignKey(User)
	question 	= models.ForeignKey(Question)
	ct 			= models.DateTimeField(auto_now=True)
	vote_type 	= models.IntegerField(null=False)

	class Meta:
		unique_together = (("user", "question"),)
		db_table = "qvote"

class Answer(models.Model):
	user 		= models.ForeignKey(User)
	question 	= models.ForeignKey(Question)
	answer 		= models.TextField()
	votes 		= models.IntegerField(default=0)
	ct 			= models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "answer"

	def __str__(self):
		return self.answer

class Answer_Vote(models.Model):
	user 		= models.ForeignKey(User)
	answer 	= models.ForeignKey(Answer)
	ct 			= models.DateTimeField(auto_now=True)
	vote_type 	= models.IntegerField(null=False)

	class Meta:
		unique_together = (("user", "answer"),)
		db_table = "avote"

class Favorite_Question(models.Model):
	user 		= models.ForeignKey(User)
	question 	= models.ForeignKey(Question)
	ct 			= models.DateTimeField(auto_now=True)

	class Meta:
		db_table = "fquestion"
		unique_together = (("user", "question"),)

	

class Profile(models.Model):
	pic 		= models.CharField(max_length=100)
	reputation 	= models.IntegerField(default=0)
	user 		= models.ForeignKey(User)
	location 	= models.CharField(max_length=100,null=True)
	aboutme 	= models.CharField(max_length=500,null=True)
	realname 	= models.CharField(max_length=50,null=True)
	birthday 	= models.DateTimeField(blank=True,null=True)

	class Meta:
		db_table = "profile"