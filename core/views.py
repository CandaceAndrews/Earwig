from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit, Record
from .forms import HabitForm, RecordForm, ObserverForm
from django.contrib.auth.decorators import login_required, user_passes_test


@login_required
def view_habits(request):
    user = request.user
    return render(request, 'core/index.html', {'user': user})


def add_habit(request):
    if request.method == 'POST':
        # form filled with info provided in post request
        habit = HabitForm(request.POST)
        if habit.is_valid():
            new_habit = habit.save(commit=False)
            new_habit.creator_id = request.user.id
            new_habit.save()
            return redirect('home')
        # empty form for .html
    form = HabitForm()
    return render(request, 'core/add_habit.html', {'form': form})


def view_habit_details(request, pk):
    habit = get_object_or_404(Habit, pk=pk)
    return render(request, 'core/habit_details.html', {'habit': habit})


def add_record(request, habit_pk):
    habit = get_object_or_404(Habit, pk=habit_pk)
    if request.method == "POST":
        record_form = RecordForm(request.POST)
        if record_form.is_valid():
            new_record = record_form.save(commit=False)
            # capture instance of the filled out form's habit so you can show on template
            new_record.habit = habit
            new_record.save()
            return redirect('home')
    form = RecordForm()
    return render(request, 'core/add_record.html', {'form': form, 'habit': habit})
