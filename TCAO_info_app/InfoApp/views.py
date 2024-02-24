from django.shortcuts import render

# Create your views here.

def main(request):
    template_file = "InfoApp/main.html"
    
    options = {}
    
    return render(request, template_file, options)