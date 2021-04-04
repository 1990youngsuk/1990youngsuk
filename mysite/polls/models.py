import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

'''
class Survey(models.Model):
    survey_title = models.CharField(max_length=100, default="Title")
    survey_description = models.CharField(max_length=500, default="Description")
    survey_reward = models.IntegerField(default=500)
    survey_created_at = models.DateTimeField(auto_now_add=True, null=True)
    survey_updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def when_posted(self):
        now = timezone.now()
        return now
    
    def __str__(self):
        return self.survey_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.survey_created_at <= now
    was_published_recently.admin_order_field = 'survey_created_at'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
'''


class Question(models.Model):
    #survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "%s: %i" % (self.choice_text, self.votes)


'''
class Survey(models.Model):
    survey_title = models.CharField(max_length=100, default="Title")
    survey_description = models.CharField(
        max_length=500, default="Description")
    survey_reward = models.IntegerField(default=500)
    
    def when_posted(self):
        now = timezone.now()
        return now
    
    def __str__(self):
        return self.survey_title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Question(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
'''
