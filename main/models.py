from django.db import models


class Question(models.Model):
    question = models.TextField(null=False)
    wiki_terms = models.CharField(max_length=200, null=False)
    wiki_text = models.TextField(null=False)
    answer = models.CharField(max_length=250)
    prediction_score = models.FloatField(default=0)

