from django.shortcuts import render

# Create your views here.
def index_views(request):
    return render(request,'index.html')
