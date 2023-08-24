from django.db import models
from django.contrib.auth.models import User

class TestCase(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField()

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return f'/{self.slug}/'

class Question(models.Model):
	test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE, related_name='questions')
	title = models.CharField(max_length=255)
	def __str__(self):
		return self.title

class Option(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
	text = models.CharField(max_length=255)
	correct = models.BooleanField(null=False)

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	options = models.ManyToManyField(Option)

class Completed(models.Model):
	test_case = models.ForeignKey(TestCase, on_delete=models.CASCADE)
	answers = models.ManyToManyField(Answer)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	right_answers = models.IntegerField()
	wrong_answers = models.IntegerField()
	result = models.IntegerField()