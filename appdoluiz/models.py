from django.db import models

# Create your models here.


class GlobalProblem(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    ranking_80000_hours = models.IntegerField()
    pub_date = models.DateField()


class AIAlignmentSkill(models.Model):
    DIFFICULTY = [("F", "Fácil"), ("M", "Médio"), ("D", "Difícil")]
    LEARNING = [("A", "Autodidata"), ("T", "Trabalho"), ("F", "Faculdade")]

    title = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY)
    importance = models.IntegerField()
    how_to_learn = models.CharField(max_length=1, choices=LEARNING)
