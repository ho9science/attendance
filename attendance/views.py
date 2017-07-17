from django.shortcuts import render

def home(request):
	return render(request, 'info/home.html')

def analysis(request):
    return render(request, 'info/analysis.html')