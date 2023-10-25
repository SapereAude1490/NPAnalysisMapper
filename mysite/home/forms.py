from django import forms
from .models import CSVFile
from .models import Experiment

class ExperimentForm(forms.ModelForm):
    class Meta:
        model = Experiment
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 30, 'rows': 1}),
        }

class MultipleCSVFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleCSVFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleCSVFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class CSVFilesForm(forms.ModelForm):
    class Meta:
        model = CSVFile
        fields = ('file',)

    file = MultipleCSVFileField()  # Use the custom MultipleFileField for the csv_files field



# class MultipleFileInput(forms.ClearableFileInput):
#     allow_multiple_selected = True

# class MultipleFileField(forms.FileField):
#     def __init__(self, *args, **kwargs):
#         kwargs.setdefault("widget", MultipleFileInput())
#         super().__init__(*args, **kwargs)

#     def clean(self, data, initial=None):
#         single_file_clean = super().clean
#         if isinstance(data, (list, tuple)):
#             result = [single_file_clean(d, initial) for d in data]
#         else:
#             result = single_file_clean(data, initial)
#         return result

# class ExperimentForm(forms.ModelForm):
#     csv_files = MultipleFileField()  # Use the custom MultipleFileField for the csv_files field

#     class Meta:
#         model = Experiment
#         fields = ['name', 'description', 'csv_files']

# class CSVFileForm(forms.ModelForm):
#     file = forms.FileField()
#     class Meta:
#         model = CSVFile
#         fields = ['file']

# class ExperimentForm(forms.ModelForm):
#     name = forms.CharField(max_length=255)
#     description = forms.CharField(widget=forms.Textarea)
#     csv_files = forms.FileField()
#     class Meta:
#         model = Experiment
#         fields = ['name', 'description', 'csv_files']

# # class UploadForm(forms.ModelForm):
# #     name = forms.CharField(max_length=255)
# #     description = forms.CharField(widget=forms.Textarea)
# #     class Meta:
# #         model = Experiment
# #         fields = ['name', 'description']