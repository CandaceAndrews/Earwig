from django import forms
from .models import Habit, Record, User


class HabitForm(forms.ModelForm):

    class Meta:
        model = Habit
        fields = ('name', 'goal', 'observers')


class RecordForm(forms.ModelForm):

    class Meta:
        model = Record
        fields = ('date', 'number_completed')


class ObserverForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username',)
