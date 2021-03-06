from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def home(request):
	return render(request, 'info/home.html')

def analysis(request):
    return render(request, 'info/analysis.html')

def simple_upload(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		print("1")
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		return render(request, 'info/simple_upload.html',{'uploaded_file_url': uploaded_file_url})
	return render(request, 'info/simple_upload.html')