import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(
        'questão',
        max_length=200,
    )
    pub_date = models.DateTimeField(
        'data de publicação',
    )

    def __str__(self) -> str:
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Questão',
        related_name='choices'  # eu coloquei - o padrão é choice_set
    )
    choice_text = models.CharField(
        'texto da escolha',
        max_length=200,
    )
    votes = models.IntegerField(
        'votos',
        default=0
    )

    def __str__(self) -> str:
        return self.choice_text
