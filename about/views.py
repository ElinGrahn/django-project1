from django.shortcuts import render

# Create your views here.
def about_me(request):
    return HttpResponse("This would me an about page")