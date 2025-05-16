"""
URL configuration for hello_django_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse, JsonResponse
import math 
def rectangle_area(request, width, length):
    try:
        area = length * width
        return HttpResponse(f"<h1>Rectangle Area:{area}</h1>")
    except ValueError:
        return JsonResponse({'error': 'Please provide both length and width'}, status=400)

def rectangle_area_query(request):
    try:
        width = int(request.GET.get("width"))
        height = int(request.GET.get("height"))
        area = width * height
        return HttpResponse(f"<h1>Rectangle Area: {area}</h1>")
    except (TypeError, ValueError):
        return JsonResponse({"error": "Width and height must be provided as numbers."}, status=400)

def rectangle_perimeter(request, length, width):
    try:
        perimeter = 2 * (length + width)
        return HttpResponse(f"<h1>rectangle perimeter: {perimeter}</h1>")
    except:
        return JsonResponse({"error" : "Please provide both length and width"})

def rectangle_perimeter_query(request):
    try:
            length = int(request.GET.get("length"))
            width = int(request.GET.get("width"))
            perimeter = 2 * (length + width)
            return HttpResponse(f"<h1>Rectangle Perimeter: {perimeter}</h1>")
    except (TypeError, ValueError):
        return JsonResponse({"error": "Width and length must be provided as numbers."}, status=400 )
def circle_area(request, radius):
    try:
        area = math.pi * pow(radius, 2)
        return HttpResponse(f"<h1>Circle Area: {area}</h1>")
    except:
        return JsonResponse({{"error" : "Please provide a radius"}})


def circle_perimeter(request, radius):
    try:
        perimeter = 2 * math.pi * radius
        return HttpResponse(f"<h1>Circle perimeter: {perimeter}</h1>")
    except:
        return JsonResponse({'error': "Please provide a radius"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rectangle/area/<int:width>/<int:length>/', rectangle_area),
    path('rectangle/area/', rectangle_area_query),
    path('rectangle/perimeter/<int:width>/<int:length>/', rectangle_perimeter),
    path('rectangle/perimeter/', rectangle_perimeter_query),
    path('circle/area/<int:radius>', circle_area),
    path('circle/perimeter/<int:radius>', circle_perimeter)
]
