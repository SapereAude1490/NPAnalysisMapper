from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

# These apps are stored separately in the DjangoDash folder.
from DjangoDash.dashapps import app
from DjangoDash.loadingbardash import appBar
from django.views.generic.edit import FormView

# Forms for importing data
from .forms import CSVFile, CSVFilesForm, ExperimentForm
from .models import Experiment
import shutil
import os


# Create your views here.

from django.db import IntegrityError

def home_view(request):
    experiments = Experiment.objects.all()

    if request.method == 'POST':
        # If the form has been submitted, process the data
        form = ExperimentForm(request.POST)
        csv_form = CSVFilesForm(request.POST, request.FILES)
        if form.is_valid() and csv_form.is_valid():
            try:
                experiment = form.save()  # Save the experiment and get the instance
                csv_files = csv_form.cleaned_data['file']  # Get the uploaded CSV files
                for csv_file in csv_files:
                    CSVFile.objects.create(experiment=experiment, file=csv_file)  # Associate the CSV files with the experiment
                messages.success(request, 'Experiment created successfully.')
                return redirect('home_view')
            except IntegrityError:
                messages.error(request, 'An experiment with that name already exists.')
    else:
        # If it's a GET request or the form is not valid, display the form
        form = ExperimentForm()
        csv_form = CSVFilesForm()

    return render(request, 'importExperiment.html', {'form': form, 'experiments': experiments, 'csv_form': csv_form})


def delete_experiment(request, experiment_id):
    experiment = Experiment.objects.get(id=experiment_id)
    experiment_folder = os.path.join('media/datasets/csv_files/', experiment.name)
    shutil.rmtree(experiment_folder)  # Delete the experiment folder and all its contents
    experiment.delete()
    messages.success(request, 'Entry Deleted')
    return redirect('home_view')
