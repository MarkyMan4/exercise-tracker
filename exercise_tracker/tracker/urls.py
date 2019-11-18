from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='tracker-dashboard'),
    path('create/', views.workout_create, name='workout-create'),
    path('create/entry/<int:id>/', views.entry_create, name='entry-create'),
    path('details/<int:id>/', views.workout_detail, name='workout-detail')
]
