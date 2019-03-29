from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image
# Create your views here.

def index(request):
  print(request.FILES)
  print(request)
  print("cbvgjxbh")
  if request.method == 'POST' and request.FILES['myfile']:
  	myfile = request.FILES['myfile']
  	print(myfile)
  	try:
  		Image.open(myfile)
  	except IOError:
  		# return render(request, 'main_app/index.html',status=400,{'error': 'Not a valid Image'})
  		return render(request, 'main_app/index.html',{'error': 'Not a valid Image'}, status=400)
  	fs = FileSystemStorage()
  	filename = fs.save(myfile.name, myfile)
  	uploaded_file_url = fs.url(filename)
  	return render(request, 'main_app/image.html', {'uploaded_file_url': uploaded_file_url})
  return render(request, 'main_app/index.html',{'error': ''})