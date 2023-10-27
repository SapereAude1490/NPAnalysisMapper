from django.urls import path

from . import views

urlpatterns = [

    path('', views.home_view, name='home_view'),
    path('delete_experiment/<int:experiment_id>/', views.delete_experiment, name='delete_experiment'),
    path('process_data/',views.process_data_view, name='process_data_view'),
    #path('displayForm/', views.displayForm, name='displayForm'),
]


