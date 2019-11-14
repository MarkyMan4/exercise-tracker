from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='tracker-dashboard'),
    path('create/', views.workout_create, name='workout-create'),
    path(r'create/entry/<int:id>', views.entry_create, name='entry-create'),
]
