from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


class User(AbstractUser):
    pass


class Habit(models.Model):
    name = models.CharField(max_length=200)
    goal = models.IntegerField()
    observers = models.ManyToManyField(
        User, blank=True, related_name='habits_i_am_observing')
    creator = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='habits_i_created')

    def __str__(self):
        return self.name


class Record(models.Model):
    date = models.DateField(default=date.today)
    number_completed = models.IntegerField()
    habit = models.ForeignKey(
        to="Habit", on_delete=models.CASCADE, blank=True, null=True, related_name='records')

    class Meta:
        unique_together = ['date', 'habit']
        ordering = ['-date']
