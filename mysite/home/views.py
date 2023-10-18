from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") # string of HTML code
    return render(request, "home.html", {})

# Function for when the button is clicked

def importCsvButtonClicked(request):
    # Handle the button click logic here
    print('ImportCsv button clicked in Django view.')

    # You can return a JSON response if needed
    return JsonResponse({'message': 'ImportCsv button clicked in Django view.'})    