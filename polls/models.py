from datetime import timedelta

from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    #models.Model is a subclass of a Question
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #'date published' is a first optiona argument of a Field class - humand readable name

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text