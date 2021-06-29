from django.db import models


class Question(models.Model):
    question_text = models.CharField(
        'questão',
        max_length=200,
    )
    pub_date = models.DateTimeField(
        'data de publicação',
    )


class Choide(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name='Questão',
        related_name='choices'  # eu coloquei
    )
    choice_text = models.CharField(
        'texto da escolha',
        max_length=200,
    )
    votes = models.IntegerField(
        'votos',
        default=0
    )
