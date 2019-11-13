from django.shortcuts import render
from django.views.generic import ListView
from tracker.models import Entry
from tracker.models import Workout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django import forms


def dashboard(request):
	# only entries for current user should show
	workouts = Workout.objects.filter(author_id = request.user.id).order_by('-workout_date')
	entries = Entry.objects.filter(entry_id__in=workouts)
	context = {
		'workouts': workouts,
		'entries': entries
	}

	return render(request, 'tracker/dashboard.html', context)

class DashboardView(ListView):
	model = Entry.objects.filter()
	template_name = 'tracker/dashboard.html'
	context_object_name = 'entries'

	def get_context_data(self, **kwargs):
	    context = super(DashboardView, self).get_context_data(**kwargs)
	    data = Entry.objects.all()
	    context.update({'data': data})
	    return context

# class WorkoutCreateForm(forms.Form):
# 	class Meta:
# 		model = Workout

# 	title = forms.CharField(label='Workout Name')
# 	title = forms.CharField(label='Workout Name')
# 	workout_date = forms.DateTimeField(label='Date of Workout')
# 	time_in_minutes = forms.IntegerField(label='Time in Minutes')

# LoginRequiredMixin makes it so that a user who isn't logged in can't access 
# the page to create a view
class WorkoutCreateView(LoginRequiredMixin, CreateView):
	model = Workout
	fields = ['title', 'workout_date', 'time_in_minutes']

	
