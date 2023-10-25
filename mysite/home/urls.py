from django.urls import path

from . import views

urlpatterns = [

    path('', views.home_view, name='home_view'),
    path('delete_experiment/<int:experiment_id>/', views.delete_experiment, name='delete_experiment'),
    #path('displayForm/', views.displayForm, name='displayForm'),
]


