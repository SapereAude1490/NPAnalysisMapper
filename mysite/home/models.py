from django.db import models
import os

# Create your models here.

def experiment_csv_upload_path(instance, filename):
    # instance is the CSVFile object, and filename is the original CSV file name
    # Create a folder with the experiment name and keep the original file name
    return os.path.join('datasets/csv_files/', instance.experiment.name, filename)

class Experiment(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    numpy_file = models.FileField(upload_to='datasets/numpy_files/')

class CSVFile(models.Model):
    file = models.FileField(upload_to=experiment_csv_upload_path)
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE, default=None, null=True, blank=True)