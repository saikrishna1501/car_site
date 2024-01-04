from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
# Create your views here.

def list_view(request):
    cars = models.Car.objects.all()
    return render(request, "cars/list.html", context={"cars": cars})


def add_view(request):
    if request.POST:
        brand = request.POST["brand"]
        year = int(request.POST["year"])
        models.Car.objects.create(brand=brand, year=year)
        return redirect(reverse("cars:list-cars"))
    else:
        return render(request, "cars/add.html")

def delete_view(request):
    if request.POST:
        pk = request.POST["pk"]
        try:
            models.Car.objects.get(pk=pk).delete()
        except:
            print("PK not found")
        return redirect(reverse("cars:list-cars"))
    else:
        return render(request, "cars/delete.html")