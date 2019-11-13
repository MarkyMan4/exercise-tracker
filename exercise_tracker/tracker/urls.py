from django.urls import path
from .views import WorkoutCreateView
from . import views

urlpatterns = [
    path('', views.dashboard, name='tracker-dashboard'),
    path('workout/new/', WorkoutCreateView.as_view(), name='workout-create'),
]
